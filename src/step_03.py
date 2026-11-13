"""STEP 03 — Each successful click shrinks the real button."""

from step_02 import Game as PreviousGame


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 03")

    def on_button_click(self):
        super().on_button_click()
        if not self.won:
            # Start at 240x70, then gradually make it smaller.
            width = max(95, 240 - self.clicks * 32)
            height = max(38, 70 - self.clicks * 7)
            # Keep the center fixed until the button starts dodging.
            current_x = self.button.winfo_x()
            current_y = self.button.winfo_y()
            old_width = self.button.winfo_width()
            old_height = self.button.winfo_height()
            center_x = current_x + old_width / 2
            center_y = current_y + old_height / 2
            self.button.place_configure(
                x=int(center_x - width / 2),
                y=int(center_y - height / 2),
                width=width,
                height=height,
            )

    def reset_game(self):
        super().reset_game()  # The base game restores the original size.


if __name__ == "__main__":
    Game().run()
