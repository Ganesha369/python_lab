import streamlit as st
import time
import pandas as pd
import numpy as np

# --- STREAMLIT UI ---
st.set_page_config(page_title="Big O Speed Tester", page_icon="🚀")
st.title("🚀 Big O: Ninja vs. Turtle Speed Test")
st.write("Adjust the slider to see how different algorithms slow down as data grows!")

# Slider for input size (N)
n_size = st.slider("How many items in our list (N)?", min_value=10, max_value=2000, value=500, step=100)

# Create a list of N numbers
data = list(range(n_size))

# --- ALGORITHMS ---

def constant_time_op(arr):
    # O(1) - Just grab the first element
    return arr[0]

def linear_time_op(arr):
    # O(n) - Loop through everything once
    total = 0
    for x in arr:
        total += x
    return total

def quadratic_time_op(arr):
    # O(n^2) - Nested loop (Slow!)
    # We limit this to 2000 for the demo so it doesn't crash the browser
    total = 0
    # To make it visible, we only do a small subset if N is huge
    limit = min(len(arr), 1000) 
    for x in arr[:limit]:
        for y in arr[:limit]:
            total += (x + y)
    return total

# --- MEASUREMENT ---

col1, col2, col3 = st.columns(3)

# Test O(1)
start = time.perf_counter()
constant_time_op(data)
end = time.perf_counter()
col1.metric("O(1) - Instant", f"{(end-start)*1000:.4f} ms", "Fastest")

# Test O(n)
start = time.perf_counter()
linear_time_op(data)
end = time.perf_counter()
col2.metric("O(n) - Linear", f"{(end-start)*1000:.4f} ms", "Normal")

# Test O(n^2)
start = time.perf_counter()
quadratic_time_op(data)
end = time.perf_counter()
col3.metric("O(n^2) - Quadratic", f"{(end-start)*1000:.4f} ms", "Slow!", delta_color="inverse")

# --- VISUALIZATION ---
st.subheader("Complexity Chart")
st.write("This is what happens to your computer's brain as 'N' gets bigger:")

# Generate chart data
x = np.linspace(1, 20, 20)
chart_data = pd.DataFrame({
    'O(1) Constant': np.ones(20),
    'O(n) Linear': x,
    'O(n^2) Quadratic': x**2
})

st.line_chart(chart_data)

st.info("""
**SDE Pro Tip:** 
- **O(1)** is like knowing where your keys are. 
- **O(n)** is like looking for your keys in every pocket. 
- **O(n^2)** is like looking for your keys, but every time you check a pocket, you stop to check your phone!
""")