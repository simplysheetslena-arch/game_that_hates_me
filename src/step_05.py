"""STEP 05 — You now have 15 seconds from the first click."""

import time
import tkinter as tk

from step_04 import Game as PreviousGame
from step_00 import BACKGROUND, FOREGROUND

TIME_LIMIT = 15.0


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 05")
        self.deadline = None
        self.timer_job = None
        self.timer_label = tk.Label(
            self.root, text="TIMER: READY", font=("Arial", 13, "bold"),
            fg=FOREGROUND, bg=BACKGROUND
        )
        self.timer_label.place(x=0, y=528, width=960)

    def on_button_click(self):
        if not self.won and self.clicks == 0 and self.deadline is None:
            self.deadline = time.monotonic() + TIME_LIMIT
            self.update_timer()
        super().on_button_click()
        if self.won:
            self.stop_timer()
            self.timer_label.config(text="TIMER: STOPPED")

    def update_timer(self):
        if self.deadline is None or self.won:
            return
        left = max(0.0, self.deadline - time.monotonic())
        self.timer_label.config(text=f"TIME LEFT: {left:04.1f}s")
        if left <= 0.0:
            self.reset_game()
            self.set_message("TIME'S UP. Back to zero. How tragic.")
        else:
            self.timer_job = self.root.after(100, self.update_timer)

    def stop_timer(self):
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.deadline = None

    def reset_game(self):
        # On a fresh playthrough there is no active timer yet.
        if hasattr(self, "timer_job"):
            self.stop_timer()
        super().reset_game()
        if hasattr(self, "timer_label"):
            self.timer_label.config(text="TIMER: READY")


if __name__ == "__main__":
    Game().run()
