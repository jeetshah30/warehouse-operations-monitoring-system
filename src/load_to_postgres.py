import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://jeetshah3011@localhost/warehouse_db"

engine = create_engine(DATABASE_URL)

inventory = pd.read_csv("data/inventory.csv")

inventory.to_sql(
    "inventory",
    engine,
    if_exists="append",
    index=False
)

print("Inventory Loaded Successfully")