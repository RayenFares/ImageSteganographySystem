# Encryption function
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Decryption function
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Example usage
message = "Hello, world!"
key = 3

# Encryption
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
