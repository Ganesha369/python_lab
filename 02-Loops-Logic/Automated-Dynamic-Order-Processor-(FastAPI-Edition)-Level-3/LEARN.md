# Automated-Dynamic-Order-Processor-(FastAPI-Edition)

[🚀 RUN LIVE](https://ganesha-dsa-hub.streamlit.app/?path=02-Loops-Logic/Automated-Dynamic-Order-Processor-(FastAPI-Edition)-Level-3/main.py) | [💡 REQUEST](https://github.com/Ganesha369/python_lab/issues/new)

### 🏢 Real-World
Real-world e-commerce platforms like Amazon or Shopify don't calculate totals manually. They use backend logic to loop through your "cart," check inventory levels, apply tiered discounts based on logic (e.g., "Buy 3, get 10% off"), and calculate taxes based on location—all in milliseconds.

### 🛠️ Tech
- **Python 3.10+**: Core language.
- **FastAPI**: To create the web interface.
- **Uvicorn**: The server to run the API.
- **Pydantic**: For data validation.
- **JSON**: To receive and send order data.

### 📘 Guide
1. **Define the Data**: We define what an "Order" looks like using Pydantic models.
2. **The Logic**: We will create a `POST` endpoint. When data is sent to it:
   - We use a **For Loop** to iterate through every item in the customer's cart.
   - We use **Nested Logic (If/Else)** to check if the item is in stock.
   - We use **Logic Operators** to determine if they qualify for a "Bulk Discount" (e.g., if quantity > 5).
3. **The Response**: We return a final JSON object containing the subtotal, the applied discounts, and the final price.
4. **Running it**: You will need to install requirements: `pip install fastapi uvicorn`.