from fastapi import FastAPI
from app.routes import data, input

app = FastAPI()


app.include_router(data.router)
app.include_router(input.router)