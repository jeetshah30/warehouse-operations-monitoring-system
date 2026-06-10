import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

employees = pd.read_sql(
    "SELECT * FROM employees",
    engine
)

st.title("👷 Employees Dashboard")

total_units = employees["units_picked"].sum()

top_employee = employees.loc[
    employees["units_picked"].idxmax(),
    "employee_name"
]

avg_units = round(
    employees["units_picked"].mean(),
    2
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Units Picked", total_units)
col2.metric("Top Performer", top_employee)
col3.metric("Average Productivity", avg_units)

st.dataframe(employees)
