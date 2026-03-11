import json
import os
from fastapi import FastAPI
from pydantic import BaseModel

# 1. SETUP & DATA STRUCTURE
app = FastAPI()
DB_FILE = "inventory.json"

# This class defines what an 'Item' looks like (Type Hinting)
class Item(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

# 2. JSON UTILITY FUNCTIONS
def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# 3. API ROUTES (The Interface)
@app.get("/")
def root():
    return {"message": "Welcome to the Inventory API. Go to /items to see data."}

@app.get("/items")
def get_items():
    """Retrieve all items from the JSON file."""
    return load_data()

@app.post("/items")
def add_item(item: Item):
    """Add a new item and save it to the JSON file."""
    inventory = load_data()
    
    # Convert the Pydantic model to a standard Python dictionary
    new_item_dict = item.dict()
    inventory.append(new_item_dict)
    
    save_data(inventory)
    return {"message": "Item added successfully", "item": new_item_dict}

# 4. HOW TO RUN
if __name__ == "__main__":
    import uvicorn
    print("Starting Server...")
    print("View the interactive documentation at: http://127.0.0.1:8000/docs")
    # Run the app using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)