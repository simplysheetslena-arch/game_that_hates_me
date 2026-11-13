"""STEP 13 — Math Gate: solve a short equation before clicks count."""
import random
import tkinter as tk
from step_12 import Game as PreviousGame
from step_00 import BACKGROUND, FOREGROUND, PURPLE

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 13 / MATH GATE")
        self.math_answer = None
        self.math_pending = False
        self.math_panel = tk.Frame(self.root, bg="#302742")
        self.math_question = tk.Label(self.math_panel, fg=FOREGROUND,
                                      bg="#302742", font=("Arial", 14, "bold"))
        self.math_question.pack(pady=8)
        self.math_entry = tk.Entry(self.math_panel, justify="center", width=12,
                                   font=("Arial", 13))
        self.math_entry.pack()
        tk.Button(self.math_panel, text="SUBMIT", command=self.submit_math,
                  bg=PURPLE, fg=BACKGROUND).pack(pady=8)
        self.math_entry.bind("<Return>", lambda event: self.submit_math())

    def on_button_click(self):
        if self.won or self.math_pending:
            return
        a, b = random.randint(4, 19), random.randint(3, 15)
        self.math_answer = a+b
        self.math_pending = True
        self.math_question.config(text=f"PROVE YOU'RE HUMAN: {a} + {b} = ?")
        self.math_entry.delete(0, "end")
        self.math_panel.place(x=325, y=70, width=310, height=140)
        self.math_entry.focus_set()

    def submit_math(self):
        if not self.math_pending:
            return
        try:
            correct = int(self.math_entry.get().strip()) == self.math_answer
        except ValueError:
            correct = False
        self.math_pending = False
        self.math_panel.place_forget()
        if correct:
            super().on_button_click()
        else:
            self.clicks = max(0, self.clicks-1)
            self.update_progress()
            self.set_message("WRONG ANSWER. -1 CLICK. AMAZING.")

    def reset_game(self):
        super().reset_game()
        self.math_pending = False
        if hasattr(self, "math_panel"):
            self.math_panel.place_forget()

if __name__ == "__main__":
    Game().run()
