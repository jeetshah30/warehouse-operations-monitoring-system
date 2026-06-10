import pandas as pd

inventory = pd.read_csv("data/inventory.csv")

total_products = len(inventory)

total_inventory = inventory["quantity"].sum()

low_stock_count = len(

    inventory[

        inventory["quantity"] < inventory["reorder_level"]

    ]

)

print("\nWAREHOUSE SUMMARY\n")

print(f"Total Products: {total_products}")

print(f"Total Inventory Units: {total_inventory}")

print(f"Low Stock Products: {low_stock_count}")