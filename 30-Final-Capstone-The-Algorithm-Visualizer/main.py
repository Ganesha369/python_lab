import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# --- SETTING UP THE PAGE ---
st.set_page_config(page_title="Algorithm Visualizer", layout="wide")
st.title("📊 The Algorithm Visualizer")
st.write("Watch how **Bubble Sort** organizes a messy list of numbers in real-time!")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Settings")
list_size = st.sidebar.slider("How many numbers?", 5, 50, 20)
speed = st.sidebar.slider("Speed (Seconds)", 0.01, 0.5, 0.1)

# --- THE LOGIC: BUBBLE SORT ---
def bubble_sort(arr):
    n = len(arr)
    # Create a place to show the graph
    chart_holder = st.empty() 
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # 1. Highlight the two we are comparing
            # (In code, we just do the logic)
            if arr[j] > arr[j + 1]:
                # 2. The "Swap"
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # 3. Visualization: Draw the bars
                fig, ax = plt.subplots()
                colors = ['teal' if x != j + 1 else 'orange' for x in range(len(arr))]
                ax.bar(range(len(arr)), arr, color=colors)
                ax.set_title("Sorting in progress...")
                
                # Show it on the website
                chart_holder.pyplot(fig)
                plt.close(fig) # Clean up memory
                
                # 4. Slow down time!
                time.sleep(speed)
    
    # Show the final sorted version
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color="green")
    ax.set_title("✅ Sorted!")
    chart_holder.pyplot(fig)

# --- THE APP FLOW ---
# Create some random data
if 'data' not in st.session_state:
    st.session_state.data = [random.randint(1, 100) for _ in range(list_size)]

if st.button('🔀 Scramble Numbers'):
    st.session_state.data = [random.randint(1, 100) for _ in range(list_size)]
    st.rerun()

if st.button('🚀 Start Sorting'):
    bubble_sort(st.session_state.data)

# Initial drawing
fig, ax = plt.subplots()
ax.bar(range(len(st.session_state.data)), st.session_state.data, color="teal")
st.pyplot(fig)

st.info("The orange bar shows the number currently 'bubbling' up to its correct spot!")