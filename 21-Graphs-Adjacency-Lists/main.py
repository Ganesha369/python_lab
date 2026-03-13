import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Streamlit App Setup
st.set_page_config(page_title="Graph Master 2.0", layout="wide")
st.title("🕸️ The VIP Party Connection Mapper")
st.write("An SDE-2 Guide to **Adjacency Lists**")

# Initialize the graph in the session state so it stays around
if 'adj_list' not in st.session_state:
    st.session_state.adj_list = {
        "You": ["SDE-2 Guide"],
        "SDE-2 Guide": ["You", "Microsoft"],
        "Microsoft": ["SDE-2 Guide"]
    }

# UI Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🛠️ Build Your Graph")
    
    # Input for adding a node
    new_person = st.text_input("Add a new person (Node):", placeholder="e.g. Alice")
    if st.button("Add Person"):
        if new_person and new_person not in st.session_state.adj_list:
            st.session_state.adj_list[new_person] = []
            st.success(f"Added {new_person}!")

    st.divider()

    # Input for adding an edge
    people = list(st.session_state.adj_list.keys())
    if len(people) >= 2:
        person_a = st.selectbox("Person 1", people)
        person_b = st.selectbox("Person 2", people)
        if st.button("Connect Them!"):
            if person_b not in st.session_state.adj_list[person_a]:
                st.session_state.adj_list[person_a].append(person_b)
                st.session_state.adj_list[person_b].append(person_a)
                st.balloons()
            else:
                st.warning("They are already friends!")

with col2:
    st.header("📋 The Adjacency List (Logic)")
    st.write("This is how Python stores your data behind the scenes:")
    st.json(st.session_state.adj_list)

    st.header("🎨 The Visual Graph")
    # Draw the graph using NetworkX and Matplotlib
    G = nx.Graph()
    for person, friends in st.session_state.adj_list.items():
        for friend in friends:
            G.add_edge(person, friend)

    if not G.nodes():
        st.info("Add some people to see the map!")
    else:
        fig, ax = plt.subplots()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="#0078D4", 
                node_size=2000, edge_color="#CCCCCC", 
                font_size=12, font_color="white", font_weight="bold")
        st.pyplot(fig)

st.info("💡 **Engineer's Tip:** Notice how we only store names that ARE connected? If there were 1,000 people and you only had 2 friends, this list would only have 2 items. That's why Adjacency Lists are more 'Space Efficient' than a big Matrix grid!")