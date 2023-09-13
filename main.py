from fastapi import FastAPI
from service import read_all_data, read_data, create_data, InputData, GetData

app = FastAPI()

@app.get('/')
def welcome():
    return 'Api desarrollada por Estanislao Olmedo! :)'

@app.get('/get_data')
def get_users(skip: int = 0, limit: int = 100):
    return read_all_data(skip, limit)

@app.get("/get_data/{id}", response_model=GetData)
def get_user(id: int):
    return read_data(id)
  
@app.post("/input/{my_target_field}")
def uppercase_user(my_target_field: str, data: InputData):
    return create_data(my_target_field, data)