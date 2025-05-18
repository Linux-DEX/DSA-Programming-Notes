from sqlalchemy.sql import select, alias
from sqlalchemy import create_engine, MetaData 
from logger import logger

# connect to MySql
engine = create_engine('mysql+pymysql://xander:xander@localhost/testdb', echo=True)

# metadata usage 
meta = MetaData()
meta.reflect(bind=engine)

# Get the books table from the Metadata object
BOOKS = meta.tables['books']

# using alias
b = BOOKS.alias('a')

# SQLAlchemy Query to select all rows where book_id > 2 
query = select(b).where(b.c.book_id > 2)

# Automatically open and close; Execute the query using a connection
with engine.connect() as conn:
    result_set = conn.execute(query)
    records = result_set.fetchall()

# Print the records
for record in records:
    logger.info(f"\n{record}")

