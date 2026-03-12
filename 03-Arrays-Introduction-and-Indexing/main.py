import streamlit as st

# Custom CSS to make it look cool for a 12-year-old
st.markdown("""
    <style>
    .locker-box {
        border: 3px solid #0078D4;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        background-color: #f0f2f6;
        font-size: 24px;
        margin: 5px;
    }
    .index-label {
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Array Explorer: Locker Edition")
st.write("Welcome to the Microsoft Coding Lab! Let's play with your locker array.")

# Initialize our array in the 'session state' so it stays saved
if 'my_lockers' not in st.session_state:
    st.session_state.my_lockers = ["🍕 Pizza", "🍎 Apple", "🍫 Choco", "🌮 Taco", "🎮 Game"]

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Locker Tools")
index_to_access = st.sidebar.number_input("Enter Index (0-4)", min_value=0, max_value=4, value=0)
new_item = st.sidebar.text_input("New Item Name", "🍩 Donut")

if st.sidebar.button("Replace Item"):
    st.session_state.my_lockers[index_to_access] = new_item
    st.sidebar.success(f"Locker {index_to_access} updated!")

# --- VISUALIZING THE ARRAY ---
st.subheader("Your Locker Room Row")
cols = st.columns(len(st.session_state.my_lockers))

for i, item in enumerate(st.session_state.my_lockers):
    with cols[i]:
        st.markdown(f"<div class='locker-box'>{item}</div>", unsafe_allow_html=True)
        st.markdown(f"<p class='index-label' style='text-align:center'>Index {i}</p>", unsafe_allow_html=True)

# --- THE LESSON INTERACTIVE ---
st.divider()
st.info(f"**SDE-2 Pro Tip:** You just accessed index **{index_to_access}**. "
        f"The computer found: **{st.session_state.my_lockers[index_to_access]}**!")

st.write(f"**Array Length:** Currently, your array has `{len(st.session_state.my_lockers)}` lockers.")

if st.button("Show me the code for this!"):
    st.code(f"""
# To get the item you selected:
item = my_lockers[{index_to_access}]
print(item) # Result: {st.session_state.my_lockers[index_to_access]}
    """)