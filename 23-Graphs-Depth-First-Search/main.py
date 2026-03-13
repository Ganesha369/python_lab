import streamlit as st
import time

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="DFS Maze Runner", layout="wide")
st.title("🚀 The DFS Maze Runner")
st.subheader("Watch how Depth-First Search explores a graph!")

# 1. THE MAP (Adjacency List)
# This represents rooms and their connections
graph = {
    'Entrance': ['Library', 'Garden'],
    'Library': ['Secret Passage', 'Office'],
    'Garden': ['Tool Shed'],
    'Secret Passage': [],
    'Office': [],
    'Tool Shed': []
}

# 2. THE LOGIC BLOCK (DFS Algorithm)
def run_dfs(current_node, visited, path_order):
    # Add breadcrumb
    visited.add(current_node)
    path_order.append(current_node)
    
    # Explore neighbors
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            run_dfs(neighbor, visited, path_order)
    return path_order

# --- INTERACTIVE APP ---
col1, col2 = st.columns([1, 2])

with col1:
    st.write("### 🗺️ Our Map")
    for room, connections in graph.items():
        st.write(f"**{room}** is connected to: {', '.join(connections) if connections else 'Dead End'}")
    
    start_btn = st.button("Start Exploring!")

with col2:
    st.write("### 🏃 Exploration Log")
    if start_btn:
        visited_rooms = set()
        history = []
        
        # We simulate the DFS step-by-step for the student
        exploration_steps = []
        
        # Inner function to capture steps for animation
        def dfs_animate(node, visited):
            visited.add(node)
            exploration_steps.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_animate(neighbor, visited)

        dfs_animate('Entrance', visited_rooms)

        # Animation Loop
        for i, step in enumerate(exploration_steps):
            time.sleep(1) # Slow down for the student to see
            st.success(f"Step {i+1}: Entering **{step}**")
            if not graph[step]:
                st.warning(f"⚠️ Hit a dead end at {step}! Backtracking...")
        
        st.balloons()
        st.write("### ✅ Discovery Order:")
        st.write(" -> ".join(exploration_steps))

# --- MICROSOFT SDE TIP ---
st.info("""
**SDE Tip:** Notice how we went all the way to the 'Secret Passage' before we ever 
checked out the 'Garden'? That's DFS! It's great for puzzles, but if you want to find the 
*shortest* path, you'd usually use its cousin, BFS (Breadth-First Search).
""")