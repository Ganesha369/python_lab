import streamlit as st
import time

# --- STREAMLIT UI ---
st.set_page_config(page_title="Sliding Window Visualizer", layout="wide")
st.title("🔭 The Magic Spyglass: Sliding Window")
st.write("### Problem: Find the longest sequence with no repeating letters!")

# User Input
input_str = st.text_input("Enter a string to test:", "MICROSOFTROX")
speed = st.slider("Animation Speed (seconds)", 0.1, 2.0, 0.5)

if st.button("Start Searching!"):
    # Logic Variables
    left = 0
    max_len = 0
    char_map = {} # Our Inventory List
    res_start = 0
    
    # Visualization Columns
    col1, col2 = st.columns([2, 1])
    window_display = col1.empty()
    stats_display = col2.empty()
    
    # The Advanced Sliding Window Algorithm
    for right in range(len(input_str)):
        current_char = input_str[right]
        
        # Add to inventory
        char_map[current_char] = char_map.get(current_char, 0) + 1
        
        # SHRINK: While we have a duplicate, move the left pointer
        while char_map[current_char] > 1:
            left_char = input_str[left]
            char_map[left_char] -= 1
            left += 1
            
            # Update Visualization during shrinking
            window_display.info(f"🚨 Duplicate found! Shrinking window...\n\n**Current Window:** `{input_str[left:right+1]}`")
            time.sleep(speed)

        # Calculate Max
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            res_start = left
            
        # Update Visualization
        with window_display:
            # Highlighting the window
            display_str = ""
            for i, char in enumerate(input_str):
                if i == left == right: display_str += f"**[{char}]**"
                elif i == left: display_str += f"**[{char}**"
                elif i == right: display_str += f"**{char}]**"
                elif left < i < right: display_str += f"**{char}**"
                else: display_str += char
            
            st.markdown(f"## {display_str}")
            st.write(f"Window Size: `{right - left + 1}`")

        with stats_display:
            st.write("### 📝 Inventory List")
            st.json(char_map)
            st.metric("Max Length Found", max_len)
            
        time.sleep(speed)

    st.success(f"🏆 Done! The longest unique stretch was '{input_str[res_start:res_start+max_len]}' with a length of {max_len}!")

# Teacher's Note
st.sidebar.markdown("""
### 🍎 SDE-2 Lessons:
1. **O(N) Complexity:** Notice we only pass through the string once. Much faster than checking every possible sub-string!
2. **Two Pointers:** `left` and `right` are the heroes here.
3. **Dynamic Size:** Notice how the window grows and shrinks based on the rules.
""")