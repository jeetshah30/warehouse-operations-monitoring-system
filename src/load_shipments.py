import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://jeetshah3011@localhost/warehouse_db"
)

shipments = pd.read_csv("data/shipments.csv")

shipments.to_sql(
    "shipments",
    engine,
    if_exists="append",
    index=False
)

print("Shipments Loaded Successfully")