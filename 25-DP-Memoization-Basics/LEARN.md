# The Secret Notebook: How to be "Efficiently Lazy" with Memoization

Summary: Memoization is like having a magic notebook where you write down the answers to hard math problems so you never have to do the same work twice.

### [🚀 CHECK LIVE RESULT](https://ganesha-dsa-lab.streamlit.app/?path=25-DP-Memoization-Basics)

---

Hey there! I'm an SDE-2 (Software Development Engineer) at Microsoft. In the professional world, we don't just want code that *works*; we want code that is **fast**. 

Imagine I ask you: "What is 123,456 plus 987,654?" 
You spend two minutes with a pencil and paper and tell me: "1,111,110."
If I ask you the **exact same question** five seconds later, would you do the math again? **No way!** You'd just remember the answer you just got. That is exactly what **Memoization** is.

### 1. The Real World: How Big Tech Uses This
At **Amazon**, when you search for "Minecraft LEGO," the website doesn't recalculate the best results for every single person every single time. They "memoize" (cache) the results. The first person to search makes the computer work; for the next 10,000 people, Amazon just looks at its "Secret Notebook" and hands over the answer instantly.

### 2. The Logic Blocks
To do this in code, we need three things:
1.  **The Notebook:** Usually a `Dictionary` (a list of Key-Value pairs).
2.  **The Check:** Before doing any work, look at the notebook. Is the answer already there?
3.  **The Save:** If the answer wasn't there, calculate it and write it in the notebook for next time.

---

### 3. The Level-Up Guide

#### Level 0: The "Forgetful" Way
Imagine calculating the Fibonacci sequence (where the next number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8...). 
To find the 5th number, a basic computer calculates the 2nd number over and over again like a goldfish. It's very slow!

#### Level 1: The Manual Notebook
We create a variable called `memo = {}`. 
*   Key: The question (e.g., "Find the 10th Fibonacci number")
*   Value: The answer (e.g., 55)

#### Level 2: The "Ask First" Logic
```python
if n in memo:
    return memo[n] # "I already know this!"
```

#### Level 3: The Calculation & Storage
If it's not in the notebook:
```python
result = calculate_it(n)
memo[n] = result # "Write it down for later!"
return result
```

#### Level 4: The Python Shortcut
In Python, we have a "cheat code" called `@lru_cache`. It's a "Decorator" (a piece of code that wraps around our function) that automatically creates the notebook for us. It’s like hiring a personal assistant to take notes for you!

### 🐍 Full Code
