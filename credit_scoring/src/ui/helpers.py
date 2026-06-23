import re

import streamlit as st


@st.dialog("⚠ Manual Review Required")
def show_manual_review_popup():
    st.warning("""
        The provided National ID could not be verified through:

        • Existing customer records
        • National voter verification system

        Please conduct **manual identity verification**
        before proceeding with the assessment.
        """)

    if st.button("OK", use_container_width=True):
        st.session_state["manual_review_required"] = True
        st.rerun()


@st.dialog("Identity Verification Required")
def show_nid_popup():
    st.error("National ID (NID) is required before performing credit assessment.")
    st.info("Please enter and verify the applicant's National ID.")


def parse_numeric_string(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        matches = re.findall(r"\d+\.?\d*", value)
        if matches:
            return float(matches[0])
    return None


def parse_percentage(value):
    numeric = parse_numeric_string(value)
    return numeric / 100.0 if numeric is not None else None


def parse_int_value(value):
    numeric = parse_numeric_string(value)
    return int(numeric) if numeric is not None else None
