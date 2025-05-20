from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from logger import logger

# Use MySQL instead of SQLite
engine = create_engine("mysql+pymysql://xander:xander@localhost/testdb", echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)

    fees = relationship("Fee", backref="student", cascade="all, delete-orphan")


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id"))


# Create tables in the MySQL database
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
s1 = Student(name="John Doe", age=20)
session.add(s1)
session.commit()  # Commit first to get the id populated

f1 = Fee(amount=100, student_id=s1.id)
f2 = Fee(amount=200, student_id=s1.id)
session.add_all([f1, f2])
session.commit()

# Query and log
student_fees = session.query(Student).filter_by(name="John Doe").one().fees
for fee in student_fees:
    logger.info(fee.amount)
