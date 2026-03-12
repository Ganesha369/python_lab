# 🔍 The Word Alchemist: Mastering the Anagram Secret

Summary: Learn how to tell if two words are secret twins by breaking them down into their "DNA" using Python!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=06-Milestone-The-Anagram-Checker)

---

Hey there! I'm an engineer at Microsoft, and today we’re going to build something called an **Anagram Checker**. 

### 1. SIMPLE DEFINITION: The Lego Box Analogy
Imagine you have two Lego sets. One is built into a **Dragon** and the other is built into a **Spaceship**. 

An **Anagram** is when both the Dragon and the Spaceship use the *exact same bricks* from the box, just rearranged differently. If you take the Dragon apart, you should have the same number of red, blue, and yellow bricks as the Spaceship. 

*   "Listen" and "Silent" are anagrams.
*   "Dormitory" and "Dirty Room" are anagrams!

### 2. REAL WORLD: Why does Microsoft or Google care?
In the professional world, we use this logic for **Search Engines**. 

Have you ever typed a word into Google with a typo, like "Pythno," and it asks, *"Did you mean Python?"* Google uses algorithms similar to anagram checking to find words that share the same letters to help guess what you meant. It’s also used in **Cybersecurity** to create or crack secret codes!

### 3. THE TOOLS: Our Tech Stack
To build this, we are using:
*   **Python:** Our engine.
*   **`.lower()`:** This tells the computer that 'A' and 'a' are the same thing (because computers are very picky).
*   **`.replace(" ", "")`:** This removes spaces. "New York" and "Worn Key" are anagrams, but we need to ignore the spaces to see it!
*   **`sorted()`:** This is our "Magic Organizer." It takes a word like "CAKE" and puts the letters in alphabetical order: "ACEK". If two words result in the same "sorted" string, they are anagrams!

---

### 4. THE LESSON: Level 0 to Level 4

#### Level 0: The Setup
We need two inputs from the user.
```python
word1 = "Listen"
word2 = "Silent"
```

#### Level 1: The Cleanup
Computers think "L" and "l" are different. We make everything lowercase and remove spaces so we compare fairly.
```python
clean_word1 = word1.lower().replace(" ", "")
clean_word2 = word2.lower().replace(" ", "")
```

#### Level 2: The Sort
This is the "A-Z" trick. 
*   "silent" becomes `['e', 'i', 'l', 'n', 's', 't']`
*   "listen" becomes `['e', 'i', 'l', 'n', 's', 't']`
```python
sorted1 = sorted(clean_word1)
sorted2 = sorted(clean_word2)
```

#### Level 3: The Big Comparison
If the sorted lists are exactly the same, we have a match!
```python
if sorted1 == sorted2:
    print("It's an Anagram!")
```

#### Level 4: The Professional App
We wrap it all in **Streamlit** to give it a "Face" (a User Interface) so anyone can use it in their browser.

### 🐍 Full Code
