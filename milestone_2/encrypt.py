# encrypt.py

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

if __name__ == "__main__":
    key = int(input("Enter key:"))
    message = input("Enter message:")
    result = encrypt(message, key)
    print("Result:", result)