from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine

from app import settings



# Step1: Database Table schmema

class Todo(SQLModel):
    id: int | None = Field(default=None)
    title: str
# Step2 : connection to the data base
connection_string: str = str(settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL)

todo_server: FastAPI = FastAPI()

@todo_server.get("/")
def hello():
    return {"Hello": "World"}

@todo_server.get("/db")
def db_var():
    return {"DB": settings.DATABASE_URL, "Connection": connection_string }
