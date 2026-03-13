```python
import streamlit as st
import time
import random

# --- STREAMLIT SETUP ---
st.set_page_config(page_title="Sorting Academy", page_icon="📊")
st.title("📊 The Sorting Academy")
st.write("Hi! I'm your Microsoft SDE Mentor. Let's watch how computers organize data!")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Settings")
sort_type = st.sidebar.selectbox("Choose an Algorithm", ["Bubble Sort", "Insertion Sort"])
data_size = st.sidebar.slider("How many numbers?", 5, 30, 15)
speed = st.sidebar.slider("Speed (seconds)", 0.01, 0.5, 0.1)

# Generate random data
if 'data' not in st.session_state or st.sidebar.button("Generate New List"):
    st.session_state.data = [random.randint(10, 100) for _ in range(data_size)]

data = st.session_state.data.copy()

# --- THE SORTING FUNCTIONS ---

def bubble_sort(arr):
    n = len(arr)
    chart = st.bar_chart(arr)
    status_text = st.empty()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Update the visual
                chart.bar_chart(arr)
                status_text.text(f"Swapping {arr[j+1]} and {arr[j]}")
                time.sleep(speed)
    status_text.success("✅ Done! The 'bubbles' have risen!")

def insertion_sort(arr):
    n = len(arr)
    chart = st.bar_chart(arr)
    status_text = st.empty()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        status_text.text(f"Picking up number: {key}")
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            chart.bar_chart(arr)
            time.sleep(speed)
            
        arr[j + 1] = key
        chart.bar_chart(arr)
    status_text.success("✅ Done! Everything is in its right place!")

# --- UI BUTTONS ---
col1, col2 = st.columns(2)
with col1:
    if st.button("Start Sorting!"):
        if sort_type == "Bubble Sort":
            bubble_sort(data)
        else:
            insertion_sort(data)

with col2:
    st.write(f"**Method:** {sort_type}")
    if sort_type == "Bubble Sort":
        st.info("Analogy: Heavy items sink, light bubbles rise!")
    else:
        st.info("Analogy: Organizing a hand of Uno cards!")

# --- EXPLANATION FOR THE STUDENT ---
st.divider()
st.subheader("What's happening under the hood?")
if sort_type == "Bubble Sort":
    st.write("""
    1. We look at two neighbors.
    2. If the left one is bigger, they **swap**.
    3. We do this over and over until the end.
    4. After one full pass, the biggest number is guaranteed to be at the far right!
    """)
else:
    st.write("""
    1. We take a number (the 'key').
    2. We look at all the numbers to its left.
    3. We **slide** the bigger numbers to the right to make a hole.
    4. We drop our 'key' into the perfect hole.
    """)
```