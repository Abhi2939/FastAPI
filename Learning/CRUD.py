from fastapi import FastAPI,Path,Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : int
    brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[int] = None
    brand : Optional[str] = None

# @app.get("/")
# def home():
#     return {"Data":"Test"}

# @app.get("/about")
# def about():
#     return {"data":"about"}

invertory = {

    1:{
        "name":"milk",
        "price":3.99,
        "brand":"regular"
    }
}

# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id:int,name:str = None):
    
#     return invertory[item_id]

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None,description="The ID of the item ",gt=0,lt=2)):
    
    return invertory[item_id]


@app.get("/get-by-name/{item_id}")
def get_item(item_id: int,test: int,name:Optional[str] = None):
    
    for item_id in invertory:
        if invertory[item_id].name == name:
            return invertory[item_id]
        raise HTTPException(status_code=404,detail="Item ID not found")
    
@app.post("/create-item/{item_id}")
def create_item(item_id: int,item:Item):

    if item_id in invertory:
        raise HTTPException(status_code=400,detail="Item ID already exists")
    
    # invertory[item_id] = {
    #     "name":item.name,
    #     "brand":item.brand,
    #     "price":item.price
    # } 

    invertory[item_id] = item
    return invertory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    
    if item_id in invertory:
        raise HTTPException(status_code=404,detail="Item ID not found")
    
    if item.name != None:
        invertory[item_id].name = item.name

    if item.price != None:
        invertory[item_id].price = item.price

    if item.brand != None:
        invertory[item_id].brand = item.brand

    return invertory[item_id]

@app.delete("/delete-item/")
def delete_item(item_id: int = Query(...,description="ID of the item to be deleted")):

    if item_id not in invertory:
        raise HTTPException(status_code=404,detail="Item ID not found")
    
    del invertory[item_id]

    return {"Success":"Item deleted!"}