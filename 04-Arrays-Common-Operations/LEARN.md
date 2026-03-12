# Mastering the Digital Locker: The Secret Art of Array Operations

Summary: Learn how to manage a row of items by reading, swapping, adding, and finding things—exactly how your favorite apps handle your data!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=04-Arrays-Common-Operations)

---

Hey there! I'm an SDE-2 at Microsoft. In my day job, I help build features you might see in Windows or Xbox. Today, we’re talking about **Array Operations**.

### 1. SIMPLE DEFINITION: The School Locker Row
Imagine a long hallway of school lockers. Each locker has a number on it, starting from **0** (because programmers are weird and start counting at zero!). 

An **Array** is just that row of lockers. **Array Operations** are the things you do with them:
*   **Accessing:** Opening locker #3 to see what's inside.
*   **Updating:** Taking out a dirty gym bag and putting in a fresh one.
*   **Inserting/Deleting:** This is like magically sliding a new locker into the middle of the wall!
*   **Searching:** Walking down the hall looking for the locker that has the "Minecraft" sticker on it.

### 2. REAL WORLD: How the Giants Use It
*   **Amazon:** When you look at your "Shopping Cart," that's an array. When you click "Remove," Amazon performs a **Delete** operation on that array.
*   **Netflix:** Your "Continue Watching" list is an array. When you watch a new show, they **Insert** it at the very beginning (Index 0).

### 3. THE TOOLS
We are using **Python Lists** today. In Python, lists act like "Super Arrays."
*   `list[i]`: This is the **Index**. It’s the locker number.
*   `.append()`: Adds something to the very end.
*   `.insert(index, value)`: Squeezes an item into a specific spot.
*   `.pop(index)`: Removes the item at that spot.
*   `if item in list`: This is how we **Search**.

---

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: The Empty Array
First, we need a place to store our stuff.
```python
inventory = ["Sword", "Shield", "Potion"]
```

#### Level 1: Accessing (The "Peek")
To see what is in the first spot, we use `0`.
```python
item = inventory[0] # Result: "Sword"
```

#### Level 2: Updating (The "Swap")
If you find a better weapon, you replace the old one.
```python
inventory[0] = "Laser Gun" 
# Now inventory is ["Laser Gun", "Shield", "Potion"]
```

#### Level 3: Inserting & Deleting (The "Shuffle")
If you pick up a "Map" and want it in the second slot:
```python
inventory.insert(1, "Map") 
# Everything shifts right! ["Laser Gun", "Map", "Shield", "Potion"]
```
If you use the Potion, it's gone:
```python
inventory.pop(3) # Removes "Potion"
```

#### Level 4: Searching (The "Scan")
Need to find where the Map is?
```python
location = inventory.index("Map") # Result: 1
```

### 🐍 Full Code
