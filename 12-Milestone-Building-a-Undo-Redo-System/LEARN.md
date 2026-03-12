# The Digital Time Machine: Mastering Undo & Redo

Summary: Learn how to build a system that lets users travel back in time to fix mistakes, just like your favorite text editor!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=12-Milestone-Building-a-Undo-Redo-System)

---

Hey there, future engineer! I’m an SDE-2 at Microsoft. In the professional world, we don't just write code; we build "safety nets." One of the most important safety nets is the **Undo/Redo system**. 

### 1. Simple Definition: The Pile of Plates
Imagine you are helpfully stacking plates in the kitchen. 
*   **The Undo Stack:** Every time you wash a plate, you put it on top of the pile. If you realize the last plate is still dirty, you "Undo" by taking the **top** plate off. 
*   **The Redo Stack:** Instead of throwing that plate away, you put it on a *different* pile (the Redo pile). If you change your mind and want it back, you take it from the top of the Redo pile and put it back on the main stack.

In coding, we call this a **Stack**, and the rule is **LIFO** (Last In, First Out). The last thing you did is the first thing you undo!

### 2. Real World: Why do Google and Amazon care?
*   **Google Docs:** Every letter you type is tracked. If you accidentally delete a whole paragraph, Google uses an "Undo Stack" to restore your work instantly.
*   **Amazon:** When designers are building layouts for the Amazon homepage, they use "State Management." If they move a "Buy Now" button and it looks ugly, they need to "Undo" that UI change immediately without refreshing the whole site.

### 3. The Tools
To build this in Python, we use:
*   **Lists `[]`:** These are our "Stacks." We use `.append()` to add a plate and `.pop()` to take the top one off.
*   **Streamlit Session State:** Streamlit is like a TV that refreshes every second. `session_state` is the "memory" that keeps our stacks from disappearing when the screen refreshes.

---

### 4. The Level-Up Guide

**Level 0: The Action**
When you type "Hello", we save that "state" into our Undo Stack. 

**Level 1: The Undo**
When you hit Undo, we "Pop" the last item from the Undo Stack and move it to the Redo Stack.

**Level 2: The Redo**
When you hit Redo, we "Pop" from the Redo Stack and push it back to the Undo Stack.

**Level 3: The "New Action" Rule**
*Crucial Rule:* If you Undo something, but then **type something new**, the Redo stack must be cleared! You've started a new timeline, and the old "future" no longer exists.

**Level 4: The Professional Implementation**
We wrap all this in a clean UI so the user only sees their text and two buttons.

### 🐍 Full Code
