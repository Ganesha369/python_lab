import streamlit as st
import time

# --- STREAMLIT APP CONFIG ---
st.set_page_config(page_title="Array Ops Lab", layout="centered")

st.title("🚀 Array Operations Lab")
st.write("Welcome, Junior SDE! Use the controls below to manipulate our 'Digital Locker' array.")

# Initialize the array in session state so it stays between clicks
if 'locker_row' not in st.session_state:
    st.session_state.locker_row = ["🍎 Apple", "🎮 Controller", "📚 Book"]

# --- VISUALIZATION ---
st.subheader("Your Lockers")
cols = st.columns(len(st.session_state.locker_row) + 1)

for i, item in enumerate(st.session_state.locker_row):
    with cols[i]:
        st.info(f"Index {i}")
        st.code(item)

# --- OPERATIONS UI ---
st.divider()
st.subheader("Common Operations")

col1, col2 = st.columns(2)

with col1:
    # OPERATION: UPDATE
    st.write("### 📝 Update")
    idx_to_update = st.number_input("Locker Index:", min_value=0, max_value=len(st.session_state.locker_row)-1, step=1)
    new_val = st.text_input("New Item Name:", "💎 Diamond")
    if st.button("Swap Item"):
        st.session_state.locker_row[idx_to_update] = new_val
        st.success(f"Updated index {idx_to_update}!")
        st.rerun()

with col2:
    # OPERATION: INSERT/APPEND
    st.write("### ➕ Add")
    add_val = st.text_input("Item to Add:", "🍕 Pizza")
    if st.button("Add to End (Append)"):
        st.session_state.locker_row.append(add_val)
        st.rerun()
    
    if st.button("Insert at Index 0"):
        st.session_state.locker_row.insert(0, add_val)
        st.rerun()

st.divider()

col3, col4 = st.columns(2)

with col3:
    # OPERATION: DELETE
    st.write("### 🗑️ Delete")
    idx_to_pop = st.number_input("Remove Locker #:", min_value=0, max_value=len(st.session_state.locker_row)-1, step=1, key="del")
    if st.button("Delete Item"):
        if len(st.session_state.locker_row) > 1:
            removed = st.session_state.locker_row.pop(idx_to_pop)
            st.warning(f"Removed {removed}")
            st.rerun()
        else:
            st.error("Don't delete your last locker!")

with col4:
    # OPERATION: SEARCH
    st.write("### 🔍 Search")
    search_query = st.text_input("Find Item:", "🍎 Apple")
    if st.button("Scan Lockers"):
        if search_query in st.session_state.locker_row:
            found_idx = st.session_state.locker_row.index(search_query)
            st.balloons()
            st.success(f"Found at Index {found_idx}!")
        else:
            st.error("Item not found.")

# --- PRO TIP ---
st.sidebar.title("SDE Pro-Tips 💡")
st.sidebar.info("""
1. **0-Indexing:** Always remember locker #1 is actually at index 0.
2. **Shifting:** When you 'Insert' at index 0, every other item has to move one spot to the right. This is slow if you have 1 million items!
3. **Speed:** Searching (Level 4) is like looking for a needle in a haystack. The longer the array, the longer it takes.
""")