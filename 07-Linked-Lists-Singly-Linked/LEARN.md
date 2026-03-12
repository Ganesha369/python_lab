# The Digital Treasure Hunt: Master the Linked List 🏴‍☠️

Summary: A Linked List is like a scavenger hunt where each clue tells you where the next secret box is hidden.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=07-Linked-Lists-Singly-Linked)

---

Hey there! I’m a Software Engineer at Microsoft, and today we’re going to build one of the coolest structures in computer science. 

### 1. Simple Definition: The Scavenger Hunt 🗺️
Imagine you are on a **Treasure Hunt**. You have a piece of paper (a **Node**) that says:
1.  **The Data:** "There is a gold coin here!"
2.  **The Pointer:** "The next clue is hidden under the red park bench."

You don't know where the 10th clue is. You only know where the *current* clue is and where it *points* to next. In an **Array** (like a shelf of books), you can just grab the 5th book. In a **Linked List**, you have to start at the beginning (the **Head**) and follow the clues one by one!

### 2. Real World: How Big Tech Uses It 🚀
*   **Spotify/Music Apps:** Think of a "Play Next" queue. The current song knows which song comes right after it.
*   **Image Gallery:** When you swipe through photos on your phone, the app often uses a linked structure to know which photo is "Next."
*   **Undo Button:** In apps like Word or Photoshop, your actions are often linked together so you can go back step-by-step.

### 3. The Tools: Our Logic Blocks 🧱
*   **The Node:** This is our basic building block. It has two pockets: one for **Data** and one for a **Next** address.
*   **The Head:** This is the "Start" sign of our hunt. If we lose the Head, we lose the whole list!
*   **None/Null:** This is the "End" sign. It means there are no more clues left.

---

### 4. The Level-Up Guide 🎮

#### Level 0: Creating a Node
A Node is just a class. It’s a box with two slots.
```python
class Node:
    def __init__(self, data):
        self.data = data  # The treasure
        self.next = None  # The map to the next box
```

#### Level 1: Linking Them Up
To connect them, we just point the `next` of one box to the other box.
```python
box1 = Node("Gold")
box2 = Node("Silver")
box1.next = box2  # box1 now points to box2!
```

#### Level 2: Adding to the Front
Adding to the front is super fast. You just tell the new node to point to the current Head.
```python
new_node.next = self.head
self.head = new_node
```

#### Level 3: Traversing (Walking the Chain)
To find something, we use a `while` loop to hop from one node to the next until we hit `None`.

#### Level 4: Deleting a Node
To delete a node, we just tell the node *before* it to skip over it and point to the one *after* it. It’s like cutting a link in a chain and re-attaching the ends!

### 🐍 Full Code
