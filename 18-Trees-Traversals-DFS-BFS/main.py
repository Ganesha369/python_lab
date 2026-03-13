import streamlit as st
import time
import collections

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tree Traversal Explorer", layout="wide")

st.title("🌲 The Tree Explorer: DFS vs BFS")
st.write("Presented by your Microsoft SDE Mentor")

# --- TREE SETUP ---
# Let's define a simple tree in a dictionary
# 'A' is the root, it has children 'B' and 'C', etc.
tree = {
    'You (Root)': ['Friend A', 'Friend B'],
    'Friend A': ['Grandchild 1', 'Grandchild 2'],
    'Friend B': ['Grandchild 3', 'Grandchild 4'],
    'Grandchild 1': [],
    'Grandchild 2': [],
    'Grandchild 3': [],
    'Grandchild 4': []
}

col1, col2 = st.columns(2)

with col1:
    st.header("🕵️ Depth-First Search (DFS)")
    st.info("Strategy: Go as deep as possible first! (Uses a Stack)")
    if st.button("Run DFS Search"):
        visited = []
        stack = ['You (Root)']
        
        progress_bar = st.progress(0)
        status = st.empty()
        log = st.empty()
        
        step = 0
        while stack:
            # Pop the last item (Pringles style!)
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # Add children to stack
                stack.extend(reversed(tree[node]))
                
                status.write(f"**Currently Visiting:** {node}")
                log.write(f"Path taken: {' -> '.join(visited)}")
                time.sleep(1)
                step += 1
                progress_bar.progress(step * 14) # Approx for 7 nodes
        st.success("DFS Complete! We went deep into each branch.")

with col2:
    st.header("🤖 Breadth-First Search (BFS)")
    st.info("Strategy: Check everyone on this level first! (Uses a Queue)")
    if st.button("Run BFS Search"):
        visited = []
        queue = collections.deque(['You (Root)'])
        
        progress_bar = st.progress(0)
        status = st.empty()
        log = st.empty()
        
        step = 0
        while queue:
            # Pop the first item (Movie line style!)
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                # Add children to queue
                queue.extend(tree[node])
                
                status.write(f"**Currently Visiting:** {node}")
                log.write(f"Path taken: {' -> '.join(visited)}")
                time.sleep(1)
                step += 1
                progress_bar.progress(step * 14)
        st.success("BFS Complete! We scanned level by level.")

# --- THE TEACHING MOMENT ---
st.divider()
st.subheader("Which one should you use?")
st.write("""
- **Use BFS** if you want to find the **shortest path** (like finding the closest Starbucks).
- **Use DFS** if you want to explore **every possibility** to the end (like solving a maze or checking game moves).
""")

st.code("""
# Simple Python logic for DFS (Level 4 stuff!)
def dfs(node):
    if node is None: return
    print(node) # Visit
    dfs(node.left) # Go Deep Left
    dfs(node.right) # Go Deep Right
""", language="python")