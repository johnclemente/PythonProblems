import tkinter as tk
from tkinter import simpledialog, messagebox

# Define the games and their possible answers
prompts_with_questions = [
    ("He looks confused. 'You alright man?' he says.", ["yes", "yeah", "yea"]),
    ("", ["no"]),
    ("eh, did't think so. Anyways--You interrupt, 'Alright man I'll be asking the questions here'", ["possible answer", "possible answer1"]),
    ("This is the first prompt", ["possible answer", "possible answer1"]),
    ("This is the first prompt", ["possible answer", "possible answer1"]),
    ("This is the first prompt", ["possible answer", "possible answer1"]),

]

class GameApp(tk.Tk):
    def __init__(self, prompts_with_questions):
        super().__init__()
        self.prompts_with_questions = prompts_with_questions
        self.current_game_index = 0
        self.score = 0
        self.title("Lost")
        self.geometry("400x400")
        self.game_label = tk.Label(self, text="", wraplength=380)
        self.game_label.pack(pady=20)
        self.answer_entry = tk.Entry(self)
        self.answer_entry.bind("<Return>", self.check_answer)  # Bind the Return key to check the answer
        self.answer_entry.pack()
        # self.next_button = tk.Button(self, text="Next", command=self.next_prompt)
        # self.next_button.pack(pady=10)
        self.display_current_prompt()
        # self.display_current_feedback()

    def display_current_prompt(self):
        game, _ = self.prompts_with_questions[self.current_game_index]
        self.game_label.config(text=game)
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()

    def check_answer(self, event=None):
        user_answer = self.answer_entry.get().lower().strip()
        _, possible_answers = self.prompts_with_questions[self.current_game_index]
        if user_answer in possible_answers:
            # messagebox.showinfo("Result", "Correct!")
            self.score += 1
            self.next_prompt()
        else:
            # TODO: give UI feedback that answer was wrong
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.focus()


    def next_prompt(self):
        self.current_game_index += 1
        if self.current_game_index < len(self.prompts_with_questions):
            self.display_current_prompt()
        else:
            messagebox.showinfo("Game Over", f"Your final score is {self.score}/{len(self.prompts_with_questions)}")
            self.destroy()

if __name__ == "__main__":
    app = GameApp(prompts_with_questions)
    app.mainloop()
