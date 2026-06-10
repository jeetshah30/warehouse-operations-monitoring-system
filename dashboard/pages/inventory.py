import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

inventory = pd.read_sql(
    "SELECT * FROM inventory",
    engine
)

st.title("📦 Inventory Dashboard")

total_products = len(inventory)

total_inventory = inventory["quantity"].sum()

low_stock = inventory[
    inventory["quantity"] < inventory["reorder_level"]
]

low_stock_count = len(low_stock)

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", total_products)
col2.metric("Total Inventory Units", total_inventory)
col3.metric("Low Stock Products", low_stock_count)

st.subheader("Inventory Levels")

fig = px.bar(
    inventory,
    x="product_name",
    y="quantity",
    title="Inventory by Product"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🚨 Low Stock Alerts")

st.dataframe(
    low_stock[
        [
            "product_name",
            "quantity",
            "reorder_level"
        ]
    ]
)

st.subheader("Inventory Data")

st.dataframe(inventory)