import streamlit as st
import time

# --- LOGIC: The Doubly Linked List Classes ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_last(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None

# --- STREAMLIT UI ---

st.set_page_config(page_title="DLL Visualizer", layout="wide")
st.title("🚂 The Doubly Linked List Train")
st.write("Welcome to the Microsoft Dev Lab! Let's build a two-way train.")

# Initialize the list in session state so it stays between clicks
if 'dll' not in st.session_state:
    st.session_state.dll = DoublyLinkedList()
    # Start with some data
    st.session_state.dll.add_to_end("Engine")
    st.session_state.dll.add_to_end("Cargo")

# Sidebar Controls
st.sidebar.header("Train Controls")
new_val = st.sidebar.text_input("Car Name", "Passenger Car")
if st.sidebar.button("Add Car to End ➕"):
    st.session_state.dll.add_to_end(new_val)
    st.rerun()

if st.sidebar.button("Remove Last Car ❌"):
    st.session_state.dll.remove_last()
    st.rerun()

# --- VISUALIZATION ---

def draw_train():
    nodes = []
    current = st.session_state.dll.head
    while current:
        nodes.append(current)
        current = current.next

    if not nodes:
        st.warning("The train tracks are empty! Add a car.")
        return

    cols = st.columns(len(nodes) * 2 - 1)
    
    for i in range(len(nodes)):
        # Draw the Node
        with cols[i*2]:
            st.info(f"**{nodes[i].data}**")
            # Show the pointers in small text
            prev_val = nodes[i].prev.data if nodes[i].prev else "None"
            next_val = nodes[i].next.data if nodes[i].next else "None"
            st.caption(f"⬅️ {prev_val}")
            st.caption(f"➡️ {next_val}")
        
        # Draw the Double Connection (Arrows)
        if i < len(nodes) - 1:
            with cols[i*2 + 1]:
                st.write(" <===> ")

draw_train()

# --- EXPLANATION BLOCK ---
st.divider()
st.subheader("What's happening under the hood?")
st.write("""
- **The Blue Boxes:** These are our `Nodes`. 
- **The Arrows (<===>):** This represents the `next` and `prev` pointers. 
- **Notice the Ends:** The first car's `prev` is always `None`, and the last car's `next` is always `None`.
- **The SDE Secret:** Because we have a `tail` pointer, adding a car to the end is **O(1)** time—that means it's instant, no matter how long the train is!
""")

st.success("Level 4 Complete: You just built a data structure used by millions of people!")