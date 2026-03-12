import streamlit as st

# Professional UI Setup
st.set_page_config(page_title="Anagram Checker", page_icon="🔍")

st.title("🔍 The Word Alchemist")
st.subheader("Are these words made of the same bricks?")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    word1 = st.text_input("Enter first word or phrase:", "Listen")
with col2:
    word2 = st.text_input("Enter second word or phrase:", "Silent")

# The Logic Function (SDE Best Practice: Keep logic in functions!)
def check_anagram(str1, str2):
    # 1. Clean the data (Lowercase and remove spaces)
    clean_str1 = str1.lower().replace(" ", "")
    clean_str2 = str2.lower().replace(" ", "")
    
    # 2. Edge case: If they aren't the same length, they can't be anagrams
    if len(clean_str1) != len(clean_str2):
        return False
    
    # 3. The 'Sorting' Magic
    return sorted(clean_str1) == sorted(clean_str2)

# Display the Result
if st.button("Check for Alchemy! ⚗️"):
    if word1 and word2:
        is_anagram = check_anagram(word1, word2)
        
        if is_anagram:
            st.success(f"✨ Huzzah! '{word1}' and '{word2}' ARE anagrams!")
            st.balloons()
        else:
            st.error(f"❌ Alas! These use different letters.")
            
        # Behind the scenes look for the student
        with st.expander("See how the computer sees it"):
            st.write(f"Word 1 Sorted: `{sorted(word1.lower().replace(' ', ''))}`")
            st.write(f"Word 2 Sorted: `{sorted(word2.lower().replace(' ', ''))}`")
    else:
        st.warning("Please enter both words to begin!")

# Footer
st.markdown("---")
st.caption("Microsoft SDE-2 Lesson: Milestone 06 - Logic & String Manipulation")