"""STEP 07 — Final boss: all mechanics, plus teleport + screen flash."""

import random

from step_06 import Game as PreviousGame
from step_00 import BACKGROUND


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="FINAL BOSS")
        self.root.title("I Created a Game That HATES Me — FINAL BOSS")
        self.flash_job = None

    def on_button_click(self):
        super().on_button_click()
        if self.won:
            return

        # Extra chaos: the real button teleports after almost every click.
        if self.clicks >= 2:
            self.move_button()
            self.set_message(random.choice([
                "Why are you still here?",
                "I have moved. You have not improved.",
                "Catch me if you can.",
                "Five clicks. Should be simple. Right?",
            ]))

        # Quick visual flash makes the interface feel angry.
        self.root.configure(bg="#362142")
        if self.flash_job is not None:
            self.root.after_cancel(self.flash_job)
        self.flash_job = self.root.after(140, self.end_flash)

    def end_flash(self):
        self.root.configure(bg=BACKGROUND)
        self.flash_job = None

    def reset_game(self):
        if hasattr(self, "flash_job") and self.flash_job is not None:
            self.root.after_cancel(self.flash_job)
            self.flash_job = None
        super().reset_game()
        self.root.configure(bg=BACKGROUND)


if __name__ == "__main__":
    Game().run()
