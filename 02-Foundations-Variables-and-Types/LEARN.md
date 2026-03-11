# Project: The Hero’s Inventory System

### Level 0: The Assignment Operator
In Python, we use the `=` sign to "assign" a value to a name. It’s not a mathematical "equals"; it’s an instruction to store something.

```python
# Level 0: Storing a simple value
hero_name = "Master Chief"
print(hero_name)
```

### Level 1: Numbers (Integers and Floats)
We deal with two main types of numbers:
1.  **Integers (`int`)**: Whole numbers. No decimals.
2.  **Floats (`float`)**: Decimal numbers (Floating point).

```python
# Level 1: Tracking stats
health_points = 100          # This is an 'int'
accuracy_rating = 98.5       # This is a 'float'
print(health_points, accuracy_rating)
```

### Level 2: Text and Logic (Strings and Booleans)
Programs need to talk to users and make decisions.
1.  **Strings (`str`)**: Text wrapped in quotes.
2.  **Booleans (`bool`)**: Either `True` or `False`. In the industry, we use these for "flags."

```python
# Level 2: Identity and Status
motto = "Finish the fight."  # This is a 'str'
is_mission_active = True     # This is a 'bool'
print(motto, is_mission_active)
```

### Level 3: Dynamic Typing & Naming Conventions
At Microsoft, we follow `snake_case` for variables (all lowercase, underscores between words). Also, Python is **dynamically typed**, meaning a variable can change its type on the fly—though you should be careful with this!

```python
# Level 3: Changing types (Dynamic Typing)
ammo_count = "Five"   # Currently a string
ammo_count = 5        # Now it's an integer! Python doesn't mind.
print(ammo_count)
```

### Level 4: Introspection (type and id)
To write professional-grade code, you need to know what's happening under the hood. The `type()` function tells you the category, and `id()` tells you the exact memory address.

```python
# Level 4: Looking under the hood
experience_points = 5000
print(type(experience_points)) # Output: <class 'int'>
print(id(experience_points))   # The memory address in your RAM!
```