# The Digital Maze Runner: Exploring Graphs with DFS

Summary: Learn how to explore a digital world by going as deep as possible into one path before ever turning back—just like a professional explorer!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=23-Graphs-Depth-First-Search)

---

Hey there! I’m an engineer here at Microsoft. When we build apps like Xbox or Microsoft Teams, we often deal with huge webs of information called **Graphs**. Today, I’m going to teach you the most adventurous way to explore these webs: **Depth-First Search (DFS).**

### 1. Simple Definition: The Stack of Plates
Imagine you are exploring a dark cave with many tunnels. You have a **Stack of Plates** in your backpack. 
*   Every time you enter a new room, you put a plate on the stack with the room's name on it.
*   You keep moving forward into the next tunnel until you hit a dead end.
*   When you hit that dead end, you "Pop" the top plate off your stack and go back to the room written on the plate below it to see if there was another tunnel you missed.

**DFS is "Deep First."** We don't care about looking at all the nearby rooms first; we want to see how far down the rabbit hole we can go!

### 2. Real World: Why does Amazon care?
Think about **Amazon’s Recommendation Engine**. 
If you buy a Harry Potter book, Amazon wants to find related items. It might use DFS logic to say: "Harry Potter is linked to Wizards... Wizards are linked to Magic Wands... Wands are linked to Halloween Costumes." By going deep into one category, it can find specific niche items you might love!

### 3. The Tools
To build a DFS explorer, we need three main logic blocks:
1.  **The Adjacency List (The Map):** A dictionary that tells us which rooms (Nodes) are connected to which tunnels (Edges).
2.  **The Visited Set (The Breadcrumbs):** A list to keep track of where we’ve already been so we don't walk in circles forever.
3.  **Recursion (The Time Loop):** This is a coding trick where a function calls itself. It’s like the movie *Inception*—we go into a dream, inside a dream, inside a dream.

---

### 4. The Level Guide

*   **Level 0: The Graph.** You create a map. Room A leads to B and C. Room B leads to D.
*   **Level 1: The Start.** You pick a starting point (Node A).
*   **Level 2: The Dive.** You move to the first neighbor you see (Node B). You don't look at Node C yet!
*   **Level 3: The Dead End.** Once you hit a room with no new neighbors, you "backtrack."
*   **Level 4: The Finish.** You repeat this until every room on the map has been visited.

### 🐍 Full Code
