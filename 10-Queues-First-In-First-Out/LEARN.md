# The Supermarket Secret: Master of the Queue! 🛒

Summary: Learn how to organize data like a pro by building a "First-Come, First-Served" system used by the world's biggest tech companies.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=10-Queues-First-In-First-Out)

---

Hey there, future engineer! I’m a Software Dev at Microsoft, and today I’m going to show you one of the most important tools in our toolkit: **The Queue.**

### 1. The Simple Definition: The Ice Cream Truck 🍦
Imagine you are standing in front of an ice cream truck. 
*   The first person who gets in line is the **first** one to get a chocolate cone and leave.
*   New people join the **back** of the line.
*   This is called **FIFO**: **F**irst **I**n, **F**irst **O**ut.

*Compare this to a Stack (like a pile of plates), where the last one you put on top is the first one you take off. A Queue is much fairer!*

### 2. Real World: How Amazon Uses Queues 📦
When you click "Buy Now" on Amazon, your order doesn't just instantly vanish. Amazon gets millions of orders a second! They use a **Message Queue**. 
1.  Your order joins a massive digital line.
2.  The "Packing Robots" look at the front of the line.
3.  They grab the oldest order first, pack it, and move to the next.
This ensures nobody who ordered a Nintendo Switch today has to wait behind someone who orders one tomorrow!

### 3. The Tools: Our Power-Ups 🛠️
To build this in Python, we use a special tool called `deque` (pronounced "deck") from a library called `collections`.
*   **`deque`**: Short for "Double-Ended Queue." It’s a super-fast list that is optimized for adding and removing things from the ends.
*   **`.append()`**: This is how we "Enqueue" (add someone to the back of the line).
*   **`.popleft()`**: This is how we "Dequeue" (take the person from the very front of the line).

---

### 4. The 0 to 4 Guide 🚀

**Level 0: The Rule**
Remember FIFO. First person in = First person served.

**Level 1: Enqueue (The Entrance)**
We add data to the "Tail" or "Back." 
`line.append("Alice")`

**Level 2: Dequeue (The Exit)**
We remove data from the "Head" or "Front."
`line.popleft()`

**Level 3: Peek (The Looker)**
Sometimes you just want to see who is next without making them leave the line. We just look at index `[0]`.

**Level 4: The Empty Check**
Before serving someone, we must check if the line is empty. If we try to remove someone from an empty line, our code will "crash" (error out!).

Ready to see it in action? Let's build a Pizza Shop Simulator!

### 🐍 Full Code
