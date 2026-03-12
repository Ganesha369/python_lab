import streamlit as st

# --- MS SDE STYLE LAYOUT ---
st.set_page_config(page_title="Digital Time Machine", layout="centered")
st.title("⏪ The Undo-Redo Lab")
st.write("Type something below. If you make a mistake, use the buttons to travel through time!")

# --- INITIALIZING THE STACKS (The Memory) ---
# We use session_state so the data stays put when the app reruns
if 'undo_stack' not in st.session_state:
    st.session_state.undo_stack = [""]  # Start with an empty document
if 'redo_stack' not in st.session_state:
    st.session_state.redo_stack = []

# --- LOGIC BLOCKS ---

def add_action(new_text):
    # Only save if the text actually changed
    if new_text != st.session_state.undo_stack[-1]:
        st.session_state.undo_stack.append(new_text)
        # LEVEL 3 RULE: New action clears the redo "future"
        st.session_state.redo_stack = []

def undo():
    if len(st.session_state.undo_stack) > 1:
        # Move the top plate from Undo to Redo
        last_action = st.session_state.undo_stack.pop()
        st.session_state.redo_stack.append(last_action)

def redo():
    if len(st.session_state.redo_stack) > 0:
        # Move the top plate from Redo back to Undo
        future_action = st.session_state.redo_stack.pop()
        st.session_state.undo_stack.append(future_action)

# --- THE USER INTERFACE ---

# Text Input
current_text = st.session_state.undo_stack[-1]
user_input = st.text_input("Type here and press Enter:", value=current_text)

# If the user types something new
if user_input != current_text:
    add_action(user_input)
    st.rerun()

# Buttons for Time Travel
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Undo", use_container_width=True):
        undo()
        st.rerun()

with col2:
    if st.button("Redo ➡️", use_container_width=True):
        redo()
        st.rerun()

# --- DEBUGGER VIEW (The "Inside the Engine" look) ---
st.divider()
st.subheader("Inventory (Under the Hood)")
c1, c2 = st.columns(2)
with c1:
    st.write("**Undo Stack (History):**")
    st.write(st.session_state.undo_stack)
with c2:
    st.write("**Redo Stack (The Future):**")
    st.write(st.session_state.redo_stack)

st.info(f"**Current State:** {st.session_state.undo_stack[-1]}")