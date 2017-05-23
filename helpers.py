import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    letter = letter.lower()

    for position in range(len(alphabet)):
        if alphabet[position] == letter:
            return position


def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    char_case = None
    position = None
    final_char = None

    if char not in string.ascii_letters:
        return char

    if char.islower():
        char_case = True
    else:
        char_case = False
        char.islower()

    position = (alphabet_position(char) + rot) % 26
    final_char = alphabet[position]

    if char_case:
        return final_char
    else:
        return final_char.upper()