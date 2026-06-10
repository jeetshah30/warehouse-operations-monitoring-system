import streamlit as st
import pandas as pd

st.title("📜 Audit Log")

try:

    audit_df = pd.read_csv(
        "data/audit_log.csv"
    )

    st.dataframe(audit_df)

except:

    st.warning(
        "No audit records found."
    )