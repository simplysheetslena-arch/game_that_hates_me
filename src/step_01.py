"""STEP 01 — The button dodges the mouse before the fifth click.

Inherits all of step_00. Only the new mechanic is added here.
"""

import random
import time

from step_00 import Game as PreviousGame


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 01")
        self.dodges = 0
        self.last_dodge = 0.0
        self.root.bind_all("<Motion>", self.on_mouse_move)

    def on_mouse_move(self, event):
        # The button runs away only when the player has 4/5 clicks.
        if self.won or self.clicks != 4 :
            return

        now = time.monotonic()
        if now - self.last_dodge < 0.12:
            return

        mouse_x = event.x_root - self.root.winfo_rootx()
        mouse_y = event.y_root - self.root.winfo_rooty()
        button_x = self.button.winfo_x()
        button_y = self.button.winfo_y()
        width = self.button.winfo_width()
        height = self.button.winfo_height()

        nearby = (
            button_x - 28 <= mouse_x <= button_x + width + 28
            and button_y - 28 <= mouse_y <= button_y + height + 28
        )
        if nearby:
            self.move_button()
            self.dodges += 1
            self.last_dodge = now
            self.set_message(f"NOPE! Dodge #{self.dodges}. I never get tired.")

    def move_button(self):
        """Choose an on-screen position, avoiding visible fake buttons."""
        width = max(90, self.button.winfo_width())
        height = max(40, self.button.winfo_height())
        for _ in range(40):
            x = random.randint(50, 960 - width - 50)
            y = random.randint(312, 510 - height)
            if self.position_is_clear(x, y, width, height):
                self.button.place_configure(x=x, y=y)
                return

    def position_is_clear(self, x, y, width, height):
        # The next steps can override this if they need extra constraints.
        return True

    def reset_game(self):
        super().reset_game()
        self.dodges = 0
        self.last_dodge = 0.0


if __name__ == "__main__":
    Game().run()
