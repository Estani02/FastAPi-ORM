from pydantic import BaseModel
from model import DataModel
from db import SessionLocal
from fastapi import HTTPException

# Modelo para la solicitud POST
class InputData(BaseModel):
    ID: int 
    field_1: str
    author: str
    description: str
    my_numeric_field: int
    
    
def create_data(my_target_field: str, data: InputData):
    allowed_fields = ["field_1", "author", "description"]

    if my_target_field not in allowed_fields:
        raise HTTPException(status_code=400, detail=f"{my_target_field} no es un campo válido para convertir a mayúscula")

    setattr(data, my_target_field, getattr(data, my_target_field).upper())

    db = SessionLocal()
    db_data = DataModel(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    db.close()

    return {"id": db_data.id}
  
def read_data(id: int):
    db = SessionLocal()
    data = db.query(DataModel).filter(DataModel.id == id).first()
    db.close()
    if data is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    format_data = {
          "ID": data.id,
          "field_1": data.field_1,
          "author": data.author,
          "description": data.description,
          "my_numeric_field": data.my_numeric_field
    }
    return format_data
  
def read_all_data(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    data = db.query(DataModel).offset(skip).limit(limit).all()
    db.close()
    formatted_data = [
        {
            "ID": item.id,
            "field_1": item.field_1,
            "author": item.author,
            "description": item.description,
            "my_numeric_field": item.my_numeric_field
        }
        for item in data
    ]
    
    return formatted_data