"""STEP 04 — Decoy buttons appear. Clicking one costs a point."""

import tkinter as tk

from step_03 import Game as PreviousGame
from step_00 import BACKGROUND, PURPLE


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 04")
        self.fake_buttons = []
        for _ in range(3):
            fake = tk.Button(
                self.root, text="CLICK ME", command=self.on_fake_click,
                font=("Arial", 13, "bold"), fg=BACKGROUND, bg=PURPLE,
                activeforeground=BACKGROUND, activebackground="#8065E8",
                relief="flat", bd=0, cursor="hand2"
            )
            self.fake_buttons.append(fake)

    def show_fake_buttons(self):
        positions = [(78, 344), (674, 344), (385, 428)]
        for fake, (x, y) in zip(self.fake_buttons, positions):
            fake.place(x=x, y=y, width=165, height=50)
            # Put the real button above any overlapping decoy.
            self.button.lift()

    def hide_fake_buttons(self):
        for fake in self.fake_buttons:
            fake.place_forget()

    def on_button_click(self):
        super().on_button_click()
        if not self.won and self.clicks >= 2:
            self.show_fake_buttons()
        elif self.won:
            self.hide_fake_buttons()

    def on_fake_click(self):
        if self.won:
            return
        self.clicks = max(0, self.clicks - 1)
        self.update_progress()
        self.set_message("WRONG BUTTON. Minus one click. LOL.")
        if self.clicks < 2:
            self.hide_fake_buttons()

    def position_is_clear(self, x, y, width, height):
        if not hasattr(self, "fake_buttons"):
            return True
        for fake in self.fake_buttons:
            if not fake.winfo_manager():
                continue
            fx, fy = fake.winfo_x(), fake.winfo_y()
            fw, fh = fake.winfo_width(), fake.winfo_height()
            if x < fx + fw + 15 and x + width + 15 > fx and y < fy + fh + 15 and y + height + 15 > fy:
                return False
        return True

    def reset_game(self):
        super().reset_game()
        if hasattr(self, "fake_buttons"):
            self.hide_fake_buttons()


if __name__ == "__main__":
    Game().run()
