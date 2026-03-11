from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Simulated Inventory Database
INVENTORY = {
    "laptop": {"price": 1000, "stock": 5},
    "mouse": {"price": 25, "stock": 50},
    "keyboard": {"price": 75, "stock": 20}
}

# Data Models (Schema)
class OrderItem(BaseModel):
    item_name: str
    quantity: int

class OrderRequest(BaseModel):
    customer_name: str
    cart: List[OrderItem]

@app.post("/process-order/")
async def process_order(order: OrderRequest):
    total_price = 0.0
    processed_items = []
    applied_discounts = 0.0

    # LOGIC START: Loop through the JSON cart
    for cart_item in order.cart:
        name = cart_item.item_name.lower()
        qty = cart_item.quantity

        # Logic: Check if item exists in our inventory
        if name not in INVENTORY:
            raise HTTPException(status_code=404, detail=f"Item {name} not found.")

        # Logic: Check stock availability
        item_data = INVENTORY[name]
        if qty > item_data["stock"]:
            raise HTTPException(status_code=400, detail=f"Not enough stock for {name}.")

        # Logic: Calculate price and apply tiered discounts
        # If buying more than 5 of an item, get 10% off that item
        item_total = item_data["price"] * qty
        if qty >= 5:
            discount = item_total * 0.10
            item_total -= discount
            applied_discounts += discount

        total_price += item_total
        processed_items.append({"item": name, "final_item_price": item_total})

    # Final logic: Apply a global 'Big Spender' discount
    if total_price > 2000:
        total_price *= 0.95  # Extra 5% off the whole order
        applied_discounts += (total_price / 0.95) * 0.05

    return {
        "customer": order.customer_name,
        "items_processed": processed_items,
        "total_savings": round(applied_discounts, 2),
        "final_total": round(total_price, 2),
        "status": "Success"
    }

# TO RUN THIS:
# 1. Save as main.py
# 2. Run: uvicorn main:app --reload
# 3. Go to http://127.0.0.1:8000/docs to test the API with JSON input.