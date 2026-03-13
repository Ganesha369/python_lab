import streamlit as st
import heapq
import random

# Streamlit App Configuration
st.set_page_config(page_title="Heap Visualizer", page_icon="🏔️")

st.title("🏔️ The Heap: King of the Hill Visualizer")
st.write("""
Hi! I'm your Microsoft SDE mentor. Use this tool to see how numbers 
bubble up to the top of the heap!
""")

# Initialize Session State
if 'my_list' not in st.session_state:
    st.session_state.my_list = []

# Sidebar Controls
st.sidebar.header("Control Panel")
heap_type = st.sidebar.radio("Select Heap Type:", ["Min-Heap (Smallest at Top)", "Max-Heap (Largest at Top)"])
new_num = st.sidebar.number_input("Enter a number:", value=random.randint(1, 100))

col1, col2, col3 = st.sidebar.columns(3)

if col1.button("Add"):
    if heap_type == "Min-Heap (Smallest at Top)":
        heapq.heappush(st.session_state.my_list, new_num)
    else:
        # Max-Heap trick: use negative numbers
        heapq.heappush(st.session_state.my_list, -new_num)
    st.success(f"Added {new_num}!")

if col2.button("Pop King"):
    if st.session_state.my_list:
        val = heapq.heappop(st.session_state.my_list)
        display_val = val if heap_type == "Min-Heap (Smallest at Top)" else -val
        st.warning(f"The King {display_val} has left the hill!")
    else:
        st.error("Hill is empty!")

if col3.button("Clear"):
    st.session_state.my_list = []

# Visualizing the Heap
st.subheader("The Hill Hierarchy")

if not st.session_state.my_list:
    st.info("The hill is empty. Add some numbers to see the magic!")
else:
    # Prepare data for display
    if heap_type == "Min-Heap (Smallest at Top)":
        display_list = list(st.session_state.my_list)
        king = display_list[0]
    else:
        display_list = [-x for x in st.session_state.my_list]
        king = display_list[0]

    # Display the "King"
    st.metric(label="Current King (Top)", value=king)

    # Visual representation
    st.write("### How it looks in memory (List View):")
    st.write(display_list)

    # Tree logic explanation
    st.info(f"""
    **SDE Insight:** 
    - The King is at index `0`.
    - The King's children are at index `1` and `2`.
    - In a **{heap_type}**, index `0` will always be the {'minimum' if 'Min' in heap_type else 'maximum'} value.
    """)

    # Fun Progress Bars to show values
    st.write("### The Power Levels:")
    for i, val in enumerate(display_list):
        st.write(f"Spot {i}: {val}")
        st.progress(min(abs(val) / 100, 1.0))

st.divider()
st.write("Built with ❤️ by your Microsoft Mentor for future engineers.")