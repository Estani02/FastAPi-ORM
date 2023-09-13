from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from decouple import config


# Configura la conexión a la base de datos PostgreSQL
meta = MetaData()
engine = create_engine(config('DATABASE_URL'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

users = Table('users', meta, 
              Column('id', Integer, primary_key=True, unique=True), 
              Column('field_1', String(255), nullable=False), 
              Column('author', String(255), nullable=False), 
              Column('description', String(255), nullable=False), 
              Column('my_numeric_field', Integer, nullable=False))

meta.create_all(engine)