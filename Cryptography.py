from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

def generate_key():
    # Generate a random 256-bit (32-byte) AES key
    return get_random_bytes(32)

def encrypt_message(message, key):
    # Create an AES cipher object with the provided key
    cipher = AES.new(key, AES.MODE_CBC)

    # Pad the message to make its length a multiple of 16 bytes (AES block size)
    padded_message = pad(message.encode(), AES.block_size)

    # Encrypt the padded message
    ciphertext = cipher.encrypt(padded_message)

    # Return the IV (Initialization Vector) and the ciphertext
    return cipher.iv + ciphertext

def decrypt_message(ciphertext, key):
    # Extract the IV from the ciphertext
    iv = ciphertext[:AES.block_size]

    # Create an AES cipher object with the provided key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext and remove the padding
    decrypted_message = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)

    # Return the decrypted message
    return decrypted_message.decode()

# Example usage
key = generate_key()
message = "Hello, World!"

encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)

print("Original message:", message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)

