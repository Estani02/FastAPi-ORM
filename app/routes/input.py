from fastapi import APIRouter, HTTPException, Path
from config.db import conn
from config.db import conn
from schema.user import User
from model.user_connection import users

router = APIRouter()

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

@router.post('/input/{attribute}', response_model=dict)
def create_user_attribute(
    user: User,
    attribute: str = Path(..., title="Attribute Name", description="Nombre del atributo (field_1, author o description)")
):
    if attribute not in ("field_1", "author", "description"):
        raise HTTPException(status_code=400, detail=f"{attribute} no es un campo válido para convertir a mayúscula")

    return create_user_with_upper_field(user, attribute)