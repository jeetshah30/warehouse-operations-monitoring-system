import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Warehouse Data Quality & Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

[data-testid="metric-container"] {
    background-color: #f8f9fa;
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 4px rgba(0,0,0,0.08);
}

h1 {
    color: #1f4e79;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("📊 Warehouse Analytics")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Navigate using the pages menu.

    • Executive Dashboard

    • Inventory

    • Orders

    • Shipments

    • Employees

    • Data Quality
    """
)

# -----------------------------
# DATABASE
# -----------------------------

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

inventory = pd.read_sql(
    "SELECT * FROM inventory",
    engine
)

orders = pd.read_sql(
    "SELECT * FROM orders",
    engine
)

shipments = pd.read_sql(
    "SELECT * FROM shipments",
    engine
)

employees = pd.read_sql(
    "SELECT * FROM employees",
    engine
)

# -----------------------------
# KPIs
# -----------------------------

inventory_units = int(
    inventory["quantity"].sum()
)

low_stock = len(
    inventory[
        inventory["quantity"]
        < inventory["reorder_level"]
    ]
)

pending_orders = len(
    orders[
        orders["status"] == "Pending"
    ]
)

delivered_shipments = len(
    shipments[
        shipments["status"] == "Delivered"
    ]
)

top_employee = employees.loc[
    employees["units_picked"].idxmax(),
    "employee_name"
]

# -----------------------------
# HEADER
# -----------------------------

st.title(
    "📊 Warehouse Data Quality & Analytics Platform"
)

st.caption(
    "Executive dashboard for warehouse operations, analytics and data quality monitoring."
)

# -----------------------------
# TABS
# -----------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "Overview",
        "Analytics",
        "Data Explorer"
    ]
)

# =====================================================
# OVERVIEW
# =====================================================

with tab1:

    st.subheader("Executive KPIs")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📦 Inventory Units",
        inventory_units
    )

    col2.metric(
        "📋 Orders",
        len(orders)
    )

    col3.metric(
        "🚚 Shipments",
        len(shipments)
    )

    col4.metric(
        "👷 Employees",
        len(employees)
    )

    st.subheader("Warehouse Health")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "⚠️ Low Stock",
        low_stock
    )

    col2.metric(
        "⏳ Pending Orders",
        pending_orders
    )

    col3.metric(
        "✅ Delivered",
        delivered_shipments
    )

    col4.metric(
        "🏆 Top Employee",
        top_employee
    )

    st.subheader("Executive Summary")

    if low_stock > 0:
        st.warning(
            f"{low_stock} products require replenishment."
        )
    else:
        st.success(
            "Inventory levels are healthy."
        )

    if pending_orders > 0:
        st.warning(
            f"{pending_orders} orders remain pending."
        )

    st.info(
        f"{top_employee} is currently the highest-performing employee."
    )

# =====================================================
# ANALYTICS
# =====================================================

with tab2:

    left_col, right_col = st.columns(2)

    with left_col:

        fig_inventory = px.bar(
            inventory,
            x="product_name",
            y="quantity",
            title="Inventory Levels"
        )

        st.plotly_chart(
            fig_inventory,
            use_container_width=True
        )

    with right_col:

        fig_employee = px.bar(
            employees,
            x="employee_name",
            y="units_picked",
            title="Employee Productivity"
        )

        st.plotly_chart(
            fig_employee,
            use_container_width=True
        )

    left_col, right_col = st.columns(2)

    with left_col:

        order_status = (
            orders["status"]
            .value_counts()
            .reset_index()
        )

        order_status.columns = [
            "Status",
            "Count"
        ]

        fig_orders = px.pie(
            order_status,
            names="Status",
            values="Count",
            title="Order Status Breakdown"
        )

        st.plotly_chart(
            fig_orders,
            use_container_width=True
        )

    with right_col:

        shipment_status = (
            shipments["status"]
            .value_counts()
            .reset_index()
        )

        shipment_status.columns = [
            "Status",
            "Count"
        ]

        fig_shipments = px.bar(
            shipment_status,
            x="Status",
            y="Count",
            title="Shipment Status"
        )

        st.plotly_chart(
            fig_shipments,
            use_container_width=True
        )

# =====================================================
# DATA EXPLORER
# =====================================================

with tab3:

    with st.expander(
        "📦 Inventory Data"
    ):
        st.dataframe(inventory)

    with st.expander(
        "📋 Orders Data"
    ):
        st.dataframe(orders)

    with st.expander(
        "🚚 Shipment Data"
    ):
        st.dataframe(shipments)

    with st.expander(
        "👷 Employee Data"
    ):
        st.dataframe(employees)

st.success(
    "Platform Status: Operational"
)

