def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)  # Output: "Khoor, Zruog!"

# Decryption function (optional):
def caesar_decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)  # Output: "Hello, World!"
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)  # Output: "Khoor, Zruog!"

# Decryption function (optional):
def caesar_decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)  # Output: "Hello, World!"