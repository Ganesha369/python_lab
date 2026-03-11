import json
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. DATA MODEL (Using Type Hinting)
class Expense(BaseModel):
    id: int
    description: str
    amount: float
    currency: str = "USD"
    category: str

# 2. FILE INITIALIZATION
DB_FILE = Path("ledger.json")
if not DB_FILE.exists():
    DB_FILE.write_text(json.dumps([]))

app = FastAPI(title="Global Expense Tracker")

# 3. HELPER FUNCTIONS (Core Logic)
def read_db() -> List[dict]:
    return json.loads(DB_FILE.read_text())

def write_db(data: List[dict]):
    DB_FILE.write_text(json.dumps(data, indent=4))

# 4. API ENDPOINTS
@app.get("/expenses")
def get_expenses(category: Optional[str] = None):
    """Retrieve all expenses, optionally filtered by category."""
    data = read_db()
    if category:
        # Using list comprehension (Level-2/3 Syntax)
        return [e for e in data if e['category'].lower() == category.lower()]
    return data

@app.post("/expenses/add")
def add_expense(item: Expense):
    """Add a new expense to the JSON ledger."""
    db = read_db()
    
    # Check if ID already exists
    if any(e['id'] == item.id for e in db):
        raise HTTPException(status_code=400, detail="ID already exists")
    
    db.append(item.dict())
    write_db(db)
    return {"message": "Expense recorded successfully", "data": item}

@app.get("/expenses/total")
def get_total(currency: str = "USD"):
    """Calculate total spending in a specific currency."""
    db = read_db()
    # Logic: Filter by currency and sum the amounts
    total = sum(e['amount'] for e in db if e['currency'].upper() == currency.upper())
    return {
        "currency": currency.upper(),
        "total_spent": round(total, 2),
        "transaction_count": len([e for e in db if e['currency'] == currency])
    }

# TO RUN THIS:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Save as main.py
# 3. Run: uvicorn main:app --reload
# 4. Visit http://127.0.0.1:8000/docs in your browser