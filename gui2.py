
from pathlib import Path
import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame2")

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_login_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    command= open_login_interface,
    relief="flat"
)
button_1.place(
    x=303.0,
    y=328.0,
    width=256.0,
    height=34.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    431.5,
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
    x=314.0,
    y=214.0,
    width=235.0,
    height=34.0
)

canvas.create_text(
    398.0,
    190.0,
    anchor="nw",
    text="Username:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    431.5,
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
    x=314.0,
    y=276.0,
    width=235.0,
    height=34.0
)

canvas.create_text(
    400.0,
    255.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    272.0,
    136.0,
    anchor="nw",
    text="Welcome to StegaX, Register now and start your trial!",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    312.0,
    153.0,
    anchor="nw",
    text="or login if you already have an account!",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    302.0,
    72.0,
    anchor="nw",
    text="Register Now",
    fill="#FFFFFF",
    font=("Poppins Regular", 40 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= open_home_interface,
    relief="flat"
)
button_2.place(
    x=745.0,
    y=30.0,
    width=91.0,
    height=34.0
)
window.resizable(False, False)
window.mainloop()
