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

df = pd.read_sql(query, engine)

print("\nLOW STOCK PRODUCTS\n")
print(df)