# StegaX - Image Steganography System

StegaX is a Python-based Image Steganography System that allows you to hide secret messages within images using the LSB (Least Significant Bit) technique. It provides an intuitive graphical user interface (GUI) for encoding and decoding messages into images.

## Overview

Steganography is the practice of concealing secret information within another medium to prevent unauthorized access. In the case of image steganography, secret messages are embedded into the pixels of an image, making them imperceptible to the human eye.

StegaX offers a simple and user-friendly way to perform image steganography, making it accessible to both beginners and experienced users. With StegaX, you can securely hide confidential information within images and share them without arousing suspicion.

## Features

- Hide secret messages within images
- Encrypt messages using a user-defined encryption key
- Intuitive and user-friendly GUI
- Support for popular image formats (PNG, JPG, JPEG)
- LSB-based encoding and decoding technique

## Requirements

- Python 3.x
- Tkinter: Python's standard GUI library for creating graphical user interfaces.
- Pillow: A powerful library for handling images in Python, used for image manipulation and processing.
- Pathlib: Provides an object-oriented approach to working with file paths.
- subprocess: Provides a way to spawn new processes, in this case, used to open other Python scripts.
- sqlite3: Provides an interface to the SQLite database engine, used for database operations.
- bcrypt: A password-hashing library used for securely hashing and verifying passwords.

## Files
- Project- Report.pdf           -- represents the final project report in pdf format
- gui2.py                       -- represents the registration interface
- gui.py                        -- represents the login interface 
- gui3.py                       -- represents the home interface
- gui4.py                       -- represents the encoding interface
- gui5.py                       -- represents the decoding interface
- assets                        -- represents the file that contains all assets needed (images)
- steganography_functions.py    -- represents the functions of encoding decoding using LSB algorithm


## Installation

1. Clone the repository:

```shell
git clone [https://github.com/your-username/stegaX.git](https://github.com/RayenFares/ImageSteganographySystem)
```

## Usage

1- Run the GUI application: gui2.py
2- Register to create an account
3- Login with your username and password
4- Choose the desired operation (encoding or decoding) from the main menu.
  For encoding:
    a. Enter the secret message to hide.
    b. Provide an encryption key for message encryption.
    c. Select the cover image (the image in which you want to hide the message).
    d. Click the "Encode" button to generate the encoded image.
    e. The image is saved on your desktop labled 'encoded_image'
    f. Share the encoded_image + the encryption key in a secure communication channel with the receiver
  For decoding:
    a. Select the encoded image (the image that contains the hidden message 'encoded_image').
    b. Enter the encryption key used during encoding.
    c. Click the "Decode" button to retrieve the hidden message.
    
## Acknowledgements

The Image Steganography System (StegaX) was developed as part of a project for the Information Assurance and Security Course(IT 360) by Rayen Fares, Aziz Srairi, Imen Cherif, Takwa karaoud.
We would like to express our sincere gratitude to our professor, Manel Abdelkader, for her invaluable guidance, expertise, and unwavering support throughout the duration of the IT 360 Course. 
