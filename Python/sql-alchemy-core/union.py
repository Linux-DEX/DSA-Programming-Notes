import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://xander:xander@localhost/testdb")

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `payment` TABLE FROM THE METADATA OBJECT
payment = meta_data.tables['payment']

# PREPARING THE REQUIRED QUERY
query_1 = db.select(payment).filter(payment.c.payment_id == 1)
query_2 = db.select(payment).filter(payment.c.payment_id == 2)
query_3 = db.select(payment).filter(payment.c.payment_id == 3)

query = db.union(query_1, query_2, query_3)

# EXTRACTING RECORDS USING THE ENGINE AND QUERY
with engine.connect() as conn:
    result = conn.execute(query).all()

# PRINT THE RESULTANT RECORDS
for r in result:
    print(r.payment_id, "|", r.customer_id, "|", r.rental_id, "|", r.amount)
