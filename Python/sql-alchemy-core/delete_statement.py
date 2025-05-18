from sqlalchemy import text, create_engine, MetaData
from logger import logger

# Assuming your engine is already defined
engine = create_engine('mysql+pymysql://xander:xander@localhost/testdb', echo=True)

# Reflect metadata
meta = MetaData()
meta.reflect(bind=engine)

# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

conn = engine.connect()

# delete
dele = BOOKS.delete().where(BOOKS.c.genre == "non-fiction")
conn.execute(dele)

# write the SQL query inside the
# text() block to fetch all records
sql = text("SELECT * from books")

# Fetch all the records
result = conn.execute(sql).fetchall()

# View the records
for record in result:
    logger.info(f"\n{record}")

conn.commit()
conn.close()
