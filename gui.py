
from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame0")
# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_home_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui3.py"])
    window.destroy()  # Close the current interface

def open_register_interface():
    window.withdraw()  # Hide the current interface
    # ... Save any necessary data ...
    subprocess.Popen(["python", "gui2.py"])
    window.destroy()  # Close the current interface

#Authentication
def authenticate():
    username = entry_1.get()
    password = entry_2.get()

    canvas.itemconfig(error_text, text="")  # Clear previous error messages
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)

    # Query the database to check if the credentials are correct
    cursor.execute("SELECT COUNT(*) FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    count = result[0]

    if count > 0:
        # Authentication successful, open the home page
        open_home_interface()
    else:
        # Authentication failed, show an error message
        canvas.itemconfig(error_text, text="Incorrect username or password")

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

'''
# Retrieve the users and their passwords from the database
cursor.execute("SELECT username, password FROM users")
users = cursor.fetchall()
for user in users:
    username, password = user
    print("Username:", username)
    print("Password:", password)
    print()
#delete all of the users
cursor.execute("DELETE FROM users")
connection.commit()
'''

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    438.0,
    474.0,
    image=image_image_1
)

# Create the error text widget
error_text = canvas.create_text(
    320.0,
    380.0,
    anchor="nw",
    fill="#FF0000",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= authenticate,
    relief="flat"
)
button_1.place(
    x=300.0000000000001,
    y=328.0,
    width=256.0,
    height=34.0
)
#We Realized that we need a register button in the login page
button_image = PhotoImage(
    file=relative_to_assets("Button.png"))
button = tk.Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command= open_register_interface,
    relief="flat"
)
button.place(
    x=745.0,
    y=30.0,
    width=91.0,
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
