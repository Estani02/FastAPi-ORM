from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define el modelo de la base de datos utilizando SQLAlchemy
Base = declarative_base()

class DataModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    field_1 = Column(String)
    author = Column(String)
    description = Column(String)
    my_numeric_field = Column(Integer)
    
  