import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_text = ""
    rotation_pos = 0

    for letter in text:
        if letter in string.ascii_letters:
            position = alphabet_position(rot[rotation_pos])
            encrypted_text += rotate_character(letter, position)
            rotation_pos = (rotation_pos + 1) % len(rot)
            #print(rotation_pos)
        else:
            encrypted_text += letter

    return encrypted_text


def main():
    text = input("Type a message:\n")
    rotation = input("Rotate by:\n")

    print(encrypt(text, rotation))

if __name__ == "__main__":
    main()