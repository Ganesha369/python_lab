import streamlit as st
from collections import deque
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Queue Master 1.0", page_icon="🍕")

# --- CSS FOR STYLING ---
st.markdown("""
    <style>
    .queue-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border: 2px dashed #ff4b4b;
        text-align: center;
        margin-bottom: 10px;
    }
    .front-label { color: #ff4b4b; font-weight: bold; }
    .back-label { color: #1f77b4; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (The Brain of our App) ---
if 'pizza_queue' not in st.session_state:
    # We initialize our Queue using deque!
    st.session_state.pizza_queue = deque(["Pepperoni", "Cheese", "Veggie"])

# --- TITLE ---
st.title("🍕 The Pizza Shop Queue")
st.write(f"**Level 4 Engineer Mode:** Using `collections.deque` for FIFO logic.")

# --- INTERACTION ---
col1, col2 = st.columns(2)

with col1:
    new_order = st.text_input("Customer's Pizza Order:", placeholder="e.g. Pineapple")
    if st.button("➕ Enqueue (Add to Back)"):
        if new_order:
            st.session_state.pizza_queue.append(new_order)
            st.toast(f"Added {new_order} to the line!")
        else:
            st.error("Enter a pizza name first!")

with col2:
    st.write("Ready to cook?")
    if st.button("🍕 Dequeue (Serve Front)"):
        if len(st.session_state.pizza_queue) > 0:
            served = st.session_state.pizza_queue.popleft()
            st.success(f"Serving {served} now!")
            st.balloons()
        else:
            st.warning("The line is empty! No pizza to cook.")

# --- VISUALIZATION ---
st.divider()
st.subheader("The Live Line (FIFO View)")

if st.session_state.pizza_queue:
    # Display the queue horizontally
    cols = st.columns(len(st.session_state.pizza_queue) + 2)
    
    for i, pizza in enumerate(st.session_state.pizza_queue):
        with cols[i]:
            label = ""
            if i == 0: label = "<br><span class='front-label'>HEAD (Next)</span>"
            if i == len(st.session_state.pizza_queue)-1: label = "<br><span class='back-label'>TAIL (Last)</span>"
            
            st.markdown(f"""
                <div class="queue-box">
                    📦<br><b>{pizza}</b>
                    {label}
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("The shop is closed! No orders in the queue.")

# --- LOGIC EXPLAINER ---
with st.sidebar:
    st.header("SDE-2 Teachings")
    st.info("""
    **Why Deque?**
    In Python, a standard `list` is slow when removing items from the front because it has to move every other item over by one. 
    
    `deque` is like a two-way street; it allows us to 'pop' from the left instantly!
    """)
    
    st.code(f"""
# Current Logic
from collections import deque

queue = deque({list(st.session_state.pizza_queue)})

# To Enqueue:
queue.append("New Pizza")

# To Dequeue:
queue.popleft()
    """, language="python")

    if st.button("Reset Everything"):
        st.session_state.pizza_queue = deque(["Pepperoni", "Cheese", "Veggie"])
        st.rerun()