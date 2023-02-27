from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from time import sleep
from psycopg2.extras import RealDictCursor
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Alicegold1987@localhost/fastapi"

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        



# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'Alicegold1987', cursor_factory=RealDictCursor )
#         cursor = conn.cursor()
#         print('database connected sucessfully')
#         break
#     except Exception as error:
#         print('connection to database failed')
#         print({"Error": error})
#         sleep(3)
    