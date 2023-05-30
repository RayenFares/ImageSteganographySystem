from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import subprocess

global selected_image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame4")

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

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_decoding_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui5.py"])
    window.destroy()  # Close the current interface

def open_afterenc_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui6.py"])
    window.destroy()  # Close the current interface

def handle_enter(event):
    entry_1.insert(tk.END, "\n")  # Insert a newline character when Enter is pressed

from PIL import Image
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    global selected_image
    if file_path:
        selected_image= Image.open(file_path)
        entry_3.delete(0, tk.END)  # Clear the current text in the Entry widget
        entry_3.insert(0, file_path)  # Insert the selected file path into the Entry widget

# Encryption function (for message encryption)
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + int(key)) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + int(key)) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Decryption function (for message decryption)

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

canvas.create_text(
    298.0,
    28.0,
    anchor="nw",
    text="Encoding with StegaX!",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 24 * -1)
)

canvas.create_text(
    318.0,
    74.0,
    anchor="nw",
    text="1. Write the message you want to hide",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    351.0,
    92.0,
    anchor="nw",
    text="2. Add the encryption code",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    369.0,
    110.0,
    anchor="nw",
    text="3. Choose the image",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    431.0,
    205.5,
    image=entry_image_1
)
entry_1 = tk.Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.bind("<Return>", handle_enter)
entry_1.place(
    x=308.0,
    y=167.0,
    width=246.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    431.0,
    284.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0
)

entry_2.place(
    x=308.0,
    y=268.0,
    width=246.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    431.0,
    343.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#224957",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=308.0,
    y=328.0,
    width=246.0,
    height=29.0
)

#encryption of the message
message = entry_1.get()
key = entry_2.get()
encrypted_message = encrypt(message, key)

global encoded_image
from steganography_functions import encode_lsb
def encode_photo():
    if selected_image is not None:
        message = entry_1.get()
        key = entry_2.get()
        encrypted_message = encrypt(message, key)
        global encoded_image
        # Perform encoding using the selected photo
        encoded_image = encode_lsb(selected_image,encrypted_message)


"""image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png")) 
image_2 = canvas.create_image(
    5410.0,
    344.0,
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
    y=335.0,
)
canvas.create_text(
    381.0,
    145.0,
    anchor="nw",
    text="Secret Message:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    379.0,
    246.0,
    anchor="nw",
    text="Encryption code:",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    403.0,
    306.0,
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
    command=encode_photo,
    relief="flat"
)
button_1.place(
    x=358.0,
    y=381.0,
    width=71.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= open_encoding_interface,
    relief="flat"
)
button_2.place(
    x=434.0,
    y=381.0,
    width=71.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_home_interface,
    relief="flat"
)
button_3.place(
    x=739.0,
    y=30.0,
    width=91.0,
    height=34.0
)
window.resizable(False, False)
window.mainloop()
