# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector

app = FastAPI(title="Voter NID API")


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jenifer12",
        database="credit_system",
    )


def get_voter_cache(nid):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM voter_cache
        WHERE nid = %s
        """,
        (nid,),
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def save_voter_cache(voter):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO voter_cache (
            nid,
            full_name,
            gender,
            dob,
            province_name,
            commune_name,
            election_office_name,
            registration_year
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
            full_name = VALUES(full_name),
            gender = VALUES(gender),
            dob = VALUES(dob),
            province_name = VALUES(province_name),
            commune_name = VALUES(commune_name),
            election_office_name = VALUES(election_office_name),
            registration_year = VALUES(registration_year)
        """,
        (
            voter["nid"],
            voter["name"],
            voter["gender"],
            voter["dob"],
            voter["province_name"],
            voter["commune_name"],
            voter["election_office_name"],
            voter["registration_year"],
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()


class NIDRequest(BaseModel):
    nid: str


def run_selenium(nid_list: List[str]):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.javascript": 1}
    )

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 800)
    wait = WebDriverWait(driver, 10)

    results_data = []

    try:
        driver.get("https://voterlist.nec.gov.kh")

        for nid in nid_list:
            try:
                # Reset tab each time to prevent stale elements
                wait.until(EC.element_to_be_clickable((By.ID, "by_id")))
                nid_tab = driver.find_element(By.ID, "by_id")
                driver.execute_script("arguments[0].click();", nid_tab)

                # Find input field
                wait.until(EC.presence_of_element_located((By.ID, "id_no")))
                nid_input = driver.find_element(By.ID, "id_no")
                nid_input.clear()
                nid_input.send_keys(str(nid))

                # Submit form directly instead of button click chain
                driver.execute_script("""
                    document.getElementById("Activetab").value = "3";
                    document.getElementById("myForm").submit();
                """)

                # Re-fetch rows after page update
                rows = driver.find_elements(By.XPATH, "//table/tbody/tr[position()>1]")
                found_any = False

                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    data = [c.text.strip() for c in cols]

                    if len(data) > 5:
                        found_any = True
                        results_data.append(
                            {
                                "range_list": data[0],
                                "id": data[1],
                                "file_type": data[2],
                                "nid": str(nid),
                                "name": data[4],
                                "gender": data[5],
                                "dob": data[6],
                                "province_id": data[7].split(") ")[0].replace("(", ""),
                                "province_name": (
                                    data[7].split(") ")[1] if ") " in data[7] else ""
                                ),
                                "commune_id": data[8].split(") ")[0].replace("(", ""),
                                "commune_name": (
                                    data[8].split(") ")[1] if ") " in data[8] else ""
                                ),
                                "election_office_id": data[9]
                                .split(") ")[0]
                                .replace("(", ""),
                                "election_office_name": (
                                    data[9].split(") ")[1] if ") " in data[9] else ""
                                ),
                                "registration_year": data[10],
                            }
                        )

                if not found_any:
                    results_data.append(
                        {"nid": str(nid), "error": "Not found on website"}
                    )

            except Exception as e:
                results_data.append({"nid": str(nid), "error": str(e)})

    finally:
        driver.quit()

    return results_data


@app.get("/")
def home():
    return {"message": "✅ Voter NID API is running", "endpoint": "/api/search"}


@app.post("/search")
def search(request: NIDRequest):

    nid = request.nid

    cached = get_voter_cache(nid)

    if cached:
        return {
            "status": "success",
            "source": "mysql",
            "data": {
                "nid": cached["nid"],
                "name": cached["full_name"],
                "gender": cached["gender"],
                "dob": cached["dob"],
                "province_name": cached["province_name"],
                "commune_name": cached["commune_name"],
                "election_office_name": cached["election_office_name"],
                "registration_year": cached["registration_year"],
            },
        }

    selenium_results = run_selenium([nid])

    if selenium_results:

        voter = selenium_results[0]

        if "error" not in voter:

            save_voter_cache(voter)

            voter["source"] = "selenium"

            return {"status": "success", "source": "selenium", "data": voter}

        return {"status": "fail", "data": voter}

    return {"status": "fail", "message": "No data found"}
