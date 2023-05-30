from pathlib import Path
import tkinter as tk
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sqlite3
import bcrypt


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\PycharmProjects\StegaX\ImageSteganographySystem\assets\frame2")
#database creation
# Connect to the database
connection = sqlite3.connect('database.db')
# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)''')

#Registration for new user
def register():
    username = entry_1.get()
    password = entry_2.get()

    canvas.itemconfig(error_text, text="")  # Clear previous error messages
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)

    # Encrypt the password
    hashed_password = bcrypt.hashpw ( password.encode (), bcrypt.gensalt () )
    # Check if the username already exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result[0] > 0:
        canvas.itemconfig(error_text, text="Username already exists. Please choose a different username.")
        return

    # Check the length of the password
    if len(password) <= 8:
        canvas.itemconfig(error_text, text="Password should be more than 8 characters long.")
        return

    # Check if the password contains only alphanumeric characters and symbols
    if not match ( r'^[a-zA-Z0-9\S]+$', password ) :
        canvas.itemconfig ( error_text, text = "Password should be composed of alphanumeric and other symbols." )
        return

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    connection.commit()
    canvas.itemconfig(success_text, text="Registration successful.")

    open_login_interface()

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
#error text defintion
# Create the error text widget
error_text = canvas.create_text(
    272.0,
    400.0,
    anchor="nw",
    fill="#FF0000",
    font=("Poppins Regular", 12 * -1)
)
success_text = canvas.create_text(
    272.0,
    400.0,
    anchor="nw",
    fill="#00FF00",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= register,
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
    command= open_login_interface,
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
