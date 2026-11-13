"""STEP 11 — Clone Army 2.0: EVERY button moves, and the real one changes slot.

All buttons have identical size and appearance while the army is active.
They constantly shuffle across the same grid; no fixed correct position.
"""
import random
import tkinter as tk
from step_10 import Game as PreviousGame
from step_00 import BACKGROUND, PURPLE

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 11 / MOVING CLONE ARMY")
        self.clones = []
        for _ in range(18):
            b = tk.Button(self.root, text="CLICK ME", command=self.on_fake_click,
                          font=("Arial", 9, "bold"), fg=BACKGROUND, bg=PURPLE,
                          activeforeground=BACKGROUND, activebackground="#8065E8",
                          relief="flat", bd=0, cursor="hand2")
            self.clones.append(b)
        self.army_active = False
        self.root.after(260, self.army_tick)

    def all_decoys(self):
        return self.fake_buttons + self.clones

    def show_fake_buttons(self):
        # Do not place any decoy at a fixed coordinate.
        if not hasattr(self, "clones"):
            return
        self.army_active = True
        self.shuffle_army()

    def shuffle_army(self):
        # 28 possible non-overlapping slots for 22 decoys + one real button.
        # Shuffle every time: the correct button has NO fixed location.
        slots = [(35 + col * 127, 308 + row * 51)
                 for row in range(4) for col in range(7)]
        random.shuffle(slots)
        widgets = [self.button] + self.all_decoys()
        random.shuffle(widgets)
        for widget, (x, y) in zip(widgets, slots):
            widget.place(x=x, y=y, width=96, height=36)
            widget.config(font=("Arial", 9, "bold"))
        # The original real button is not lifted: it looks like any other clone.

    def army_tick(self):
        if not self.root.winfo_exists():
            return
        if (getattr(self, "army_active", False) and not self.won and
            self.clicks >= 2 and not getattr(self, "math_pending", False)):
            self.shuffle_army()
        self.root.after(260, self.army_tick)

    def hide_fake_buttons(self):
        self.army_active = False
        for b in getattr(self, "fake_buttons", []) + getattr(self, "clones", []):
            b.place_forget()

    def position_is_clear(self, x, y, width, height):
        # The army shuffles everyone to independent, non-overlapping slots.
        return True

    def reset_game(self):
        super().reset_game()
        self.army_active = False
        for b in getattr(self, "clones", []):
            b.place_forget()
        # Reset original size/font after an army round.
        self.button.config(font=("Arial", 17, "bold"))

if __name__ == "__main__":
    Game().run()
