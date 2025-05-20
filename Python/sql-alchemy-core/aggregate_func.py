import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://xander:xander@localhost/testdb")
meta_data = db.MetaData()
meta_data.reflect(bind=engine)

payment_table = meta_data.tables['payment']
query = db.select(db.func.min(payment_table.c.amount))

with engine.connect() as conn:
    result = conn.execute(query).first()
    print(result[0])
