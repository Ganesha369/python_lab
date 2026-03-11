# Project: The Digital Business Card

### Level 0: The Entry Point (`print`)
In Python, the `print()` function is our primary way to see what's happening inside the "black box" of the CPU. Unlike C++ or Java, Python doesn't need a `main` function or semicolons. 

```python
# Level 0: Simplest output
print("System Initialized.")
```

### Level 1: Variables and Data Types
At Microsoft, we don't just hardcode strings; we store them in variables. Python is **dynamically typed**, meaning you don't have to tell it that a variable is a "string" or an "integer"—it figures it out.

```python
# Level 1: Variables
username = "SDE_Intern"  # This is a String
access_level = 1         # This is an Integer
print(username)
```

### Level 2: Modern Formatting (F-Strings)
In the old days, we used `%` or `.format()`. Today, we use **F-Strings** (Formatted Strings). They are faster and much easier to read. This is the industry standard for production code.

```python
# Level 2: F-Strings
alias = "MasterChief"
id_number = 117
print(f"User: {alias} | ID: {id_number}")
```

### Level 3: Clean Code & Comments
Code is read much more often than it is written. We use `#` for single-line comments. A good SDE uses comments to explain *why* something is happening, not *what* is happening.

```python
# Level 3: Meaningful documentation
# We define the version here to track legacy support
VERSION = "v1.0.4"
print(f"Software Version: {VERSION}")
```

### Level 4: Special Characters & Multi-line Output
Sometimes you need to format your output with tabs (`\t`) or new lines (`\n`). If you have a massive block of text, we use triple quotes `"""`.

```python
# Level 4: Advanced Formatting
print("Status Check:\n\t- Memory: OK\n\t- CPU: OK")

banner = """
-----------------------
  MICROSOFT TERMINAL
-----------------------
"""
print(banner)
```