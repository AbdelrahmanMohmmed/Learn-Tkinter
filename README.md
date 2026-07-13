# Learn Tkinter

A beginner-friendly collection of small Python Tkinter GUI examples.

## What is in this repository

This project contains standalone scripts that each demonstrate a different Tkinter concept:

- `create_window.py` — create and configure a basic window.
- `add_label.py` — add labels with custom font, color, border, and image.
- `clock_tk.py` — digital clock with live time/date updates.
- `calculator.py` — simple calculator UI with button input and expression evaluation.
- `moveObject_tk.py` — drag and drop objects with the mouse.
- `moveUsingkeyboard_tk.py` — move an image with keyboard controls (`W`, `A`, `S`, `D`).
- `textEditer_tk.py` — basic text editor with open/save, edit actions, and font/color controls.

## Prerequisites

- Python 3.8+ (recommended)
- Tkinter support enabled in your Python installation

> On most systems Tkinter is included by default.  
> Linux users may need to install it separately (for example: `python3-tk` on Debian/Ubuntu).

## How to run

From the repository root:

```bash
python create_window.py
```

Replace `create_window.py` with any script you want to try.

## Assets

The `images/` folder stores image assets used by the GUI examples:

- `images/logo.png`
- `images/logo.ico`

## Notes

- Each script is independent and can be run on its own.
- These examples are intentionally simple for learning and experimentation.

## Suggested next improvements

- Add unit-testable logic by separating UI code from pure functions.
- Add script screenshots/GIFs to make examples easier to preview.
- Add packaging (`pyproject.toml`) and task commands for linting/testing.
