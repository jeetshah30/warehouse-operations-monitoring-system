import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Inventory Forecasting & Reorder Analytics")

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

inventory = pd.read_sql(
    "SELECT * FROM inventory",
    engine
)

st.subheader("Current Inventory Status")

st.dataframe(inventory)

# Inventory Risk Analysis

inventory["Risk Level"] = inventory.apply(
    lambda x:
    "High Risk"
    if x["quantity"] <= x["reorder_level"]
    else "Safe",
    axis=1
)

st.subheader("Inventory Risk Analysis")

risk_counts = (
    inventory["Risk Level"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Risk Level",
    "Count"
]

fig = px.pie(
    risk_counts,
    names="Risk Level",
    values="Count",
    title="Inventory Risk Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Reorder Recommendations

st.subheader("📦 Reorder Recommendations")

reorder_df = inventory[
    inventory["quantity"]
    <= inventory["reorder_level"]
]

if len(reorder_df) > 0:

    st.warning(
        f"{len(reorder_df)} products require replenishment."
    )

    st.dataframe(
        reorder_df[
            [
                "product_name",
                "quantity",
                "reorder_level"
            ]
        ]
    )

else:

    st.success(
        "All products are sufficiently stocked."
    )

# Inventory Visualization

st.subheader("Inventory Levels")

fig2 = px.bar(
    inventory,
    x="product_name",
    y="quantity",
    color="Risk Level",
    title="Inventory Levels by Product"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)