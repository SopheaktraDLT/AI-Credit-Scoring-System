import requests
import streamlit as st


def verify_nid(nid):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/search",
            json={"nid": nid},
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        if data.get("status") != "success":
            return None

        return data.get("data")

    except requests.exceptions.Timeout:
        st.error("NID verification service timed out.")
        return None

    except Exception as e:
        st.error(f"NID verification error: {e}")
        return None
