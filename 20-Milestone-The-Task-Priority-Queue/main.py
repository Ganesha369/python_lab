import streamlit as st
import heapq
import time

# --- SETUP ---
st.set_page_config(page_title="Task Priority Queue", page_icon="🚀")

st.title("🚀 The VIP Task Manager")
st.write("Welcome to the Priority Queue simulator! Add tasks and watch how the computer re-orders them based on importance.")

# We use 'session_state' to keep our data alive while the app reruns
if 'queue' not in st.session_state:
    st.session_state.queue = []
    # Adding a counter to act as a tie-breaker for same-priority tasks
    st.session_state.counter = 0

# --- SIDEBAR: ADD TASKS ---
st.sidebar.header("Add New Task")
task_name = st.sidebar.text_input("Task Description", placeholder="e.g. Save the world")
priority = st.sidebar.slider("Priority Level (1 = Urgent, 10 = Relaxed)", 1, 10, 5)

if st.sidebar.button("Add to Queue"):
    if task_name:
        # We push a tuple: (priority_number, tie_breaker, task_name)
        # heapq uses the first element to sort
        heapq.heappush(st.session_state.queue, (priority, st.session_state.counter, task_name))
        st.session_state.counter += 1
        st.sidebar.success(f"Added: {task_name}")
    else:
        st.sidebar.error("Please enter a task name!")

# --- MAIN AREA: THE QUEUE ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Current Queue (Behind the Scenes)")
    if st.session_state.queue:
        # We show it as a list, but sorted so the student sees the 'priority' logic
        sorted_display = sorted(st.session_state.queue)
        for p, c, t in sorted_display:
            st.write(f"**Priority {p}**: {t}")
    else:
        st.write("The queue is empty. Add tasks from the sidebar!")

with col2:
    st.subheader("⚙️ Process Next Task")
    if st.button("EXECUTE HIGHEST PRIORITY"):
        if st.session_state.queue:
            # heappop always grabs the smallest priority number
            prio, count, task = heapq.heappop(st.session_state.queue)
            
            with st.spinner(f"Processing '{task}'..."):
                time.sleep(1) # Simulate 'work' being done
                st.balloons()
                st.success(f"COMPLETED: {task} (Priority {prio})")
        else:
            st.warning("No tasks left to process!")

# --- FOOTER ---
st.divider()
st.info("💡 **SDE-2 Tip:** Notice how even if you add a Priority 1 task LAST, it will always be the first one to be 'Executed'! That's the power of the Priority Queue.")