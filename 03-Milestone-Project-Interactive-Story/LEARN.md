# Cyber-Rescue: A Terminal Adventure

### Level 0: The Interface (I/O)
Every application starts with getting data from the user and displaying results. In Python, we use `input()` and `print()`.
**SDE Tip:** Use *f-strings* for readable string formatting.

```python
name = input("Enter your hacker alias: ")
print(f"Welcome to the mainframe, {name}. Your mission begins now.")
```

### Level 1: Branching Logic (Decisions)
A story isn't interactive without choices. We use `if`, `elif`, and `else` to create different paths.
**SDE Tip:** Always handle the "Else" case to catch unexpected inputs.

```python
choice = input("Do you go [LEFT] to the server room or [RIGHT] to the office? ").upper()

if choice == "LEFT":
    print("you encounter a firewall!")
elif choice == "RIGHT":
    print("You find a hidden keycard.")
else:
    print("Invalid choice. The guards spotted you.")
```

### Level 2: Input Validation (Loops)
Users make mistakes. If you ask for "A" or "B" and they type "C", your code shouldn't just break or quit. We use `while` loops to keep asking until we get a valid response.

```python
while True:
    action = input("Type 'RUN' or 'HIDE': ").upper()
    if action in ["RUN", "HIDE"]:
        break # Exit loop if input is valid
    print("Command not recognized. Try again.")
```

### Level 3: Modularity (Functions)
In production, we never write one giant block of code (spaghetti code). We break things into **functions**. Each function should do one thing well.

```python
def start_scene():
    print("You are at the entrance.")
    # Logic for scene 1

def forest_scene():
    print("You are in a dark forest.")
    # Logic for scene 2
```

### Level 4: State Management (Dictionaries)
To make a game feel "real," the world needs to remember what you did. We use a dictionary to track the "Game State" (like your inventory).

```python
# The 'State' of our application
player_stats = {
    "has_key": False,
    "health": 100
}

if player_stats["has_key"]:
    print("The door unlocks!")
```