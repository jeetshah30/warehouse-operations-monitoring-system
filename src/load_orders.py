import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

orders = pd.read_csv("data/orders.csv")

orders.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print("Orders Loaded Successfully")