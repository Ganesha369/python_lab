```python
import streamlit as st
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dijkstra's Shortcut Finder", layout="wide")

st.title("🗺️ Dijkstra's Shortcut Finder")
st.write("""
Hi! I'm your Microsoft SDE mentor. Use this app to see how Dijkstra's Algorithm 
calculates the fastest route between cities!
""")

# --- 1. SETUP THE DATA ---
# (City A, City B, Travel Time)
edges = [
    ("Home", "Library", 2),
    ("Home", "Cafe", 5),
    ("Library", "Cafe", 2),
    ("Library", "Park", 8),
    ("Cafe", "Park", 3),
    ("Cafe", "School", 9),
    ("Park", "School", 1),
]

def run_dijkstra(start_node, target_node):
    # Create Adjacency List
    graph = {}
    for u, v, w in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w)) # Making it two-way

    # Dijkstra Logic
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessors = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct path
    path = []
    curr = target_node
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    return path[::-1], distances[target_node]

# --- 2. USER INTERFACE ---
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Settings")
    all_cities = sorted(list(set([e[0] for e in edges] + [e[1] for e in edges])))
    start = st.selectbox("Where are you starting?", all_cities, index=0)
    end = st.selectbox("Where do you want to go?", all_cities, index=len(all_cities)-1)
    
    if st.button("Find Shortest Path!"):
        path, total_time = run_dijkstra(start, end)
        st.success(f"✅ Found it! Total time: {total_time} mins")
        st.write(f"**Route:** {' ➡️ '.join(path)}")
    else:
        path = []

with col2:
    st.header("Visual Map")
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="#0078D4")
    nx.draw_networkx_labels(G, pos, font_color="white", font_weight="bold")
    
    # Draw regular edges
    nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", alpha=0.5)
    
    # Highlight the path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=5, edge_color="#76B900")

    # Edge labels (Weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    st.pyplot(fig)

# --- 3. EXPLAINER ---
st.divider()
st.subheader("How the code works (The SDE Secrets)")
st.info("""
1. **Priority Queue (`heapq`)**: This is our VIP line. It makes sure we always explore the city that is closest to us first.
2. **Infinite Distances**: We start by assuming every city is 'Infinity' miles away.
3. **The Update**: As we find paths, we check: *'Is (Current Distance + Road) < What I previously wrote in my notebook?'* If yes, update it!
""")
```