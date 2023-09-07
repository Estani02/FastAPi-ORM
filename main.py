from fastapi import FastAPI, HTTPException, Path
from config.db import SessionLocal, conn
from model.user_connection import users
from schema.user import User
from sqlalchemy import select

app = FastAPI()

# /data
@app.get('/data')
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

@app.get('/data/{id}')
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
  
def create_user_with_upper_field(user: User, field_name: str):
    new_user = {
        "field_1": user.field_1,
        "author": user.author,
        "description": user.description,
        "my_numeric_field": user.my_numeric_field
    }
    new_user[field_name] = getattr(user, field_name).upper()

    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    inserted_id = result.inserted_primary_key[0]
    return {"id": inserted_id}

@app.post('/input/{attribute}', response_model=dict)
def create_user_attribute(
    user: User,
    attribute: str = Path(..., title="Attribute Name", description="Nombre del atributo (field_1, author o description)")
):
    if attribute not in ("field_1", "author", "description"):
        raise HTTPException(status_code=400, detail=f"{attribute} no es un campo válido para convertir a mayúscula")

    return create_user_with_upper_field(user, attribute)

