
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})