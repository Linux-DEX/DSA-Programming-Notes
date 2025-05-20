from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    select,
)
from logger import logger

engine = create_engine("sqlite:///:memory:", echo=True)
metadata = MetaData()

customers_table = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

orders_table = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("item", String),
)

metadata.create_all(engine)

connection = engine.connect()

insert_customers = customers_table.insert().values(
    [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
)
connection.execute(insert_customers)

insert_orders = orders_table.insert().values(
    [
        {"customer_id": 1, "item": "Laptop"},
        {"customer_id": 2, "item": "Tablet"},
        {"customer_id": 1, "item": "Keyboard"},
    ]
)
connection.execute(insert_orders)

# Inner Join
join_stmt = select(customers_table.c.name, orders_table.c.item).select_from(
    customers_table.join(
        orders_table, customers_table.c.id == orders_table.c.customer_id
    )
)
result = connection.execute(join_stmt)
logger.info("Inner Join:")
for row in result:
    logger.info(row)

# Left Outer Join
left_join_stmt = select(customers_table.c.name, orders_table.c.item).select_from(
    customers_table.outerjoin(
        orders_table, customers_table.c.id == orders_table.c.customer_id
    )
)
result = connection.execute(left_join_stmt)
logger.info("\nLeft Outer Join:")
for row in result:
    logger.info(row)

connection.close()
