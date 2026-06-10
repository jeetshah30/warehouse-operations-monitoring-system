import streamlit as st

st.set_page_config(
    page_title="Data Lineage",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 Data Lineage")

st.markdown("""
### Data Flow Architecture

CSV / Excel Upload

⬇️

Data Profiling

⬇️

Data Validation

⬇️

Data Cleaning

⬇️

PostgreSQL Database

⬇️

Executive Dashboard
""")

st.success(
    "This page shows how data moves through the platform."
)