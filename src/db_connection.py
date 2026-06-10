from sqlalchemy import create_engine

DATABASE_URL = "postgresql://jeetshah3011@localhost/warehouse_db"

engine = create_engine(DATABASE_URL)

print("Database Connected Successfully")