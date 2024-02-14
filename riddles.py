import tkinter as tk
from tkinter import simpledialog, messagebox

# Define the riddles and their possible answers
riddles_with_answers = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", ["echo"]),
    ("You measure my life in hours and I serve you by expiring. I'm quick when I'm thin and slow when I'm fat. The wind is my enemy.", ["candle"]),
    ("I walk on 4 legs in the morning, 2 legs at noon, and 3 legs in the evening. What am I?", ["human", "person", "man", "woman", "human being"]),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", ["m"]),
    ("What has keys but can't open locks?", ["piano"])
]

class RiddlesApp(tk.Tk):
    def __init__(self, riddles_with_answers):
        super().__init__()
        self.riddles_with_answers = riddles_with_answers
        self.current_riddle_index = 0
        self.score = 0
        self.title("Riddle Me This!")
        self.geometry("400x200")
        self.riddle_label = tk.Label(self, text="", wraplength=380)
        self.riddle_label.pack(pady=20)
        self.answer_entry = tk.Entry(self)
        self.answer_entry.bind("<Return>", self.check_answer)  # Bind the Return key to check the answer
        self.answer_entry.pack()
        self.next_button = tk.Button(self, text="Next", command=self.next_riddle)
        self.next_button.pack(pady=10)
        self.display_current_riddle()

    def display_current_riddle(self):
        riddle, _ = self.riddles_with_answers[self.current_riddle_index]
        self.riddle_label.config(text=riddle)
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()

    def check_answer(self, event=None):
        user_answer = self.answer_entry.get().lower().strip()
        _, possible_answers = self.riddles_with_answers[self.current_riddle_index]
        if user_answer in possible_answers:
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            messagebox.showinfo("Result", f"Wrong! A correct answer could have been: {possible_answers[0]}")
        self.next_riddle()

    def next_riddle(self):
        self.current_riddle_index += 1
        if self.current_riddle_index < len(self.riddles_with_answers):
            self.display_current_riddle()
        else:
            messagebox.showinfo("Game Over", f"Your final score is {self.score}/{len(self.riddles_with_answers)}")
            self.destroy()

if __name__ == "__main__":
    app = RiddlesApp(riddles_with_answers)
    app.mainloop()
