from sqlalchemy import create_engine
from logger import logger

# defining the database credentials
user = "xander"
password = "xander"
host = "127.0.0.1"
port = 3306
database = "testdb"


# return sqlalchemy engine object
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    try:
        # get the connection object for the database
        engine = get_connection()
        logger.info(f"Connection to the {host} for {user} created successfully.")
    except Exception as ex:
        logger.error("Connection could not be made due to: \n", ex)
