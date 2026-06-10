import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

shipments = pd.read_sql(
    "SELECT * FROM shipments",
    engine
)

st.title("🚚 Shipments Dashboard")

total_shipments = len(shipments)

delivered = len(
    shipments[shipments["status"] == "Delivered"]
)

delayed = len(
    shipments[shipments["status"] == "Delayed"]
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Shipments", total_shipments)
col2.metric("Delivered", delivered)
col3.metric("Delayed", delayed)

st.dataframe(shipments)

import plotly.express as px

status_counts = (
    shipments["status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = ["status", "count"]

fig = px.bar(
    status_counts,
    x="status",
    y="count",
    title="Shipment Status Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)