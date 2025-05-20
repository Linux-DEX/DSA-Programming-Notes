from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR

# connect to MySQL
engine = create_engine("mysql+pymysql://xander:xander@localhost/testdb", echo=True)

# metadata usage
meta = MetaData()
meta.reflect(bind=engine)

# define table
books = Table(
    "books",
    meta,
    Column("book_id", Integer, primary_key=True),
    Column("book_price", Numeric),
    Column("genre", VARCHAR(100)),
    Column("book_name", VARCHAR(255)),
)

# create table
meta.create_all(bind=engine)

# insert records
stmt_list = [
    books.insert().values(
        book_id=1, book_price=12.2, genre="fiction", book_name="Old age"
    ),
    books.insert().values(
        book_id=2, book_price=13.2, genre="non-fiction", book_name="Saturn rings"
    ),
    books.insert().values(
        book_id=3, book_price=121.6, genre="fiction", book_name="Supernova"
    ),
    books.insert().values(
        book_id=4, book_price=100, genre="non-fiction", book_name="History of the world"
    ),
    books.insert().values(
        book_id=5, book_price=1112.2, genre="fiction", book_name="Sun city"
    ),
]

# use a connection and commit the inserts
with engine.connect() as conn:
    for stmt in stmt_list:
        conn.execute(stmt)
    conn.commit()
