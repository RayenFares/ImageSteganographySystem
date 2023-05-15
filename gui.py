

from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

window = tk.Tk()

window.geometry("862x519")
window.configure(bg = "#093545")


canvas = Canvas(
    window,
    bg = "#093545",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    438.0,
    474.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= open_home_interface,
    relief="flat"
)
button_1.place(
    x=300.0000000000001,
    y=328.0,
    width=256.0,
    height=34.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    428.5000000000001,
    232.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=311.0000000000001,
    y=214.0,
    width=235.0,
    height=34.0
)

canvas.create_text(
    407.0000000000001,
    190.0,
    anchor="nw",
    text="Login:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    428.5000000000001,
    294.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=311.0000000000001,
    y=276.0,
    width=235.0,
    height=34.0
)

canvas.create_text(
    397.0000000000001,
    255.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    250.0000000000001,
    164.0,
    anchor="nw",
    text="Welcome to StegaX, login to your account in order to access",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    364.0000000000001,
    101.0,
    anchor="nw",
    text="Sign in",
    fill="#FFFFFF",
    font=("Poppins Regular", 40 * -1)
)
window.resizable(False, False)
window.mainloop()
