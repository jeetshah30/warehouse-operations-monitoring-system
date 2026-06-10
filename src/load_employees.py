import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(

    "postgresql://jeetshah3011@localhost/warehouse_db"

)

employees = pd.read_csv("data/employees.csv")

employees.to_sql(

    "employees",

    engine,

    if_exists="append",

    index=False

)

print("Employees Loaded Successfully")
