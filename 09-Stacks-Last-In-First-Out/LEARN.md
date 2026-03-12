# The Pancake Power-Up: Mastering the Stack

Summary: 

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=09-Stacks-Last-In-First-Out)

---

Hey there! I'm an engineer at Microsoft, and today I’m going to show you one of the most important tools in our coding toolbox: **The Stack**. 

### 1. Simple Definition: The Pancake Rule
Imagine you are making a giant stack of chocolate chip pancakes. 
*   When you cook a new pancake, you place it on **top** of the pile. 
*   When you want to eat one, you take it off the **top**.

You wouldn't grab the pancake at the very bottom, right? (That would be a sticky mess!) This is called **LIFO**: **L**ast **I**n, **F**irst **O**ut. The last pancake you cooked is the first one you eat.

### 2. Real World: How Big Tech Uses Stacks
At **Microsoft** or **Google**, we use stacks everywhere:
*   **The "Undo" Button (Ctrl+Z):** Every time you type a word in Word or Google Docs, we "push" that action onto a stack. When you hit Undo, we "pop" the last action off the top to erase it.
*   **Browser History:** When you click the "Back" button in Chrome, you are popping the last website you visited off your history stack.

### 3. The Tools: Our Coding Blocks
To build a stack in Python, we use a simple **List**. Here are the magic commands:
*   `.append()`: This is our **Push**. It puts an item on top.
*   `.pop()`: This is our **Pop**. It removes the top item.
*   `[-1]`: This is our **Peek**. It lets us look at the top item without removing it.
*   `len()`: This tells us the **Size** (how many items are in our stack).

---

### 4. The Lesson: Level 0 to Level 4

#### Level 0: The Empty Plate
Every stack starts empty.
```python
pancake_stack = []
```

#### Level 1: Pushing (Adding)
Let's add some flavors!
```python
pancake_stack.append("Blueberry")
pancake_stack.append("Chocolate Chip")
# The stack is now: ["Blueberry", "Chocolate Chip"]
```

#### Level 2: Popping (Eating)
Time to eat the top one.
```python
top_pancake = pancake_stack.pop()
print(f"I just ate the {top_pancake} pancake!")
# Only "Blueberry" is left.
```

#### Level 3: Peeking (Checking)
What's next on the menu?
```python
next_one = pancake_stack[-1]
print(f"The next one is {next_one}, but I'm saving it for later.")
```

#### Level 4: The Pro Check
In the real world, we always check if the stack is empty before popping, or the program will crash!
```python
if len(pancake_stack) > 0:
    pancake_stack.pop()
else:
    print("No more pancakes left!")
```

### 🐍 Full Code
