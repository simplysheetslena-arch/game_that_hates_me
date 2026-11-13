"""STEP 02 — The game now insults your clicking skills."""

from step_01 import Game as PreviousGame

TOXIC_LINES = [
    "Oh wow. You found the mouse.",
    "Impressive. For a potato.",
    "My grandma clicks faster than that.",
    "Four clicks? Don't get cocky.",
]


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 02")

    def on_button_click(self):
        super().on_button_click()
        if not self.won and 1 <= self.clicks <= 4:
            self.set_message(TOXIC_LINES[self.clicks - 1])


if __name__ == "__main__":
    Game().run()
