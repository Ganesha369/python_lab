```python
import streamlit as st
import time

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="Recursion Mirror Logic", page_icon="🪞")
st.title("🪞 The Recursion Mirror Logic")
st.write("Welcome, Junior SDE! Let's explore how functions talk to themselves.")

# --- SIDEBAR NAVIGATION ---
level = st.sidebar.radio("Select your Training Level:", 
                         ["Level 1: The Countdown", "Level 2: The Nesting Gift", "Level 3: The Factorial Factory"])

if level == "Level 1: The Countdown":
    st.header("🚀 The Rocket Launch")
    st.write("Recursion is great for counting down. The 'Base Case' is 0.")
    
    start_num = st.slider("Select start number:", 1, 10, 5)
    
    if st.button("Launch!"):
        output_area = st.empty()
        log = []
        
        def recursive_countdown(n):
            if n == 0:
                log.append("💥 BLAST OFF!")
                return
            else:
                log.append(f"Counting down: {n}...")
                recursive_countdown(n - 1)
        
        recursive_countdown(start_num)
        for line in log:
            st.write(line)
            time.sleep(0.3)
        st.balloons()

elif level == "Level 2: The Nesting Gift":
    st.header("🎁 The Mystery Box")
    st.write("We are looking for a '💎' hidden deep inside layers of boxes.")
    
    layers = st.number_input("How many layers of boxes?", min_value=1, max_value=10, value=3)
    
    if st.button("Open the Boxes"):
        def open_box(current_layer):
            if current_layer == 0:
                st.success("💎 Found the Diamond in the smallest box!")
                return
            else:
                st.write(f"📦 Opening box layer {current_layer}...")
                time.sleep(0.5)
                open_box(current_layer - 1)
                st.write(f"✅ Closing box layer {current_layer} back up.")
        
        open_box(layers)

elif level == "Level 3: The Factorial Factory":
    st.header("🔢 The Factorial Factory")
    st.write("A Factorial (n!) is just `n * (n-1) * (n-2)...`")
    st.info("Formula: `Factorial(n) = n * Factorial(n-1)`")
    
    num = st.number_input("Enter a number to Factorialize:", min_value=1, max_value=10, value=5)
    
    if st.button("Calculate"):
        steps = []
        
        def factorial(n):
            if n == 1:
                steps.append("Base Case: 1 reached!")
                return 1
            else:
                result = n * factorial(n - 1)
                steps.append(f"Calculating: {n} * {n-1}! = {result}")
                return result
        
        final_answer = factorial(num)
        
        for s in steps:
            st.write(s)
        st.metric("Final Result", final_answer)

# --- TEACHER'S NOTE ---
st.sidebar.divider()
st.sidebar.info("""
**SDE-2 Pro Tip:**
Recursion is beautiful but dangerous! Always ensure your **Base Case** is reachable, or you'll get a 'RecursionError'. 
In the real world, we use this for searching folders and sorting complex data.
""")
```