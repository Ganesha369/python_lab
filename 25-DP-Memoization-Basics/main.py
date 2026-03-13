import streamlit as st
import time
from functools import lru_cache

# --- PAGE CONFIG ---
st.set_page_config(page_title="Memoization Masterclass", page_icon="📝")

st.title("📝 The Memoization Time Machine")
st.write("""
As a Microsoft Engineer, I want to show you how we make code **1,000x faster**. 
We'll use the **Fibonacci Sequence**. To find the 30th number, the "Slow way" 
has to do millions of calculations. The "Memoized way" does it in a blink!
""")

# --- LOGIC ---

# 1. SLOW WAY (No Notebook)
def slow_fib(n):
    if n <= 1:
        return n
    return slow_fib(n-1) + slow_fib(n-2)

# 2. FAST WAY (With Notebook)
@lru_cache(maxsize=None)
def fast_fib(n):
    if n <= 1:
        return n
    return fast_fib(n-1) + fast_fib(n-2)

# --- UI ---

n = st.slider("Select a Fibonacci Number to find:", min_value=1, max_value=35, value=25)

col1, col2 = st.columns(2)

with col1:
    st.header("🐢 The Slow Way")
    st.write("No Memoization")
    start_time = time.time()
    result_slow = slow_fib(n)
    end_time = time.time()
    
    st.metric("Result", result_slow)
    st.error(f"Time: {end_time - start_time:.5f} seconds")
    st.write("The computer recalculated the same numbers over and over! 😫")

with col2:
    st.header("🚀 The Fast Way")
    st.write("With Memoization")
    start_time = time.time()
    result_fast = fast_fib(n)
    end_time = time.time()
    
    st.metric("Result", result_fast)
    st.success(f"Time: {end_time - start_time:.5f} seconds")
    st.write("The computer used its 'Secret Notebook'! 😎")

st.divider()

st.subheader("What just happened?")
st.info(f"""
When calculating Fibonacci({n}):
- The **Slow Way** performed a recursive tree search, repeating thousands of calculations.
- The **Fast Way** calculated each number exactly **once**, stored it, and just looked it up the next time it was needed.
- This is the core of **Dynamic Programming**. In a big company, this saves us millions of dollars in electricity and server costs!
""")

# Code display for the student
with st.expander("Peek at the Microsoft-level Code"):
    st.code("""
from functools import lru_cache

# The @lru_cache is our "Magic Notebook"
@lru_cache(maxsize=None)
def fast_fib(n):
    if n <= 1:
        return n
    # The computer checks the cache before doing this math:
    return fast_fib(n-1) + fast_fib(n-2)
    """, language="python")