import sys

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


def caesar_cipher(action: str, message: str, shift: int) -> str:
    if action not in {"decode", "encode"}:
        print("Unknown action, try again")
        sys.exit()

    shift %= 26  # Ensures shift is within valid range

    word = ""
    for letter in message.lower():
        if letter == " ":
            word += letter
            continue

        if letter not in ALPHABET:
            print(f"Error: '{letter}' is not a valid character.")
            sys.exit()

        index_letter = ALPHABET.index(letter)
        if action == "encode":
            index = (index_letter + shift) % 26
        else:  # action == "decode"
            index = (index_letter - shift) % 26

        word += ALPHABET[index]

    return word


SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    action = input(
        "Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
    message = input("Type your message: ")

    try:
        shift = int(input("Type the shift number: "))
    except ValueError:
        print("Invalid shift number. Please enter an integer.")
        continue

    result = caesar_cipher(action, message, shift)
    print(f"Here's the {action}d message: {result}")

    keep_running = input(
        "Type 'yes' if you want to go again. ").strip().lower()
    if keep_running == "no":
        SHOULD_CONTINUE = False

print("Goodbye!")
