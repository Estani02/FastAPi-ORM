from decouple import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine(config("DATABASE_URL"))

meta = MetaData()

conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conn)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()