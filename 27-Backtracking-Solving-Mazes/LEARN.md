# The Magic Breadcrumb Hack: Solving Mazes with Backtracking

Summary: Learn how to teach a computer to explore a maze, hit a dead end, and "rewind" time to find the right path using the power of Backtracking.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=27-Backtracking-Solving-Mazes)

---

Hey there, Future Engineer! I'm an SDE-2 at Microsoft. In my day job, I build systems that handle millions of requests, but every complex system is built on simple logic—like solving a maze! Let’s dive in.

### 1. SIMPLE DEFINITION: The "Video Game Save Point"
Imagine you are playing a game like *Minecraft* or *Zelda*. You enter a dark cave with three different tunnels. You don't know which one leads to the treasure!

**Backtracking** is like having an infinite "Undo" button. 
1. You walk down Tunnel A. 
2. You hit a wall (Dead end). 
3. You **"Backtrack"** (Undo your steps) to the entrance.
4. You try Tunnel B.

It’s exactly like the story of Hansel and Gretel dropping breadcrumbs. If they get lost, they follow the crumbs back to the last place they were safe and try a different turn.

### 2. REAL WORLD: Who uses this?
*   **Google Maps:** When calculating a route, Google’s algorithm explores millions of "turns." If a road is closed or blocked, it "backtracks" and tries a different street.
*   **Amazon Warehouse Robots:** These robots need to find the shortest path to a shelf. If another robot is blocking an aisle, the robot backtracks to find a detour.

### 3. THE TOOLS: Your Engineering Toolkit
To solve a maze in Python, we use:
*   **A 2D Grid (Matrix):** Think of this as a piece of graph paper where `0` is a path and `1` is a wall.
*   **Recursion:** This is a function that calls itself. It’s like a Russian Nesting Doll; each move you make is a smaller version of the same "Solve the Maze" problem.
*   **Lists:** To keep track of where we’ve already walked so we don't walk in circles!

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: The Map
We represent our maze as a list of lists.
```python
maze = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 1, 0] # 0 is walk-able, 1 is a wall
]
```

#### Level 1: The Goal (Base Case)
Every backtracking algorithm needs to know when to stop.
*   *Are we at the exit?* If yes, MISSION ACCOMPLISHED!

#### Level 2: The Rules
We can only move if:
1. We are inside the maze boundaries.
2. We aren't hitting a wall (`1`).
3. We haven't been to this square before.

#### Level 3: The Exploration (The "Search")
We try moving in four directions: **Down, Right, Up, Left.** 
If we move Down and it works, we keep going!

#### Level 4: The Backtrack (The "Oops" moment)
If we try all four directions and none lead to the exit, we must "un-mark" our current spot (pick up our breadcrumb) and return `False`. This tells the previous step, "Hey, don't come this way, it's a dead end!"

### 🐍 Full Code
