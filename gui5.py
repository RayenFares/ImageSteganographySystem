
from pathlib import Path
import tkinter as tk
from global_variables import selected_image

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\assets\frame5")

def open_login_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui.py"])
    window.destroy()  # Close the current interface

def open_encoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui4.py"])
    window.destroy()  # Close the current interface

def open_decoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui5.py"])
    window.destroy()  # Close the current interface

def handle_enter(event):
    entry_1.insert(tk.END, "\n")  # Insert a newline character when Enter is pressed

def open_file_dialog():
    global selected_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        selected_image = file_path
        entry_1.delete(0, tk.END)  # Clear the current text in the Entry widget
        entry_1.insert(0, selected_image)  # Insert the selected file path into the Entry widget

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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

canvas.create_text(
    296.0,
    28.0,
    anchor="nw",
    text="Decoding with StegaX!",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 24 * -1)
)

canvas.create_text(
    339.0,
    74.0,
    anchor="nw",
    text="1. Choose the Encrypted image",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    361.0,
    92.0,
    anchor="nw",
    text="2. Decode the message",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    431.0,
    166.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=308.0,
    y=148.0,
    width=246.0,
    height=35.0
)

"""image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    541.0,
    167.0,
    image=image_image_2
)"""

button_image_locate = PhotoImage(
    file=relative_to_assets("image_2.png"))
button_locate = Button(
    image=button_image_locate,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_dialog,
)

button_locate.place(
    x=541.0,
    y=158.0,
)

canvas.create_text(
    404.0,
    126.0,
    anchor="nw",
    text="Locate ...",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_login_interface,
    relief="flat"
)
button_1.place(
    x=739.0,
    y=30.0,
    width=91.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=358.0,
    y=193.0,
    width=71.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_decoding_interface,
    relief="flat"
)
button_3.place(
    x=434.0,
    y=193.0,
    width=71.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
