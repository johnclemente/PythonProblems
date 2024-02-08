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
