# The Magic Growing Spyglass: Mastering Advanced Sliding Windows

Summary: Learn how to find the perfect "stretch" of data in a massive list without checking every single possibility twice!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=29-Advanced-Sliding-Window)

---

Hey there! I'm an engineer at Microsoft. When we have billions of pieces of data (like every song on Spotify), we can't afford to be slow. That's where the **Advanced Sliding Window** comes in.

### 1. SIMPLE DEFINITION: The Magic Spyglass 🔭
Imagine you have a long row of candies on a table. You have a **Spyglass** (your window). 
*   **Basic Window:** Your spyglass is taped at a fixed size (say, 3 candies wide). You just slide it along.
*   **Advanced Window:** Your spyglass is made of **magic rubber**. It can stretch to cover 10 candies or shrink to cover just 1. You stretch it to find more "goodies," and you shrink it the moment you break a rule (like having too many sour candies).

### 2. REAL WORLD: How we use it at Microsoft/Amazon
*   **Netflix/YouTube:** When you stream a video, the "Buffer" is a sliding window. It moves forward as you watch, dropping old video bits and grabbing new ones.
*   **Amazon:** If you search for "Best 3-day stretch of sales," we use a sliding window to scan the whole year in one quick pass.

### 3. THE TOOLS: Your Utility Belt 🛠️
To build an Advanced Sliding Window, we use three main things:
1.  **Left & Right Pointers:** Think of these as your two hands holding the edges of the rubber spyglass.
2.  **A Dictionary (Hash Map):** This is our "Inventory List." It keeps track of exactly how many of each item are inside our window right now.
3.  **The "While" Loop:** This is our "Shrink Trigger." If our window gets "too full" or breaks a rule, we use a `while` loop to pull the Left hand forward until the window is valid again.

### 4. THE LESSON: Level 0 to Level 4

**Level 0: The Goal**
Find the longest "stretch" of something that follows a rule. (Example: Longest piece of a string with no repeating characters).

**Level 1: The Expansion (Right Hand)**
We move our `right` pointer forward one by one. Every time we move, we add that new item to our "Inventory List."

**Level 2: The Violation**
Oh no! We just added a character that was already in our window. The rule is broken!

**Level 3: The Contraction (Left Hand)**
We don't start over! We just slide the `left` pointer forward, removing items from our inventory, until the rule isn't broken anymore.

**Level 4: The Record**
Every time the window is "valid," we check: "Is this the biggest window I've seen so far?" If yes, save the size!

---

### 🐍 Full Code
