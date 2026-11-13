"""STEP 06 — The first victory is a lie. Win again to really win."""

from step_05 import Game as PreviousGame


class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 06")
        self.fake_victory_used = False

    def win(self):
        if self.fake_victory_used:
            # Second victory is real. We're not completely evil.
            super().win()
            return

        self.fake_victory_used = True
        self.won = True  # Temporarily freezes other mechanics.
        self.stop_timer()
        self.title_label.config(text="YOU WIN! 🎉")
        self.set_message("Congratulations! You actually did it!")
        self.button.config(text="VICTORY!", state="disabled")
        self.root.after(1500, self.reveal_lie)

    def reveal_lie(self):
        # Only run if the player is still viewing the fake result.
        if not self.won or not self.fake_victory_used:
            return
        self.reset_game()
        self.set_message("JUST KIDDING. Do it again. 😈")


if __name__ == "__main__":
    Game().run()
