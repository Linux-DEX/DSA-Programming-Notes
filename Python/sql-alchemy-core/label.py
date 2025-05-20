# Import the necessary SQLAlchemy components
from sqlalchemy import *

# Create a connection to a SQLite database using a SQLAlchemy engine
engine = create_engine("sqlite:///library.db")
connection = engine.connect()

# Define a metadata object and a table object for the "student" table
metadata = MetaData()
table = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
    Column("dept", String),
)

# Create the "student" table in the database
metadata.create_all(engine)

# Insert some sample data into the "student" table
q = text("""
INSERT INTO student(id, name, age, dept) 
    VALUES
    (1, 'Mitul Rao', 20, "Comp"), 
    (2, 'Lochan Patel', 17, "Comp"), 
    (3, 'Inderjeet Ahmad', 17, "Mech"), 
    (4, 'Punita Gadhavi', 25, "Civil"), 
    (5, 'Sarvesh Mishra', 30, "Comp")
""")
connection.execute(q)

# Select all rows from the "student" table and display the results
print("\nDisplaying the table: \n")
q = text("SELECT * FROM student")
result = connection.execute(q)

for row in result.fetchall():
    print(row)

# Define a query to select the "name" column in uppercase and
# the "age" column for rows where age > 18
query = select(label("name_uppercase", func.upper(table.c.name)), table.c.age).where(
    table.c.age > 18
)

# Execute the query and print the results
print("\nDisplaying records labels with age" + "greater than 18 age: \n")
with engine.connect() as conn:
    result = connection.execute(query)

    for row in result:
        print(row)

# Close the database connection
connection.close()
