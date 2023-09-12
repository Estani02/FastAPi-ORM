from decouple import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Añade ?sslmode=require a la URL de conexión
engine = create_engine('postgresql://estani:mplfypreha0O0h8ohKfAV3FVQ4VhyoGW@dpg-ck08fnb6fquc73d2f7sg-a/uppercase_convert')

meta = MetaData()

conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conn)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
