"""STEP 14 — Rage Mode: the timer gets shorter and the button teleports."""
import time
from step_13 import Game as PreviousGame

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 14 / RAGE MODE")
        self.rage_started = False

    def submit_math(self):
        before = self.clicks
        super().submit_math()
        if not self.won and self.clicks > before and self.clicks >= 3:
            self.move_button()
            self.set_message("RAGE MODE: NO REST FOR YOU.")
            if self.deadline is not None and not self.rage_started:
                self.deadline = min(self.deadline, time.monotonic() + 9.0)
                self.rage_started = True

    def reset_game(self):
        super().reset_game()
        self.rage_started = False

if __name__ == "__main__":
    Game().run()
