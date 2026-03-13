import streamlit as st

# --- BST LOGIC ---
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def get_tree_display(root, level=0, prefix="Root: "):
    """Helper to visualize the tree in text"""
    if root is None:
        return ""
    
    display = "    " * level + prefix + str(root.data) + "\n"
    if root.left or root.right:
        if root.left:
            display += get_tree_display(root.left, level + 1, "L--- ")
        else:
            display += "    " * (level + 1) + "L--- None\n"
        if root.right:
            display += get_tree_display(root.right, level + 1, "R--- ")
        else:
            display += "    " * (level + 1) + "R--- None\n"
    return display

# --- STREAMLIT UI ---
st.set_page_config(page_title="BST Explorer", page_icon="🌳")

st.title("🌳 The Binary Search Tree Lab")
st.write("Welcome, Junior Engineer! Let's build a lightning-fast search system.")

# Initialize session state for the tree
if 'tree' not in st.session_state:
    st.session_state.tree = None
if 'history' not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Add Data")
    num = st.number_input("Enter a number to insert:", min_value=0, max_value=100, value=50)
    if st.button("Insert Node"):
        st.session_state.tree = insert(st.session_state.tree, num)
        st.session_state.history.append(f"Inserted {num}")
        st.success(f"Added {num} to the tree!")

    if st.button("Clear Tree"):
        st.session_state.tree = None
        st.session_state.history = []
        st.rerun()

with col2:
    st.subheader("Tree Structure")
    if st.session_state.tree:
        tree_text = get_tree_display(st.session_state.tree)
        st.code(tree_text, language="text")
    else:
        st.info("The tree is empty. Add a root node!")

st.divider()

st.subheader("How Search Works")
search_val = st.number_input("What number should we look for?", min_value=0, max_value=100, value=50)
if st.button("Simulate Search"):
    if st.session_state.tree:
        curr = st.session_state.tree
        path = []
        found = False
        while curr:
            path.append(str(curr.data))
            if curr.data == search_val:
                found = True
                break
            elif search_val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        
        if found:
            st.balloons()
            st.success(f"Found {search_val}! Path taken: {' ➔ '.join(path)}")
        else:
            st.error(f"{search_val} not in tree. Path searched: {' ➔ '.join(path)} ➔ None")
    else:
        st.warning("Build a tree first!")

st.sidebar.header("Dev Log")
for log in reversed(st.session_state.history):
    st.sidebar.text(log)