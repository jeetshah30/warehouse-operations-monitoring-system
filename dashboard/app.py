import streamlit as st
import plotly.express as px

from sqlalchemy import create_engine

import pandas as pd

DATABASE_URL = "postgresql://jeetshah3011@localhost/warehouse_db"

engine = create_engine(DATABASE_URL)

query = """

SELECT

    COUNT(*) AS total_products,

    SUM(quantity) AS total_inventory,

    COUNT(

        CASE

            WHEN quantity < reorder_level

            THEN 1

        END

    ) AS low_stock_products

FROM inventory;

"""

metrics = pd.read_sql(query, engine)

st.set_page_config(

    page_title="Warehouse Operations Monitoring System",

    layout="wide"

)

st.title("📦 Warehouse Operations Monitoring System")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "Total Products",

        int(metrics["total_products"][0])

    )

with col2:

    st.metric(

        "Total Inventory",

        int(metrics["total_inventory"][0])

    )

with col3:

    st.metric(

        "Low Stock Products",

        int(metrics["low_stock_products"][0])

    )

st.subheader("Inventory Data")

inventory = pd.read_sql(

    "SELECT * FROM inventory",

    engine

)

st.dataframe(inventory)
st.subheader("Inventory Data")

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

low_stock = inventory[
    inventory["quantity"] <
    inventory["reorder_level"]
]

st.dataframe(
    low_stock[
        [
            "product_name",
            "quantity",
            "reorder_level"
        ]
    ]
)