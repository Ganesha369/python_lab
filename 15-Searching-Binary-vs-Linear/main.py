import streamlit as st
import time
import random

# App Config
st.set_page_config(page_title="Search Detective Lab", layout="wide")
st.title("🔍 The Search Detective Lab")
st.write("Compare Linear Search vs. Binary Search in real-time!")

# Sidebar Controls
st.sidebar.header("Settings")
list_size = st.sidebar.slider("How many items in the list?", 10, 100, 50)
target = st.sidebar.number_input("Target Number to find:", 0, list_size, 25)

# Generate Data
data = list(range(list_size))

col1, col2 = st.columns(2)

# --- LINEAR SEARCH VISUALIZER ---
with col1:
    st.subheader("🐢 Linear Search")
    st.caption("Checking one-by-one...")
    
    linear_placeholder = st.empty()
    status_linear = st.empty()
    
    if st.button("Run Linear Search"):
        found = False
        steps = 0
        for i in range(len(data)):
            steps += 1
            # Visualizing the search
            display_list = ["⬜"] * len(data)
            display_list[i] = "🔦" # The flashlight looking
            linear_placeholder.text(" ".join(display_list))
            status_linear.info(f"Step {steps}: Checking index {i}...")
            
            time.sleep(0.1) # Slow it down for kids to see
            
            if data[i] == target:
                display_list[i] = "✅"
                linear_placeholder.text(" ".join(display_list))
                status_linear.success(f"Found {target} in {steps} steps!")
                found = True
                break
        if not found:
            status_linear.error("Not found!")

# --- BINARY SEARCH VISUALIZER ---
with col2:
    st.subheader("⚡ Binary Search")
    st.caption("Splitting the list in half!")
    
    binary_placeholder = st.empty()
    status_binary = st.empty()
    
    if st.button("Run Binary Search"):
        low = 0
        high = len(data) - 1
        steps = 0
        found = False
        
        while low <= high:
            steps += 1
            mid = (low + high) // 2
            
            # Visualizing
            display_list = ["⬜"] * len(data)
            for j in range(low, high + 1):
                display_list[j] = "🟦" # The current search range
            display_list[mid] = "🎯" # The middle point
            
            binary_placeholder.text(" ".join(display_list))
            status_binary.info(f"Step {steps}: Middle is {mid}. High/Low range is getting smaller!")
            
            time.sleep(0.5) # Binary search is fast, keep it visible
            
            if data[mid] == target:
                display_list[mid] = "✅"
                binary_placeholder.text(" ".join(display_list))
                status_binary.success(f"Found {target} in {steps} steps!")
                found = True
                break
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if not found:
            status_binary.error("Not found!")

# Fun Fact at the bottom
st.divider()
st.markdown(f"""
### 💡 Microsoft Engineer Tip:
Notice how the **Linear Search** takes more time as the target gets further away? 
But **Binary Search** finds the number almost instantly because it's like "guessing the page" in a book! 

**Linear Complexity:** O(n)  
**Binary Complexity:** O(log n)
""")