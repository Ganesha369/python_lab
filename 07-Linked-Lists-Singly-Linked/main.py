import streamlit as st

# --- LOGIC BLOCKS ---
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def get_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

# --- STREAMLIT UI ---
st.set_page_config(page_title="Linked List Treasure Hunt", layout="centered")

st.title("🏴‍☠️ Linked List Treasure Hunt")
st.write("Welcome, Junior SDE! Use the buttons below to build your chain of clues.")

# Initialize session state to keep our list alive
if 'my_list' not in st.session_state:
    st.session_state.my_list = LinkedList()
    # Adding some default items
    st.session_state.my_list.append("Map")
    st.session_state.my_list.append("Compass")

# Sidebar for controls
st.sidebar.header("Control Panel")
new_item = st.sidebar.text_input("Enter Treasure Name:", "Diamonds")

if st.sidebar.button("Add Treasure (Append)"):
    if new_item:
        st.session_state.my_list.append(new_item)
        st.toast(f"Added {new_item} to the end of the hunt!")

if st.sidebar.button("Remove First Item"):
    st.session_state.my_list.delete_first()
    st.toast("Removed the first clue!")

# Visualizing the List
st.subheader("Current Treasure Chain")
current_items = st.session_state.my_list.get_list()

if not current_items:
    st.info("The hunt is empty! Add some clues from the sidebar.")
else:
    # Creating a cool visual flow
    cols = st.columns(len(current_items) * 2 - 1)
    for i, item in enumerate(current_items):
        # Display the Node
        cols[i*2].info(f"**Node**\n\n{item}")
        
        # Display the Pointer (Arrow)
        if i < len(current_items) - 1:
            cols[i*2 + 1].write("➡️")
    
    st.success(f"The 'Head' is currently: **{current_items[0]}**")

# Fun Fact Section
with st.expander("🤓 Why don't we just use a normal list?"):
    st.write("""
    Great question! In a normal list (Array), if you want to put something at the very beginning, 
    you have to push every other item one spot to the right. That's a lot of work!
    
    In a **Linked List**, you just point your new clue to the old 'Head' and you're done! 
    It's super fast, no matter how many items you have.
    """)

st.markdown("---")
st.caption("Microsoft Student Learning Series | SDE-2 Lesson 07")