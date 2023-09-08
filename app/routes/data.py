from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from config.db import conn, SessionLocal
from model.user_connection import users

router = APIRouter()

# /data
@router.get('/data')
def get_users():
  all_users = conn.execute(users.select()).fetchall()
  items = []
  for data in all_users:
    dictionary = {}
    dictionary['id'] = data[0]
    dictionary['field_1'] = data[1]
    dictionary['description'] = data[2]
    dictionary['my_numeric_field'] = data[3]
    items.append(dictionary)
  return items

@router.get('/data/{id}')
def get_user(id: int):
    with SessionLocal() as session:
        result_row = session.execute(select(users).where(users.c.id == id)).first()
    
    if result_row:
        result_dict = {
        "id": result_row[0],
        "field_1": result_row[1],
        "author": result_row[2],
        "description": result_row[3],
        "my_numeric_field": result_row[4]
        }
        return result_dict
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")