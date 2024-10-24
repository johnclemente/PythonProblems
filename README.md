# General catch-all python repo

This repo is for python scripts I find interesting. It includes text-based games I’ve experimented with, as well as a problems folder dedicated to LeetCode-style problems that I find particularly interesting and enjoyable to solve.

## Problems

### triangle.py

You are given an integer n representing the number of rows in a triangle. Implement a function that prints a right-aligned triangle pattern using spaces and the character 'x'.

Each row of the triangle should contain the appropriate number of leading spaces followed by the character 'x' repeated according to the row number.

The pattern should look like this:

```Python
       x
      x x
     x x x
    x x x x
   x x x x x
```

Function Signature

```python
def triangle(n: int) -> None:
```

Input:

```python
n (1 ≤ n ≤ 100): An integer representing the number of rows in the triangle.
```

<br>
<br>

### square.py

You are given an integer n representing the length of one side of the square. Implement a function that prints an empty square pattern using spaces and the character 'x'.

I found this one on youtube shorts and had to try XD

The pattern should look like this:

```Python
x x x
x   x
x x x
```

Function Signature

```python
def square(n: int) -> None:
```

Input:

```python
n (1 ≤ n ≤ 100): An integer representing the length of one side of the square.
```

<br>
<br>
<br>
<br>

## Game Idea

```python
# Define the riddles and their possible answers
riddles_with_answers = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", ["echo"]),
    ("You measure my life in hours and I serve you by expiring. I'm quick when I'm thin and slow when I'm fat. The wind is my enemy.", ["candle"]),
    ("I walk on 4 legs in the morning, 2 legs at noon, and 3 legs in the evening. What am I?", ["human", "person", "man", "woman", "human being"]),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", ["m"]),
    ("What has keys but can't open locks?", ["piano"])
]

def ask_riddles(riddles_with_answers):
    score = 0
    for riddle, possible_answers in riddles_with_answers:
        print(riddle)
        user_answer = input("Your answer: ").lower().strip()
        if user_answer in possible_answers:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! A correct answer could have been: {possible_answers[0]}")
        print()  # New line for readability

    print(f"Your final score is {score}/{len(riddles_with_answers)}")

ask_riddles(riddles_with_answers)
```
