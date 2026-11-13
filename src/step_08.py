"""STEP 08 — Endless Cursor Hunter: no dodge limit, checks mouse continuously."""
import time
from step_07 import Game as PreviousGame

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 08 / ENDLESS HUNTER")
        self.hunter_moves = 0
        self.root.after(60, self.hunter_tick)

    def hunter_tick(self):
        # The cursor does not need to move: the game keeps watching it.
        if not self.root.winfo_exists():
            return
        if not self.won and self.clicks >= 2 and not getattr(self, "math_pending", False):
            now = time.monotonic()
            x = self.root.winfo_pointerx() - self.root.winfo_rootx()
            y = self.root.winfo_pointery() - self.root.winfo_rooty()
            bx, by = self.button.winfo_x(), self.button.winfo_y()
            bw, bh = self.button.winfo_width(), self.button.winfo_height()
            if (bx - 65 <= x <= bx + bw + 65 and
                by - 55 <= y <= by + bh + 55 and
                now - self.last_dodge >= 0.12):
                self.move_button()
                self.hunter_moves += 1
                self.last_dodge = now
                self.set_message(f"STOP CHASING ME! DODGES: {self.hunter_moves}")
        self.root.after(60, self.hunter_tick)

    def on_mouse_move(self, event):
        # No cap; the periodic hunter handles dodging even for a stationary cursor.
        pass

    def reset_game(self):
        super().reset_game()
        self.hunter_moves = 0

if __name__ == "__main__":
    Game().run()
