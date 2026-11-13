"""STEP 10 — Invisible Menace: the button fades near the cursor, but returns."""
import time
from step_09 import Game as PreviousGame
from step_00 import PURPLE, BACKGROUND

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 10 / INVISIBLE MENACE")
        self.hidden_until = 0.0
        self.root.after(80, self.visibility_tick)

    def on_mouse_move(self, event):
        super().on_mouse_move(event)
        if self.won or self.clicks < 3:
            return
        x = event.x_root - self.root.winfo_rootx()
        y = event.y_root - self.root.winfo_rooty()
        bx, by = self.button.winfo_x(), self.button.winfo_y()
        bw, bh = self.button.winfo_width(), self.button.winfo_height()
        if bx - 40 <= x <= bx + bw + 40 and by - 40 <= y <= by + bh + 40:
            self.hidden_until = time.monotonic() + 0.45

    def visibility_tick(self):
        if not self.root.winfo_exists():
            return
        hidden = not self.won and self.clicks >= 3 and time.monotonic() < self.hidden_until
        self.button.config(bg=BACKGROUND if hidden else PURPLE,
                           activebackground=BACKGROUND if hidden else PURPLE,
                           fg=BACKGROUND)
        self.root.after(80, self.visibility_tick)

    def reset_game(self):
        super().reset_game()
        self.hidden_until = 0.0
        self.button.config(bg=PURPLE, activebackground=PURPLE)

if __name__ == "__main__":
    Game().run()
