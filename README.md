# Riddle Game

Welcome to the Riddle Game! This Python script challenges users with a series of riddles. The user has to provide answers, and the script checks if the provided answers are correct. It's a fun and interactive way to test your riddle-solving skills.

## Features

- A set of predefined riddles with multiple possible correct answers.
- A scoring system to keep track of correct answers.

## Usage

To run the riddle game, simply execute the script in a Python environment. The script will present each riddle, wait for the user's answer, and then provide feedback on whether the answer is correct or not.

### Example

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

## Contributing

I welcome contributions to enhance the Riddle Game! Here are some guidelines to help you get started:

Adding New Riddles

Define the riddle: Add your new riddle and its possible answers to the riddles_with_answers list.

```python
riddles_with_answers.append(
    ("Your riddle here?", ["correct", "answers", "comma", "separated"])
)
```

Please make sure the format: Make sure your riddle follows the same format as the existing ones.

## Desired features

- GUI: Develop a visually appealing GUI using frameworks like Tkinter, PyQt, or web-based interfaces with Flask/Django.
- Responsive Design: Ensure the game can be played on various devices, including desktops, tablets, and smartphones.
- Multiplayer: the ability to play with friends online.

