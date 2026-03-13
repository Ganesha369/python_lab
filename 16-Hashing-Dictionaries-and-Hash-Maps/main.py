import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="Magic Hash Map Tutor", page_icon="⚡")

st.title("⚡ The Digital Speed-Dial")
st.write("### Learn Hashing & Dictionaries with a Microsoft Engineer")

# Initialize our "Database" in session state so it doesn't reset
if 'my_dict' not in st.session_state:
    st.session_state.my_dict = {
        "MasterChief": "Halo",
        "Steve": "Minecraft",
        "Mario": "Super Mario Bros"
    }

# Level 1: The Visual Concept
st.header("1. The Secret Math (Hashing)")
user_input = st.text_input("Enter a username to see its 'Secret Cubby Number' (Hash):", "Alex")

if user_input:
    hash_value = hash(user_input)
    st.info(f"The word **'{user_input}'** hashes to cubby number: `{hash_value}`")
    st.write("In a real computer, we use this number to find your data instantly!")

# Level 2: The Dictionary in Action
st.header("2. Your Magic Cubby Room")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Add a Entry")
    new_key = st.text_input("Student Name:")
    new_val = st.text_input("Favorite Game:")
    if st.button("Add to Map"):
        st.session_state.my_dict[new_key] = new_val
        st.success(f"Added {new_key}!")

with col2:
    st.subheader("Current Data")
    st.write(st.session_state.my_dict)

# Level 3: Speed Test
st.header("3. Speed Test: List vs. Dictionary")
st.write("Why do we use Hash Maps? Because they are lightning fast!")

if st.button("Run Speed Test"):
    # Create a huge list and a huge dict
    big_list = list(range(1000000))
    big_dict = {i: True for i in range(1000000)}
    
    # Test List
    start_time = time.time()
    999999 in big_list
    list_time = time.time() - start_time
    
    # Test Dict
    start_time = time.time()
    999999 in big_dict
    dict_time = time.time() - start_time
    
    st.write(f"⏱ **List Search Time:** {list_time:.8f} seconds (Slow...)")
    st.write(f"🚀 **Dict (Hash Map) Search Time:** {dict_time:.8f} seconds (INSTANT!)")
    
    st.balloons()

# Footer
st.markdown("---")
st.write("👨‍💻 **SDE-2 Pro Tip:** Use Dictionaries whenever you need to look up data by a specific ID. It makes your code run at O(1) speed—that's constant time!")