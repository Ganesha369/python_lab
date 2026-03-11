# Coding Speedrun: Is Your Code a Ninja or a Turtle?

Summary: Learn how to measure the "speed" and "memory" of your code using Big O notation, so your apps don't crash when millions of people use them.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=02-Basics-Time-and-Space-Complexity)

---

Hey there! I'm an SDE at Microsoft. When we build things like Minecraft or Xbox Live, we don't just care if the code *works*—we care how **efficient** it is. If a game takes 10 minutes to load a map, nobody will play it!

### 1. SIMPLE DEFINITION: The "Library Search" Analogy
Imagine you are looking for a specific book in a library:

*   **Time Complexity (Speed):** This is how many "steps" you take to find the book. If the books are scattered on the floor, you have to check every single one (Slow). If they are alphabetized, you can jump straight to the right shelf (Fast!).
*   **Space Complexity (Memory):** This is how many "extra carts" you need to help you search. If you have to copy the title of every book onto a new piece of paper to find the right one, you’re using a lot of "space."

In the coding world, we call this **Big O Notation**.

### 2. REAL WORLD: How Google Uses This
When you search for "Funny Cat Videos" on Google, there are **trillions** of web pages. 
*   If Google used a "Slow Turtle" algorithm ($O(n)$), it would take years to show you the results.
*   Instead, they use "Super Ninja" algorithms ($O(\log n)$) that find your video in less than a second. Big companies care about this because **Time = Money** and **Space = Battery/Hardware cost**.

### 3. THE TOOLS: Our Logic Blocks
*   **Python:** Our language of choice. It's like the LEGO bricks we use to build.
*   **Streamlit:** A cool library that turns our Python code into a website instantly.
*   **Time Library:** Used to measure exactly how many milliseconds our "Ninja" or "Turtle" takes.
*   **Lists `[]`:** Our "storage bins" for data.

---

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: $O(1)$ - The Instant Teleport (Constant Time)
No matter how many items you have, it always takes 1 step. 
*Example:* Grabbing the very first book from a pile. It doesn't matter if the pile has 10 books or 10 million; you just grab the top one!
```python
def fast_teleport(my_list):
    return my_list[0] # One step!
```

#### Level 1: $O(n)$ - The Long Walk (Linear Time)
If you have 10 items, it takes 10 steps. If you have a million, it takes a million steps.
*Example:* Checking every single locker in school to find your jacket.
```python
def long_walk(my_list):
    for item in my_list:
        print(item) # Steps increase with list size
```

#### Level 2: $O(n^2)$ - The Double Loop (Quadratic Time)
This is getting slow! For every item, you look at every other item.
*Example:* Every student in a class of 30 shaking hands with every other student. (That's 900 handshakes!)
```python
def slow_handshake(my_list):
    for x in my_list:
        for y in my_list:
            print(x, y) # Very slow as list grows!
```

#### Level 3: Space Complexity - The "Note-Taker"
If your code creates a **copy** of the data to process it, it uses $O(n)$ Space. If it does the work without making copies, it's $O(1)$ Space. At Microsoft, we try to save space so your phone's battery lasts longer!

#### Level 4: The Trade-off
Sometimes, we make code use more **Space** (Memory) so that it runs with faster **Time** (Speed). It’s like buying a bigger desk so you can spread your homework out and finish it faster!

### 🐍 Full Code
