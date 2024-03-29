create project in command line 
```
poetry new todo-server --name app
```
```
cd todo-server 
```

poetry add fastapi uvicorn

create folder in current envirement like app
create file main.py in app folder

from fastapi import FastAPI

todo_server: FastAPI = FastAPI()

@todo_server.get("/")
def hello():
    return {"Hello": "World"}

now run command check the api route is running 

poetry run uvicorn app.main:todo_server

create databade in noen postgress

database is todo_server

create env file and store connection string 

DATABASE_URL = "postgresql://Shafiqmuhammad:Txe6XCp4FIQc@ep-ancient-wildflower-403825.ap-southeast-1.aws.neon.tech/todo_server?sslmode=require"

now create file settings.py in app folder 

create structure for env in this file 

```
from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
```

import settings.py in main.py
and updated the main.py
```
from fastapi import FastAPI
from app import settings



todo_server: FastAPI = FastAPI()

@todo_server.get("/")
def hello():
    return {"Hello": "World"}

@todo_server.get("/db")
def db_var():
    return {"DB", settings.DATABASE_URL}
```
installation of sqlmodel
poetry add sqlmodel
poetry add "psycopg[binary]"