from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select, union, intersect, except_

# Insert data into the table
from sqlalchemy.orm import sessionmaker

# Create a new connection to the SQLite database
engine = create_engine('sqlite:///employees.db', echo=True)

Base = declarative_base()


# Defining the Employee table
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

# Create the Employee table
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# inserting values into the Employee table
session.add(Employee(name='John Doe', age=30, department='IT'))
session.add(Employee(name='Jane Smith', age=25, department='HR'))
session.add(Employee(name='John Smith', age=26, department='BD'))
session.add(Employee(name='Jane Doe', age=41, department='IT'))


session.commit()

# UNION example

# Generating the two SELECT queries
select_1 = select(Employee).where(Employee.age > 25)
select_2 = select(Employee).where(Employee.department == 'IT')

# Performing the UNION operations
union_query = select_1.union(select_2)

# Executing the query
result = session.execute(union_query).all()

# Displaying the result
for employee in result:
    print(employee.name, employee.age, employee.department)


