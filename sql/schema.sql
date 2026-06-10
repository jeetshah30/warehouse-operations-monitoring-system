CREATE TABLE inventory (
    sku_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    reorder_level INT,
    warehouse_location VARCHAR(50),
    last_updated DATE
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    order_date DATE,
    ship_date DATE,
    quantity INT,
    status VARCHAR(50)
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100),
    shift VARCHAR(20),
    units_picked INT
);

CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    shipment_type VARCHAR(20),
    shipment_date DATE,
    status VARCHAR(50)
);