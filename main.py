# main.py
from fastapi import FastAPI, HTTPException
from database import read_data, write_data
from models import Item
from typing import List

app = FastAPI()

data_file = "data.json"

@app.get("/items", response_model=List[Item])
def get_items():
    return read_data(data_file)

@app.post("/items", response_model=Item)
def create_item(item: Item):
    data = read_data(data_file)
    data.append(item.dict())
    write_data(data_file, data)
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    data = read_data(data_file)
    new_data = [item for item in data if item["id"] != item_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Item not found")
    write_data(data_file, new_data)
    return {"message": "Item deleted"}
