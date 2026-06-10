import pandas as pd

inventory = pd.read_csv("data/inventory.csv")

low_stock = inventory[

    inventory["quantity"] <

    inventory["reorder_level"]

]

print("LOW STOCK ALERTS")

print(low_stock[["product_name","quantity","reorder_level"]])