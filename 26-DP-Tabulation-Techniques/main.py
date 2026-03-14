import streamlit as st
import time

# --- STREAMLIT UI ---
st.set_page_config(page_title="DP Tabulation Master", layout="wide")
st.title("🧱 The DP Tabulation Builder")
st.write("Watch how a computer builds a 'Table' to solve the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...)!")

# User Input
n = st.slider("How many floors should our LEGO tower be?", min_value=2, max_value=15, value=7)

if st.button("Start Building Bottom-Up"):
    # Level 0: Create the notebook
    dp = [0] * (n + 1)
    
    # Level 1: Base Cases
    dp[0] = 0
    if n > 0:
        dp[1] = 1
        
    cols = st.columns(n + 1)
    
    # Visualizing the table initialization
    st.subheader("Step 1: Laying the Foundation")
    for i in range(n + 1):
        cols[i].metric(f"Index {i}", dp[i])
    
    time.sleep(1)
    
    # Level 2 & 3: Filling the table
    st.subheader("Step 2: Building Up (The Loop)")
    progress_bar = st.progress(0)
    
    status_text = st.empty()
    
    for i in range(2, n + 1):
        # The Logic
        status_text.write(f"Calculating Index {i}: Adding {dp[i-1]} + {dp[i-2]}...")
        dp[i] = dp[i-1] + dp[i-2]
        
        # Update UI
        cols[i].metric(f"Index {i}", dp[i], delta=dp[i-1])
        progress_bar.progress(i / n)
        time.sleep(0.5)
        
    st.success(f"✅ Tower Complete! The value at floor {n} is {dp[n]}.")
    
    # Showing the final "Notebook"
    st.write("### Your Final 'DP Table' (The Notebook)")
    st.table([dp])

    # SDE-2 Pro Tip
    st.info("**SDE-2 Pro Tip:** This took O(n) time. If we used recursion without a table, the computer would have to do way more work, especially as the tower gets taller!")

# Code explanation for the student
with st.expander("See the Logic (Python Code)"):
    st.code(f"""
def fib_tabulation(n):
    # 1. Create the table
    dp = [0] * (n + 1)
    
    # 2. Base cases
    dp[0] = 0
    dp[1] = 1
    
    # 3. Fill the table from bottom to top
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

print(fib_tabulation({n}))
    """, language="python")