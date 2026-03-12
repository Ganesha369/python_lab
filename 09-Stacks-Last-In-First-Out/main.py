import streamlit as st

# --- STREAMLIT SETUP ---
st.set_page_config(page_title="Stack Master 3000", page_icon="🥞")
st.title("🥞 The Pancake Stack Visualizer")
st.write("Welcome to the Microsoft SDE-2 Training Lab. Let's learn LIFO!")

# Initialize our stack in the "session_state" so it doesn't disappear when the app refreshes
if 'my_stack' not in st.session_state:
    st.session_state.my_stack = []

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Kitchen Controls")
new_pancake = st.sidebar.text_input("Enter a Pancake Flavor:", placeholder="e.g. Strawberry")

col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("Push (Add) ➕"):
        if new_pancake:
            st.session_state.my_stack.append(new_pancake)
            st.success(f"Added {new_pancake}!")
        else:
            st.warning("Type a flavor first!")

with col2:
    if st.button("Pop (Eat) 🍴"):
        if len(st.session_state.my_stack) > 0:
            removed = st.session_state.my_stack.pop()
            st.error(f"Ate the {removed} pancake!")
        else:
            st.info("The plate is empty! Nothing to pop.")

# --- MAIN DISPLAY ---
st.subheader("Your Virtual Stack")

if not st.session_state.my_stack:
    st.write("🍽️ The plate is currently empty. Add a pancake from the sidebar!")
else:
    # We display the stack in reverse because the "Top" should be at the top of the screen
    for i, item in enumerate(reversed(st.session_state.my_stack)):
        if i == 0:
            st.markdown(f"### 🔝 TOP: {item}")
            st.write("---")
        else:
            st.write(f"🥞 {item}")

st.sidebar.markdown("---")
st.sidebar.write("**SDE Pro-Tip:**")
st.sidebar.info("In Python, using a list as a stack is very fast! It has an O(1) time complexity for appending and popping.")

# Show the raw logic for the student
with st.expander("See the Logic Code"):
    st.code(f"""
# Current Stack State:
stack = {st.session_state.my_stack}

# To add:
# stack.append('{new_pancake}')

# To remove:
# stack.pop()
    """)