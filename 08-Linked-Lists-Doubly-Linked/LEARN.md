# The Two-Way Train: Mastering Doubly Linked Lists

Summary: A special type of data chain where every "car" knows exactly who is in front of them AND who is behind them, making it easy to move in both directions!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=08-Linked-Lists-Doubly-Linked)

---

Hey there, Future Engineer! I'm an SDE-2 here at Microsoft. When we build apps like Microsoft Word or Windows, we need data to move fast. Today, we are upgrading from a normal Linked List to the **Doubly Linked List**.

### 1. The Fun Analogy: The "Super-Connected" Train
Imagine a train. In a **Singly Linked List**, each car only has a hook on the back. If you are in Car #3, you know who is in Car #4, but you have no idea who is in Car #2! You'd have to run all the way back to the start of the train to find out.

In a **Doubly Linked List**, every car has a hook on the **Front** AND the **Back**. 
*   If you're in Car #3, you can peek forward to Car #4.
*   But you can also peek backward to Car #2.
*   This makes you a "Two-Way Explorer!"

### 2. Real World: How Big Tech Uses This
*   **Google Chrome / Microsoft Edge:** Your browser history uses this! When you click the **"Back"** button, the browser uses the `prev` pointer. When you click **"Forward"**, it uses the `next` pointer.
*   **Spotify:** When you are in a playlist, you need to be able to hit "Next Song" and "Previous Song." A Doubly Linked List is the perfect way to store that queue.

### 3. The Tools: Our Building Blocks
*   **The Node:** This is our "Train Car." It has three parts: `Data` (the cargo), `Next` (the link ahead), and `Prev` (the link behind).
*   **The Head:** The very first car.
*   **The Tail:** The very last car (Doubly Linked Lists love having a tail, it makes adding to the end super fast!).
*   **Pointers:** These are just variables that "point" or "refer" to another object in memory.

### 4. Level 0 to Level 4 Guide

**Level 0: The Blueprint**
We create a class called `Node`. Unlike before, we add `self.prev = None`.

**Level 1: The Handshake**
When we connect Node A to Node B, we must do two things:
1.  A's `next` points to B.
2.  B's `prev` points to A. 
It’s like a firm two-handed handshake!

**Level 2: Adding to the Front (The Head)**
To add a new car at the start, we tell the new car's `next` to point to the current Head, and the current Head's `prev` to point to the new car.

**Level 3: Adding to the Back (The Tail)**
Because we have a `tail` pointer, we don't have to walk through the whole list! we just tell the current Tail: "Hey, your `next` is this new guy," and the new guy's `prev` is you.

**Level 4: Deleting**
To remove a node in the middle, we just tell the nodes on either side to "skip" the middle guy and point directly to each other. It’s like the middle car vanished, and the two surrounding cars hooked their chains together!

### 🐍 Full Code
