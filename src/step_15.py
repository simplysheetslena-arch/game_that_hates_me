"""STEP 15 — Ultimate Betrayal: a final secret phase after a real win."""
import tkinter as tk
import random
from step_14 import Game as PreviousGame
from step_00 import BACKGROUND, PURPLE

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 15 / PURE NIGHTMARE")
        self.secret_phase = False
        self.secret_hits = 0
        self.secret_button = tk.Button(self.root, text="END THIS", command=self.secret_click,
                                       font=("Arial", 12, "bold"), bg="#FF597C",
                                       fg=BACKGROUND, relief="flat")

    def win(self):
        # Step 06 still handles its one fake victory first.
        if not self.fake_victory_used:
            super().win()
            return
        if self.secret_phase:
            return
        self.secret_phase = True
        self.won = True
        self.stop_timer()
        self.hide_fake_buttons()
        self.button.place_forget()
        self.title_label.config(text="ONE LAST THING...")
        self.set_message("CLICK THE RED BUTTON 3 TIMES. THEN YOU'RE FREE.")
        self.secret_hits = 0
        self.move_secret()

    def move_secret(self):
        self.secret_button.place(x=random.randint(90, 730),
                                 y=random.randint(320, 470), width=140, height=45)

    def secret_click(self):
        if not self.secret_phase:
            return
        self.secret_hits += 1
        if self.secret_hits >= 3:
            self.secret_phase = False
            self.secret_button.place_forget()
            self.button.place(x=360, y=335, width=240, height=70)
            self.button.config(bg=PURPLE)
            self.title_label.config(text="YOU ACTUALLY WIN.")
            self.set_message("I HATE THAT YOU DID IT. PRESS R TO PLAY AGAIN.")
            self.button.config(text="PLAY AGAIN", command=self.reset_game)
        else:
            self.set_message(f"SECRET PHASE: {self.secret_hits}/3. NOT SO FAST.")
            self.move_secret()

    def reset_game(self):
        super().reset_game()
        self.secret_phase = False
        self.secret_hits = 0
        if hasattr(self, "secret_button"):
            self.secret_button.place_forget()

if __name__ == "__main__":
    Game().run()
