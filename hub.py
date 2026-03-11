import streamlit as st
import os

st.set_page_config(page_title="DSA University Hub", page_icon="🐍", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 12px; border: 1px solid #00D1B2; text-align: left; padding-left: 20px; color: white; height: 3.5em; }
    .stButton>button:hover { background-color: rgba(0, 209, 178, 0.1); border: 1px solid #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 1. Capture Direct Link
query_path = st.query_params.get("path", "🏠 Home")
if "page" not in st.session_state:
    st.session_state.page = query_path

# --- DATA ---
curriculum = ['01-Basics-Big-O-Notation', '02-Basics-Time-and-Space-Complexity', '03-Arrays-Introduction-and-Indexing', '04-Arrays-Common-Operations', '05-Strings-Manipulation-Techniques', '06-Milestone-The-Anagram-Checker', '07-Linked-Lists-Singly-Linked', '08-Linked-Lists-Doubly-Linked', '09-Stacks-Last-In-First-Out', '10-Queues-First-In-First-Out', '11-Recursion-The-Mirror-Logic', '12-Milestone-Building-a-Undo-Redo-System', '13-Sorting-Bubble-and-Insertion', '14-Sorting-Quick-and-Merge', '15-Searching-Binary-vs-Linear', '16-Hashing-Dictionaries-and-Hash-Maps', '17-Trees-Binary-Search-Trees', '18-Trees-Traversals-DFS-BFS', '19-Heaps-Max-and-Min-Heap', '20-Milestone-The-Task-Priority-Queue', '21-Graphs-Adjacency-Lists', '22-Graphs-Breadth-First-Search', '23-Graphs-Depth-First-Search', '24-Graphs-Shortest-Path-Dijkstra', '25-DP-Memoization-Basics', '26-DP-Tabulation-Techniques', '27-Backtracking-Solving-Mazes', '28-Bit-Manipulation-Magic', '29-Advanced-Sliding-Window', '30-Final-Capstone-The-Algorithm-Visualizer']
completed = [t for t in curriculum if os.path.exists(t)]

# Sidebar Navigation
st.sidebar.title("🐍 DSA Academy")
sidebar_nav = st.sidebar.selectbox("Jump to Lesson:", ["🏠 Home Dashboard"] + completed, index=0 if st.session_state.page not in completed else completed.index(st.session_state.page)+1)

if sidebar_nav != st.session_state.page:
    st.session_state.page = sidebar_nav
    st.query_params["path"] = sidebar_nav
    st.rerun()

# --- CONTENT AREA ---
if st.session_state.page in ["🏠 Home", "🏠 Home Dashboard"]:
    st.title("🎓 Python DSA University")
    st.write("Welcome, Student! Select a module to begin your journey to SDE-1.")
    st.divider()
    
    for topic in curriculum:
        is_done = topic in completed
        status = "✅" if is_done else "⏳"
        if is_done:
            if st.button(f"{status} {topic.replace('-', ' ')}", key=f"btn_{topic}"):
                st.session_state.page = topic
                st.query_params["path"] = topic
                st.rerun()
        else:
            st.button(f"{status} {topic.replace('-', ' ')} (Locked)", disabled=True)
else:
    # AUTOMATIC LESSON RUNNER
    st.markdown(f"## 🚀 {st.session_state.page.replace('-', ' ')}")
    if st.button("⬅️ Back to Syllabus"):
        st.session_state.page = "🏠 Home Dashboard"
        st.query_params["path"] = "🏠 Home Dashboard"
        st.rerun()
    
    st.divider()
    
    try:
        path = os.path.join(st.session_state.page, "main.py")
        with open(path, encoding='utf-8') as f:
            exec(f.read())
    except Exception as e:
        st.error(f"Execution Error: {e}")
