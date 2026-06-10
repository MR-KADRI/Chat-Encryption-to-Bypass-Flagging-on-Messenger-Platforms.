def encrypt(text):
    encrypted = ""

    for char in text:
        ascii_value = ord(char) + 13
        encrypted += f"{ascii_value:03}"   # Make every value 3 digits

    return encrypted


def decrypt(code):
    decrypted = ""

    for i in range(0, len(code), 3):
        chunk = code[i:i+3]

        ascii_value = int(chunk) - 13
        decrypted += chr(ascii_value)

    return decrypted


# Menu
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose (1/2): ")

if choice == "1":
    message = input("Enter text to encrypt: ")
    encrypted_text = encrypt(message)
    print("Encrypted:", encrypted_text)

elif choice == "2":
    encrypted_code = input("Enter code to decrypt: ")
    decrypted_text = decrypt(encrypted_code)
    print("Decrypted:", decrypted_text)

else:
    print("Invalid choice")