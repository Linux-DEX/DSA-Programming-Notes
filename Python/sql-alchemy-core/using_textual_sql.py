from sqlalchemy import text, create_engine, MetaData
from logger import logger

# Assuming your engine is already defined
engine = create_engine('mysql+pymysql://xander:xander@localhost/testdb', echo=True)

#! execute insert query

# Define raw SQL
sql = text('SELECT * FROM books WHERE book_price > 100')

# Manually open and close connection
conn = engine.connect()
try:
    result = conn.execute(sql).fetchall()
    for record in result:
        logger.info(f"\n {record}")
finally:
    conn.close()

#! execute insert query

data = [
    {
        "book_id": 6,
        "book_price": 400,
        "genre": "fiction",
        "book_name": "yoga is science"
    },
    {
        "book_id": 7,
        "book_price": 800,
        "genre": "non-fiction",
        "book_name": "alchemy tutorials"
    }
]

# Define the insert SQL query using text() and named params
insert_stmt = text("""
    INSERT INTO books (book_id, book_price, genre, book_name)
    VALUES (:book_id, :book_price, :genre, :book_name)
""")

conn = engine.connect()
try:
    # Insert each row of data
    for entry in data:
        conn.execute(insert_stmt, entry)

    # Commit the transaction to persist inserts
    conn.commit()

    # Run a SELECT query
    select_stmt = text("SELECT * FROM books WHERE book_price > 100")
    results = conn.execute(select_stmt).fetchall()

    # Print each result
    for record in results:
        logger.info(f"\n {record}")

finally:
    # close connection
    conn.close()

#! Executing update query

# Reflect metadata
meta = MetaData()
meta.reflect(bind=engine)

# Get the `books` table from the metadata
BOOKS = meta.tables['books']

# Update query: change genre from 'non-fiction' to 'sci-fi'
update_stmt = BOOKS.update().where(BOOKS.c.genre == 'non-fiction').values(genre='sci-fi')

# Use connection with transaction
with engine.begin() as conn: 
    # Execute update
    conn.execute(update_stmt)

    result = conn.execute(text("SELECT * FROM books")).fetchall()

    # Print the records
    for record in result:
        logger.info(record)

#! Executing delete query

# Reflect metadata
meta = MetaData()
meta.reflect(bind=engine)

# Get the `books` table from the Metadata object
BOOKS = meta.tables['books']

# delete
dele = BOOKS.delete().where(BOOKS.c.genre == "fiction")

conn = engine.connect()

# Using transaction to ensure commit
with conn.begin(): 
    conn.execute(dele)

# Verify the delete by fetching records
sql = text("SELECT * from books")

result = conn.execute(sql).fetchall()
conn.close()

# View the records
for record in result:
    logger.info("\n{record}")

