import sqlalchemy
from sqlalchemy import create_engine, MetaData
from logger import logger

# connect to MySql
engine = create_engine("mysql+pymysql://xander:xander@localhost/testdb", echo=True)

# metadata usage
meta = MetaData()
meta.reflect(bind=engine)

# Get the books table from the Metadata object
BOOKS = meta.tables["books"]

# SQLAlchemy Query to select all rows with
# fiction genre
query = sqlalchemy.select(BOOKS).where(BOOKS.c.genre == "fiction")

# Automatically open and close; Execute the query using a connection
with engine.connect() as conn:
    result_set = conn.execute(query)
    records = result_set.fetchall()

# Print the records
for record in records:
    logger.info(f"\n{record}")


# Manually open and close connection
conn = engine.connect()
try:
    result_set = conn.execute(query)
    records = result_set.fetchall()
    for record in records:
        logger.info(f"\n{record}")
finally:
    conn.close()
