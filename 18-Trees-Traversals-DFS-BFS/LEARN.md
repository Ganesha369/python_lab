# The Great Digital Scavenger Hunt: Mastering DFS and BFS!

Summary: Learn how to navigate a "Tree" of data using two secret techniques that computers use to find everything from your friends on TikTok to the fastest route on Google Maps.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=18-Trees-Traversals-DFS-BFS)

---

Hey there, future engineer! I’m a Software Engineer at Microsoft. When we build apps like Xbox or Minecraft, we deal with massive amounts of data organized in "Trees." 

Imagine a **Tree** isn't something with leaves, but a family tree. You are at the top, and your kids and grandkids branch out below you. But how do we "search" this tree to find a specific person? We use two legendary methods: **DFS** and **BFS**.

### 1. The Simple Definition (Analogy)
Imagine you are exploring a multi-floor Mystery Mansion looking for a hidden diamond.

*   **DFS (Depth-First Search): The Brave Explorer.** 
    *   **Analogy:** You pick one hallway and run as deep as you can until you hit a dead end. Then you backtrack and try the next deep hallway.
    *   **Tool:** It uses a **Stack** (like a pile of Pringles—the last one you put in is the first one you eat).

*   **BFS (Breadth-First Search): The Scanning Drone.**
    *   **Analogy:** You stay on the ground floor and check every single room. Only after you’ve seen everything on Floor 1 do you move to Floor 2.
    *   **Tool:** It uses a **Queue** (like a line at the movies—the first person in line is the first one to get popcorn).

### 2. Real World: Why does Google/Amazon care?
*   **Google Maps (BFS):** When you want the *shortest* path to a pizza shop, Google uses BFS. It looks at all nearby streets first before looking at streets far away.
*   **Amazon Recommendations (DFS):** If you like "Star Wars," Amazon might go deep into a rabbit hole: *Star Wars -> Sci-Fi Movies -> Space Documentaries -> Astronaut Ice Cream.*

### 3. The Tools (Our Logic Blocks)
*   **Node:** A single "circle" in our tree containing data.
*   **Children:** The nodes directly below a node.
*   **Recursion:** When a function calls itself (like looking in a mirror that shows you looking in a mirror).
*   **Streamlit:** A cool tool we use to turn our Python code into a website instantly.

### 4. The Level 0 to Level 4 Guide

**Level 0: The Structure**
A tree starts with a "Root." Every node can have a Left child and a Right child.

**Level 1: DFS (Going Deep)**
We go: Root -> Left -> Left's Child... then back up to the Right.
*Code Logic:* `visit(node) -> visit(left) -> visit(right)`

**Level 2: BFS (Going Wide)**
We use a "To-Do List" (Queue). We visit a node, then add its children to the end of the list.
*Code Logic:* `Take first from list -> Add its kids to end -> Repeat.`

**Level 3: The Stack vs. Queue**
*   **DFS uses a Stack:** "Last In, First Out" (LIFO).
*   **BFS uses a Queue:** "First In, First Out" (FIFO).

**Level 4: Implementation**
In the code below, we’ll build a visualizer to see these "explorers" in action!

### 🐍 Full Code
