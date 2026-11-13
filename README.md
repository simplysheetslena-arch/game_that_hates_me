# I Created a Game That Hates Me 😈

A ridiculous 5-click game written in **Python with Tkinter**. Every step makes it worse.

**No pip installs required:** Tkinter normally comes with the official Python installer for Windows and macOS. You need Python installed (VS Code alone does not run Python).

## Run

From a terminal opened in the project folder:

```powershell
py src/step_00.py
```

If `py` doesn't work, try:

```powershell
python src/step_00.py
```

Or on Windows:

```powershell
.\run-game.bat 00
.\run-game.bat 07
```

Press **R** to restart. Close the window to quit.

## Steps

| File | What's new? |
| --- | --- |
| `src/step_00.py` | Basic 5-click game |
| `src/step_01.py` | The button runs away before the final click (only 4 dodges, so still winnable) |
| `src/step_02.py` | Toxic comments |
| `src/step_03.py` | Shrinking button |
| `src/step_04.py` | Three decoy buttons, wrong clicks cost a point |
| `src/step_05.py` | 15-second timer from first click |
| `src/step_06.py` | First win is fake; second win is real |
| `src/step_07.py` | Final boss, extra teleporting and visual flash |

### How code evolves

`step_00.py` contains the original `Game` class. Each new step **inherits from the preceding step** and adds/overrides a few methods, so every step is runnable without copying a giant codebase. This also makes the changes easy to show during a YouTube recording.

> Every step needs the preceding step files in the same `src/` folder. **Don't delete earlier steps!**

## Notes

- Game language: English (for the YouTube video).
- No additional Python packages or C++ compiler are needed.
- A normal desktop environment is required (the game opens a window).
- Publishing the source on GitHub doesn't automatically make a Python desktop game playable in a browser; distributing it to viewers requires them to run it with Python or package it into an executable.
