"""STEP 09 — Betrayal: once per round, 4 clicks becomes 2."""
from step_08 import Game as PreviousGame

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 09 / BETRAYAL")
        self.betrayed = False

    def on_button_click(self):
        before = self.clicks
        super().on_button_click()
        if not self.won and not self.betrayed and before < 4 <= self.clicks:
            self.betrayed = True
            self.clicks = 2
            self.update_progress()
            self.set_message("FOUR? I THINK YOU MEANT TWO. -2 POINTS.")

    def reset_game(self):
        super().reset_game()
        self.betrayed = False

if __name__ == "__main__":
    Game().run()
