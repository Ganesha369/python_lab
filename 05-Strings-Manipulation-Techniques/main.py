import streamlit as st

# Microsoft SDE Style Header
st.set_page_config(page_title="String Architect", page_icon="📝")
st.title("📝 String Manipulation Playground")
st.subheader("Level up your SDE-2 skills with Python strings!")

# Sidebar for Tools
st.sidebar.header("Your Toolbox")
tool_choice = st.sidebar.selectbox("Choose a Level", 
    ["Level 0: The Basics", 
     "Level 1: Slicing (Scissors)", 
     "Level 2: Makeover (Case)", 
     "Level 3: Surgeon (Replace)", 
     "Level 4: Detective (Reverse)"])

# User Input
user_text = st.text_input("Enter some text to manipulate:", "Hello World")

st.divider()

if tool_choice == "Level 0: The Basics":
    st.write("### What is a String?")
    st.write(f"Your string is: `{user_text}`")
    st.write(f"The length of your string is: **{len(user_text)}** characters.")
    st.code(f"len('{user_text}')")

elif tool_choice == "Level 1: Slicing (Scissors)":
    st.write("### Cut your string!")
    col1, col2 = st.columns(2)
    with col1:
        start = st.number_input("Start Index", value=0)
    with col2:
        end = st.number_input("End Index", value=5)
    
    sliced = user_text[start:end]
    st.success(f"Result: `{sliced}`")
    st.info(f"Logic: user_text[{start}:{end}]")

elif tool_choice == "Level 2: Makeover (Case)":
    st.write("### Change the Style")
    col1, col2, col3 = st.columns(3)
    if col1.button("UPPERCASE"):
        st.write(user_text.upper())
    if col2.button("lowercase"):
        st.write(user_text.lower())
    if col3.button("Title Case"):
        st.write(user_text.title())

elif tool_choice == "Level 3: Surgeon (Replace)":
    st.write("### Find and Replace")
    to_find = st.text_input("Word to find:")
    to_replace = st.text_input("Word to replace it with:")
    
    if to_find:
        new_text = user_text.replace(to_find, to_replace)
        st.success(f"New Version: {new_text}")
        st.code(f"user_text.replace('{to_find}', '{to_replace}')")

elif tool_choice == "Level 4: Detective (Reverse)":
    st.write("### Secret Codes & Palindromes")
    reversed_text = user_text[::-1]
    st.write(f"Backward: **{reversed_text}**")
    
    # Palindrome Check
    if user_text.lower().replace(" ", "") == reversed_text.lower().replace(" ", ""):
        st.balloons()
        st.success("🚨 ALERT: This is a Palindrome! (Reads the same forward and backward)")
    else:
        st.warning("Not a palindrome, but still a cool string!")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 **Pro Tip:** In Python, strings are *zero-indexed*. That means we start counting at 0, not 1!")