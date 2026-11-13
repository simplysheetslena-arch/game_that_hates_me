"""STEP 12 — Mouse Trap: red hazard zones punish cursor contact."""
import tkinter as tk
import time
from step_11 import Game as PreviousGame
from step_00 import BACKGROUND

class Game(PreviousGame):
    def __init__(self):
        super().__init__()
        self.level_label.config(text="STEP 12 / MOUSE TRAP")
        self.trap_cooldown = 0.0
        self.traps = []
        for x, y, w, h in [(275,320,55,120),(620,330,45,125),(455,435,60,40)]:
            t = tk.Label(self.root, text="!", fg="white", bg="#9D243A",
                         font=("Arial", 15, "bold"))
            self.traps.append((t,x,y,w,h))
        self.root.bind_all("<Motion>", self.check_traps, add="+")
        self.root.after(100, self.trap_tick)

    def trap_tick(self):
        if not self.root.winfo_exists():
            return
        for t,x,y,w,h in self.traps:
            if self.won or self.clicks < 2:
                t.place_forget()
            else:
                t.place(x=x,y=y,width=w,height=h)
        self.root.after(100, self.trap_tick)

    def check_traps(self, event):
        if self.won or self.clicks < 2 or time.monotonic() < self.trap_cooldown:
            return
        x = event.x_root - self.root.winfo_rootx()
        y = event.y_root - self.root.winfo_rooty()
        for _,tx,ty,tw,th in self.traps:
            if tx <= x <= tx+tw and ty <= y <= ty+th:
                self.trap_cooldown = time.monotonic() + 1.0
                self.clicks = max(0, self.clicks-2)
                self.update_progress()
                self.set_message("TRAP! -2 CLICKS. WATCH YOUR MOUSE.")
                break

    def reset_game(self):
        super().reset_game()
        self.trap_cooldown = time.monotonic() + 0.5

if __name__ == "__main__":
    Game().run()
