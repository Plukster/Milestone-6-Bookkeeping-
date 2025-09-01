# decrypt.py
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            decrypted_char = chr((ord(char) - start - shift + 26) % 26 + start)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    key = int(input("Enter key: "))
    encrypted_message = input("Enter message: ")
    result = decrypt(encrypted_message, key)
    print("Result:", result)