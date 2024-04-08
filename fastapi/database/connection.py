from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
import os

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD'],
    host="postgres",
    port=5432,
    database=os.environ['POSTGRES_DB']
)
engine = create_engine(url,echo=True)

session_pool = sessionmaker(engine)


with session_pool() as session:
    session.execute(text('SELECT 1'))
    #session.commit()
