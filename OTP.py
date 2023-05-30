import random

def generate_key(message_length):
    key = ""
    for _ in range(message_length):
        key += chr(random.randint(0, 255))
    return key

def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_char = chr(ord(message[i]) ^ ord(key[i]))
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_char = chr(ord(encrypted_message[i]) ^ ord(key[i]))
        decrypted_message += decrypted_char
    return decrypted_message

# Example usage
message = "Hello, world!"
key = generate_key(len(message))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
