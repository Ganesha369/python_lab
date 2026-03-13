```python
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="BFS Ripple Explorer", layout="wide")
st.title("🌊 BFS: The 'Ripple' Search Visualizer")
st.write("""
Observe how Breadth-First Search explores a social network layer-by-layer! 
It finds your friends, then your friends-of-friends.
""")

# --- STEP 1: DEFINE THE GRAPH ---
# A dictionary representing a simple social network
network = {
    'You': ['Alice', 'Bob', 'Charlie'],
    'Alice': ['You', 'David', 'Eve'],
    'Bob': ['You', 'Frank'],
    'Charlie': ['You', 'Gina'],
    'David': ['Alice'],
    'Eve': ['Alice', 'Henry'],
    'Frank': ['Bob'],
    'Gina': ['Charlie'],
    'Henry': ['Eve']
}

# --- STEP 2: BFS LOGIC WITH ANIMATION ---
def run_bfs_visual(start_node):
    visited = []
    queue = deque([start_node])
    layers = {start_node: 0}
    
    # We'll use these to show the progress in the UI
    steps = []
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            steps.append(list(visited)) # Save a snapshot for animation
            
            for neighbor in network[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return steps

# --- STEP 3: VISUALIZATION ---
start_btn = st.button("🚀 Start BFS Search (From 'You')")

if start_btn:
    all_steps = run_bfs_visual('You')
    status_text = st.empty()
    chart_spot = st.empty()
    
    # Create the visual layout using NetworkX
    G = nx.Graph(network)
    pos = nx.spring_layout(G, seed=42)
    
    for i, visited_nodes in enumerate(all_steps):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Color nodes: Visited = Orange, Unvisited = SkyBlue
        colors = ['#FF6F61' if node in visited_nodes else '#88D8B0' for node in G.nodes()]
        
        nx.draw(G, pos, with_labels=True, node_color=colors, 
                node_size=2000, font_size=10, font_weight='bold', edge_color='#BDC3C7')
        
        status_text.subheader(f"Step {i+1}: Visited {visited_nodes[-1]}")
        chart_spot.pyplot(fig)
        plt.close()
        time.sleep(1.0) # Pause so the student can see the "ripple"
        
    st.success("✅ BFS Complete! Notice how it finished the inner circle before moving to the edges.")

# --- STEP 4: EDUCATIONAL SIDEBAR ---
st.sidebar.header("The SDE Toolbox")
st.sidebar.info("""
**Why a Queue?**
BFS uses a Queue (First-In-First-Out). It ensures we visit all "Level 1" nodes before moving to "Level 2".

**Time Complexity:**
O(V + E) 
(V = People, E = Friendships)
Basically, we look at everyone and every connection exactly once. Super efficient!
""")

st.sidebar.warning("""
**Interview Tip:**
If an interviewer asks for the **Shortest Path** in an unweighted map, your brain should immediately scream: **BFS!**
""")
```