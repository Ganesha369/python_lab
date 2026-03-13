import streamlit as st
import random
import time

# --- SORTING ALGORITHMS ---

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# --- STREAMLIT UI ---

st.set_page_config(page_title="Sorting Adventure", page_icon="📊")

st.title("🚀 Sorting Speed Test: Quick vs Merge")
st.write("""
Hi! I'm an SDE-2 at Microsoft. Today, we're going to see how 
fast we can sort a messy pile of numbers using our two favorite algorithms!
""")

# User Controls
num_elements = st.slider("How many numbers should we sort?", 100, 5000, 1000)
generate_data = st.button("Generate Random Numbers")

if 'data' not in st.session_state:
    st.session_state.data = [random.randint(1, 10000) for _ in range(num_elements)]

if generate_data:
    st.session_state.data = [random.randint(1, 10000) for _ in range(num_elements)]
    st.success(f"Generated {num_elements} random numbers!")

st.write(f"First 10 numbers: `{st.session_state.data[:10]}...`")

col1, col2 = st.columns(2)

with col1:
    st.header("⚡ Quick Sort")
    if st.button("Run Quick Sort"):
        start_time = time.time()
        sorted_data = quick_sort(st.session_state.data)
        end_time = time.time()
        st.success(f"Done in {end_time - start_time:.5f} seconds!")
        st.write(f"Sorted: `{sorted_data[:5]}...`")

with col2:
    st.header("🧩 Merge Sort")
    if st.button("Run Merge Sort"):
        start_time = time.time()
        sorted_data = merge_sort(st.session_state.data)
        end_time = time.time()
        st.success(f"Done in {end_time - start_time:.5f} seconds!")
        st.write(f"Sorted: `{sorted_data[:5]}...`")

st.divider()
st.info("💡 **Engineer's Tip:** Notice how both are incredibly fast? Standard sorting (Bubble Sort) would take much longer as the number of items grows!")