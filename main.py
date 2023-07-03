from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

# Data classes

class FormRegister(BaseModel):
    username:str
    mdp:str

    
# App

app = FastAPI()

# Endpoints

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/register")
def register(new_user: FormRegister):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO user VALUES(NULL, ?, ?);
        """,
        (new_user.username, new_user.mdp)
    )
    connection.commit()
    connection.close()
    return {"Status: ": "Done!"}

@app.get("/users")
def get_users():
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name FROM user;
        """
    )
    resultat = cursor.fetchall()
    connection.close()
    return {"user_names:" : resultat}
