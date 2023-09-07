import uuid
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.postgresql import UUID
from config.db import meta, engine

users = Table('users', meta, 
              Column('id', Integer, primary_key=True, unique=True), 
              Column('field_1', String(255), nullable=False), 
              Column('author', String(255), nullable=False), 
              Column('description', String(255), nullable=False), 
              Column('my_numeric_field', Integer, nullable=False))

meta.create_all(engine)