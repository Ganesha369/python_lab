import streamlit as st
import time
import pandas as pd
import numpy as np

# Streamlit App UI
st.set_page_config(page_title="Big O Explorer", page_icon="🚀")

st.title("🚀 The Code Speedometer (Big O)")
st.write("Hi! I'm your Microsoft SDE mentor. Move the slider to see how different code 'speeds' react to more data.")

# Level Slider
data_size = st.slider("How many items in our list?", min_value=1, max_value=100, value=10)

col1, col2, col3 = st.columns(3)

# Level 0 & 1: O(1) and O(n)
with col1:
    st.header("O(1)")
    st.info("The Constant")
    st.code(f"item = my_list[0]")
    st.write(f"Steps taken: **1**")
    st.caption("Always 1 step, no matter what!")

with col2:
    st.header("O(n)")
    st.info("The Linear")
    st.code("for item in my_list:\n    print(item)")
    st.write(f"Steps taken: **{data_size}**")
    st.caption("1 step per item.")

with col3:
    st.header("O(n²)")
    st.error("The Snail")
    st.code("for x in list:\n  for y in list:\n    print(x, y)")
    st.write(f"Steps taken: **{data_size**2}**")
    st.caption("It multiplies!")

# Visualizing the Growth
st.divider()
st.subheader("Graphing the 'Pain'")
st.write("Watch how the Red line (O(n²)) explodes compared to the others!")

# Create data for the chart
x = np.arange(1, data_size + 1)
chart_data = pd.DataFrame({
    "Items (n)": x,
    "O(1) - Instant": [1] * len(x),
    "O(n) - Fair": x,
    "O(n²) - Slow": x**2
})

st.line_chart(chart_data, x="Items (n)", y=["O(1) - Instant", "O(n) - Fair", "O(n²) - Slow"])

st.success("SDE Tip: Always look for loops inside loops. That's usually where the 'Snail' (O(n²)) is hiding!")