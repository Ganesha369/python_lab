import streamlit as st

st.set_page_config(page_title="Binary Wizardry", page_icon="🪄")

st.title("🪄 28-Bit-Manipulation-Magic")
st.write("### Hosted by your Microsoft SDE-2 Mentor")

st.info("Goal: Understand how computers use 0s and 1s to do fast math!")

# Sidebar for inputs
st.sidebar.header("Wizard Controls")
num_input = st.sidebar.number_input("Enter a Number", value=10, min_value=0, max_value=255)

# Visualizing Bits
def get_binary_string(n):
    return bin(n)[2:].zfill(8)

binary_str = get_binary_string(num_input)

st.subheader(f"Level 0: Visualizing {num_input}")
cols = st.columns(8)
for i, bit in enumerate(binary_str):
    label = "ON" if bit == "1" else "OFF"
    color = "orange" if bit == "1" else "gray"
    cols[i].markdown(f"**{bit}**")
    cols[i].image(f"https://img.icons8.com/ios-filled/50/{color}/light-switch.png", caption=f"Bit {7-i}")

# Interaction 1: AND trick
st.divider()
st.subheader("Level 1: The Even/Odd Detector")
is_odd = num_input & 1
if st.button("Is it Odd?"):
    if is_odd:
        st.success(f"Yes! {num_input} ends in 1, so it's ODD.")
    else:
        st.info(f"No! {num_input} ends in 0, so it's EVEN.")

# Interaction 2: Shifting
st.divider()
st.subheader("Level 2: The Bit Escalator (Shift)")
shift_amt = st.slider("Shift Left by how much?", 0, 3, 1)
shifted_val = num_input << shift_amt
st.code(f"{num_input} << {shift_amt} = {shifted_val}")
st.write(f"Binary: `{get_binary_string(num_input)}` became `{get_binary_string(shifted_val)}`")
st.caption("Notice how the 1s just slid to the left? That's instant multiplication!")

# Interaction 3: Power of 2
st.divider()
st.subheader("Level 3: Power of 2 Check")
if num_input > 0:
    is_pow_2 = (num_input & (num_input - 1)) == 0
    if is_pow_2:
        st.balloons()
        st.success(f"{num_input} is a Power of 2! 🚀")
    else:
        st.error(f"{num_input} is NOT a Power of 2.")

# Magic Trick Section
st.divider()
st.subheader("Level 4: The XOR Swap Magic")
val_a = st.number_input("Value A", value=5)
val_b = st.number_input("Value B", value=9)

if st.button("Swap without Temp Variable"):
    st.write("Performing: `a = a ^ b`, then `b = a ^ b`, then `a = a ^ b`...")
    val_a = val_a ^ val_b
    val_b = val_a ^ val_b
    val_a = val_a ^ val_b
    st.write(f"**New A:** {val_a} | **New B:** {val_b}")
    st.write("Magic! We swapped them using only logic gates!")

st.sidebar.markdown("---")
st.sidebar.write("Keep coding, future engineer! 👨‍💻")