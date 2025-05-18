import sqlalchemy as db
from logger import logger

# define the engine
# engine = db.create_engine('mysql+mysqlconnector://xander:xander@localhost/testdb', echo=True) # for mysql-connector-python package
engine = db.create_engine('mysql+pymysql://xander:xander@localhost/testdb', echo=True) # for pymysql package

# create the metadata object
metadata_obj = db.MetaData()

profile = db.Table(
    "profile",
    metadata_obj,
    db.Column("email", db.String(255), primary_key=True),
    db.Column("name", db.String(255)),
    db.Column("contact", db.String(20)),
)

try:
    # Create the profile table
    metadata_obj.create_all(engine)
    logger.info(f"Created the table")
except Exception as e:
    logger.exception(e)
