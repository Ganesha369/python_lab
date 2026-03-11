# Automated-Multi-Currency-Expense-Ledger-API

[🚀 RUN LIVE](https://ganesha-dsa-hub.streamlit.app/?path=01-Python-Syntax/Automated-Multi-Currency-Expense-Ledger-API-Level-4/main.py) | [💡 REQUEST](https://github.com/Ganesha369/python_lab/issues/new)

### 🏢 Real-World
Real-world businesses operate across borders. A simple print statement isn't enough; they need persistent storage (JSON) and a way for different devices to access data simultaneously (FastAPI). This project demonstrates how to build a production-ready data pipeline using core Python syntax, file I/O, and modern web frameworks.

### 🛠️ Tech
Python 3.10+, FastAPI, Uvicorn (ASGI Server), JSON Library, Pydantic (Data Validation), Pathlib.

### 📘 Guide
1.  **Define the Data Schema:** Use Pydantic classes to define what an "Expense" looks like (ID, amount, currency, category).
2.  **JSON Persistence:** Create functions to read from and write to a `ledger.json` file. This ensures data isn't lost when the script stops.
3.  **Business Logic:** Implement Python syntax (list comprehensions and filters) to calculate totals and filter by category.
4.  **API Routing:** Use FastAPI decorators (`@app.post`, `@app.get`) to map URLs to your Python functions.
5.  **Execution:** Run the server using `uvicorn` and test the auto-generated documentation at `/docs`.