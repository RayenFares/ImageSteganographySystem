# -*- coding: utf-8 -*-
"""Steganography functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f9fV8siQEhDz5MVJY__bVd09Ten4X4tB
"""

from PIL import Image
import string
import numpy as np
import os

def encode_lsb(image, message):
    # Convert the image to a numpy array for ease of manipulation
    image_array = np.array(image)

    # Flatten the message into a binary string
    binary_message = ''.join(format(ord(i), '08b') for i in message)

    # Check if the message can fit within the image
    if len(binary_message) > image_array.size * 3:
        raise ValueError('Message too large to encode in image')
        
    # Resize the image if necessary
    if len(binary_message) > image_array.size:
        width = int(np.ceil(len(binary_message) / image_array.shape[1]))
        resized_image = image.resize((width, image_array.shape[1]))
        image_array = np.array(resized_image)

    # Iterate through the image pixel by pixel, encoding the message into the least significant bit of each color channel
    binary_message_index = 0
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):
                if binary_message_index >= len(binary_message):
                    break
                image_array[i, j, k] = (image_array[i, j, k] & ~1) | int(binary_message[binary_message_index])
                binary_message_index += 1
            if binary_message_index >= len(binary_message):
                break
        if binary_message_index >= len(binary_message):
            break

    # Convert the numpy array back to a Pillow image and save it
    encoded_image = Image.fromarray(image_array)
    if encoded_image is not None:
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        # Save the encoded image on the desktop
        encoded_image_path = os.path.join(desktop_path, 'encoded_image.png')
        encoded_image.save(encoded_image_path)
        print("Encoded image saved successfully.")


def decode_lsb(image_path):
    # Load the image using Pillow
    image = Image.open(image_path)

    # Convert the image to a numpy array for ease of manipulation
    image_array = np.array(image)

    # Extract the least significant bit from each color channel of each pixel to reconstruct the binary message
    binary_message = ''
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):
                binary_message += str(image_array[i, j, k] & 1)

    # Find the index of the null character in the binary message
    null_index = binary_message.find('00000000')

    # Retrieve the binary message before the null character
    message_binary = binary_message[:null_index]

    # Split the binary message into 8-bit chunks and convert each chunk to a character using the chr function
    message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i+8]
        message += chr(int(byte, 2))

    return messagedef decode_lsb(image_path):
    # Load the image using Pillow
    image = Image.open(image_path)

    # Convert the image to a numpy array for ease of manipulation
    image_array = np.array(image)

    # Extract the least significant bit from each color channel of each pixel to reconstruct the binary message
    binary_message = ''
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):
                binary_message += str(image_array[i, j, k] & 1)

    # Find the index of the null character in the binary message
    null_index = binary_message.find('00000000')

    # Retrieve the binary message before the null character
    message_binary = binary_message[:null_index]

    # Split the binary message into 8-bit chunks and convert each chunk to a character using the chr function
    message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i+8]
        message += chr(int(byte, 2))

    return message

    # Split the binary message into 8-bit chunks and convert each chunk to a character using the chr function
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
        if chr(int(byte, 2)) not in string.printable:
            break

    return message
