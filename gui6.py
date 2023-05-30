from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import subprocess
from global_variables import selected_image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame6")


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

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        # Save the image to the selected file path
        image.save(file_path)

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
    298.0,
    28.0,
    anchor="nw",
    text="Encoding with StegaX!",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 24 * -1)
)

canvas.create_text(
    343.0,
    74.0,
    anchor="nw",
    text="Image Successfully encoded!",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_rectangle(
    114.0,
    148.0,
    384.0,
    326.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    479.0,
    148.0,
    749.0,
    326.0,
    fill="",
    outline="")
image = PhotoImage(file=selected_image)
canvas.create_image(479.0, 148.0, anchor="nw", image=image)

canvas.create_text(
    196.0,
    331.0,
    anchor="nw",
    text="Original Image",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    561.0,
    331.0,
    anchor="nw",
    text="Encrypted Image",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=save_image,
    relief="flat"
)
button_1.place(
    x=320.0,
    y=377.0,
    width=71.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_decoding_interface,
    relief="flat"
)
button_2.place(
    x=396.0,
    y=377.0,
    width=71.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=472.0,
    y=377.0,
    width=71.0,
    height=23.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_login_interface,
    relief="flat"
)
button_4.place(
    x=748.0,
    y=29.0,
    width=91.0,
    height=34.0
)
window.resizable(False, False)
window.mainloop()
