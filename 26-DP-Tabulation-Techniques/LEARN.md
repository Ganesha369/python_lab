# The LEGO Master Builder: Mastering the Art of the "DP Table"

Summary: Tabulation is like filling out a cheat-sheet table from the bottom up so you never have to solve the same math problem twice!

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=26-DP-Tabulation-Techniques)

---

Hey there, future engineer! I’m an SDE-2 at Microsoft. In the professional world, we hate doing the same work twice—it’s a waste of money and electricity. That’s where **Dynamic Programming (DP)** comes in. 

Specifically, we're looking at **Tabulation**.

### 1. The Analogy: The LEGO Tower 🧱
Imagine you are building a massive LEGO skyscraper. 
*   **Recursion** is like starting at the 100th floor and saying, "To build this, I first need the 99th floor," then asking the 99th floor person, who asks the 98th... all the way down to the ground. It’s a lot of shouting!
*   **Tabulation** is the "Bottom-Up" way. You start at the ground. You lay the first brick, then the second, then the third. You record exactly how much weight the base can hold in a notebook (your **Table**). By the time you get to the 100th floor, you don't need to ask anyone anything; you just look at your notebook for the 99th floor's data and add one more brick.

### 2. Real World: How Big Tech Uses This 🌐
*   **Amazon:** When you fill your cart, Amazon’s "Knapsack Algorithm" uses tabulation to figure out the best way to fit items into the fewest number of boxes to save on shipping.
*   **Google Maps:** To find the shortest path from your house to the mall, Google builds a table of distances for all the little intersections in between.

### 3. The Tools: Our Logic Blocks 🛠️
*   **The Array (The Table):** Usually called `dp[]`. This is our "notebook" where we store answers.
*   **Base Case:** This is the ground floor (e.g., `dp[0] = 0`). You can't build a house without a foundation!
*   **The Loop:** This is our "construction worker" who moves from the bottom to the top, one step at a time.
*   **The Logic:** `dp[i] = dp[i-1] + dp[i-2]`. This is the "blueprint" for how to calculate the next step using the previous ones.

---

### 4. The 5-Level Guide to Tabulation

#### Level 0: The Empty Notebook
We create a list of zeros. If we want to solve for step 5, we make a list of size 6 (because we count from 0).
`dp = [0] * 6`

#### Level 1: The Foundation (Base Case)
We know the answer for the simplest version.
`dp[0] = 0`
`dp[1] = 1`

#### Level 2: The Construction (The Loop)
We start from index 2 and go to the end.
```python
for i in range(2, 6):
    dp[i] = dp[i-1] + dp[i-2]
```

#### Level 3: The Finished Product
The very last cell in our table `dp[5]` now holds the answer for the whole problem!

#### Level 4: The Space Saver (Pro Move)
At Microsoft, we try to save memory. If you only need the last two numbers to find the next one, why keep the whole 100-page notebook? You can just keep two variables: `prev1` and `prev2`.

### 🐍 Full Code
