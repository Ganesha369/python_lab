# The Ultimate GPS: Finding the Secret Shortcut with Dijkstra!

Summary: Learn how to find the fastest route through a maze of paths using the same logic Google Maps uses to get you to school on time.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=24-Graphs-Shortest-Path-Dijkstra)

---

Hey there! I'm an engineer at Microsoft, and today I’m going to show you one of the most famous "Cheat Codes" in computer science: **Dijkstra’s Algorithm.** 

### 1. SIMPLE DEFINITION: The "Breadcrumb Scout"
Imagine you are a scout in a video game map with different kingdoms. Between kingdoms, there are roads. Some roads are paved (fast), and some are muddy (slow). 

**Dijkstra’s Algorithm** is like sending out a team of magical scouts from your starting castle. Each scout moves at the same speed. The first scout to reach a new kingdom tells you the fastest way to get there. By always focusing on the scout who has traveled the *least* amount of time so far, you eventually find the shortest path to every single kingdom on the map!

### 2. REAL WORLD: Who uses this?
*   **Google Maps:** When you type in a destination, Google treats every intersection as a "node" and every street as an "edge." The traffic levels are the "weights" (costs). Dijkstra helps find the route with the lowest "cost" (time).
*   **Amazon:** To get a package from a warehouse to your door, Amazon’s computers calculate the shortest path through shipping hubs to save on gas and time.

### 3. THE TOOLS (The SDE Toolkit)
To build this, we use three main logic blocks:
1.  **The Graph (Adjacency List):** A dictionary where we store "If I am at City A, I can go to City B (5 mins) or City C (10 mins)."
2.  **The Priority Queue (The VIP Line):** This is a special list that always keeps the smallest number at the very top. In Python, we use `heapq`. It ensures we always work on the shortest path we've found so far.
3.  **Distance Table:** A notebook where we write down the shortest time it takes to get to every city. We start by setting everyone to "Infinity" because we haven't visited them yet!

---

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: The Setup
We represent our map as a dictionary.
```python
graph = {
    'Home': [('School', 5), ('Park', 2)],
    'Park': [('School', 2), ('Store', 6)],
    'School': [('Store', 1)],
    'Store': []
}
```

#### Level 1: The VIP Line (Priority Queue)
We put our starting point in the queue with a distance of 0. 
`[(0, 'Home')]`

#### Level 2: Exploring
We take the "cheapest" item out. 
"Okay, I'm at **Home**. I can go to **Park** in 2 mins." 
We update the Park's time to 2.

#### Level 3: The "Wait, I found a shortcut!" (Relaxation)
If we find a way to get to the **School** through the **Park** that is faster than the direct road from **Home**, we update our notebook. This is called "Relaxation."

#### Level 4: The Final Map
Once the VIP line is empty, our notebook has the absolute shortest time to every single location!

### 🐍 Full Code
