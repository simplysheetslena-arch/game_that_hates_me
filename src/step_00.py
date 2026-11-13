"""STEP 00 — The innocent button. Five clicks to win.

Run from the project root: python src/step_00.py
No external libraries needed: tkinter is included in most Python installs.
"""

import tkinter as tk

BACKGROUND = "#171825"
FOREGROUND = "#F5F2FF"
MUTED = "#A5A5BB"
PURPLE = "#AA93FF"
PURPLE_DARK = "#8065E8"


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("I Created a Game That Hates Me")
        self.root.geometry("960x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        self.clicks = 0
        self.won = False

        tk.Label(
            self.root, text="THE GAME THAT HATES YOU",
            font=("Arial", 12, "bold"), fg=PURPLE, bg=BACKGROUND
        ).place(x=32, y=25)

        self.level_label = tk.Label(
            self.root, text="STEP 00", font=("Arial", 11, "bold"),
            fg=MUTED, bg=BACKGROUND
        )
        self.level_label.place(x=858, y=25)

        self.title_label = tk.Label(
            self.root, text="Can you click a button?",
            font=("Arial", 30, "bold"), fg=FOREGROUND, bg=BACKGROUND
        )
        self.title_label.place(x=0, y=125, width=960)

        tk.Label(
            self.root, text="Just click it 5 times. Easy, right?",
            font=("Arial", 14), fg=MUTED, bg=BACKGROUND
        ).place(x=0, y=195, width=960)

        self.progress_label = tk.Label(
            self.root, font=("Arial", 16, "bold"), fg=PURPLE, bg=BACKGROUND
        )
        self.progress_label.place(x=0, y=265, width=960)

        self.button = tk.Button(
            self.root, text="CLICK ME", command=self.on_button_click,
            font=("Arial", 17, "bold"), fg=BACKGROUND, bg=PURPLE,
            activeforeground=BACKGROUND, activebackground=PURPLE_DARK,
            relief="flat", bd=0, cursor="hand2"
        )
        self.button.place(x=360, y=335, width=240, height=70)

        self.message_label = tk.Label(
            self.root, font=("Arial", 13), fg=MUTED, bg=BACKGROUND
        )
        self.message_label.place(x=0, y=470, width=960)

        tk.Label(
            self.root, text="R = restart     •     Close the window to quit",
            font=("Arial", 10), fg="#77778E", bg=BACKGROUND
        ).place(x=0, y=564, width=960)

        self.root.bind("<r>", lambda event: self.reset_game())
        self.root.bind("<R>", lambda event: self.reset_game())
        self.update_progress()
        self.set_message("Go ahead. This is literally impossible to lose.")

    def update_progress(self):
        dots = " ".join("●" if i < self.clicks else "○" for i in range(5))
        self.progress_label.config(text=f"{dots}      {self.clicks}/5")

    def set_message(self, text):
        self.message_label.config(text=text)

    def on_button_click(self):
        if self.won:
            return
        self.clicks += 1
        self.update_progress()
        if self.clicks >= 5:
            self.win()
        else:
            self.set_message("Nice. Keep clicking.")

    def win(self):
        self.won = True
        self.title_label.config(text="YOU WIN!")
        self.set_message("That was easy. Suspiciously easy.")
        self.button.config(text="PLAY AGAIN", command=self.reset_game)

    def reset_game(self):
        self.clicks = 0
        self.won = False
        self.title_label.config(text="Can you click a button?")
        self.button.config(text="CLICK ME", command=self.on_button_click, state="normal")
        self.button.place(x=360, y=335, width=240, height=70)
        self.update_progress()
        self.set_message("Go ahead. This is literally impossible to lose.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Game().run()
