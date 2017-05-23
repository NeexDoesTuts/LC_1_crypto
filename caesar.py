from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_string = ""
    for letter in text:
        encrypted_string += rotate_character(letter, rot)
    return encrypted_string


def main():
    text = input("Type a message:\n")
    rotation = int(input("Rotate by:\n"))
    print(encrypt(text, rotation))
    #tests()

def tests():
    # Test alphabet_position()
    print(alphabet_position("A"))
    print(alphabet_position("a"))
    print(alphabet_position("x"))
    print(alphabet_position("z"))
    # test rotate_character()
    print(rotate_character("A", 13))
    print(rotate_character("a", 13))
    print(rotate_character("A", 130))
    print(rotate_character("A", 26))
    print(rotate_character("X", 13))
    print(rotate_character("x", 13))
    print(rotate_character("g", 10))
    print(rotate_character("!", 27))
    # test encrypt()
    print(encrypt("a", 13))
    print(encrypt("abcd", 13))
    print(encrypt("LaunchCode", 13))
    print(encrypt("LaunchCode", 1))
    print(encrypt("Hello, World!", 5))


if __name__ == "__main__":
    main()
    tests()