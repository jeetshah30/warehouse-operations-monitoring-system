import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

orders = pd.read_sql(
    "SELECT * FROM orders",
    engine
)

st.title("📋 Orders Dashboard")

total_orders = len(orders)

shipped_orders = len(
    orders[orders["status"] == "Shipped"]
)

pending_orders = len(
    orders[orders["status"] == "Pending"]
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", total_orders)
col2.metric("Shipped Orders", shipped_orders)
col3.metric("Pending Orders", pending_orders)

st.subheader("Orders Data")
st.dataframe(orders)

import plotly.express as px

status_counts = (
    orders["status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = ["status", "count"]

fig = px.pie(
    status_counts,
    names="status",
    values="count",
    title="Orders by Status"
)

st.plotly_chart(fig, use_container_width=True)