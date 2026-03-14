# Sorting Superpowers: Building X-Ray Goggles for Code

Summary: We are going to build a tool that slows down time so you can watch a computer's "brain" organize a messy pile of numbers into a perfect line!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=30-Final-Capstone-The-Algorithm-Visualizer)

---

Hi there! I’m an SDE-2 at Microsoft. In my day job, I work on big systems, but every big system is just a collection of small, smart "recipes" called **Algorithms**. Today, you’re graduating! We’re building an **Algorithm Visualizer**.

### 1. SIMPLE DEFINITION: The Messy Bookshelf
Imagine you have a bookshelf with 10 books of different heights, all mixed up. You want them sorted from shortest to tallest. 
*   **The Algorithm:** This is the set of steps you take to move the books.
*   **The Visualizer:** This is like filming yourself in **slow motion** so you can see every single time you swap two books.

### 2. REAL WORLD: Why does big tech care?
At **Amazon**, when you search for "Video Games" and click "Sort by Price: Low to High," an algorithm exactly like the one we're building kicks into gear. If that algorithm is slow, Amazon loses millions of dollars because people get bored and leave! At **Microsoft**, we use sorting to organize your files, your emails, and even the players in an Xbox party.

### 3. THE TOOLS: Our Utility Belt
*   **Streamlit:** This is our "Magic Wand." It turns boring Python code into a cool website with buttons and sliders.
*   **Time Library:** Computers are too fast! We use `time.sleep()` to force the computer to pause for a micro-second so our human eyes can keep up.
*   **Matplotlib:** This is our "Canvas." It draws the bars that represent our numbers.
*   **Random:** To create a "messy" list of numbers for us to fix.

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: The "Mess"
Before we sort, we need a list of numbers.
```python
# A random list of heights
data = [50, 10, 40, 30, 20]
```

#### Level 1: The "Swap" Logic
To sort, we have to swap two numbers. Imagine you have a **Red Apple** in your left hand and a **Green Apple** in your right. To swap them, you need a **Table** (a temporary variable) to set one down for a second!
```python
temp = data[0]
data[0] = data[1]
data[1] = temp
```

#### Level 2: The "Bubble Sort" (Our Recipe)
We compare two neighbors. If the left one is bigger than the right one, they swap places. The biggest number "bubbles" up to the end of the list like a bubble in a soda!

#### Level 3: The Animation
Every time we swap, we tell Streamlit to "re-draw" the bars. This creates the movie effect.

#### Level 4: The Speed Control
We add a slider so the user can decide if the "brain" should think fast or slow.

### 🐍 Full Code
