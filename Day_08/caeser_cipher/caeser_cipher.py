#!/usr/bin/python3
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def text_input(message):
    while True:
        text = input (f"{message}\n").lower()
        if not text:
            continue
        return text

def caeser(direction, text, shift):
    encrypt_decrypt = ""

    if direction != "encode" and direction != "decode":
        return "Invalid encrypt/decrypt choice"

    if shift > 26:
        shift %= 26

    if direction == "decode":
            shift *= -1

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            shift_index = idx + shift

            if shift_index > 25:
                shift_index -= 26

            encrypt_decrypt += alphabet[shift_index]
        else:
            encrypt_decrypt += char

    return f"The {direction}d message is [{encrypt_decrypt}]"

print(logo, "\n\n")

while True:
    direction = text_input("Type 'encode' to encrypt, type 'decode' to decrypt:")

    text = text_input("Type your message:")

    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            continue

    print(caeser(direction, text, shift))
    prompt = input("Type 'Yes' to encode/decode again. 'No' to exit: ").lower()
    if not prompt or prompt != "yes":
        print("Goodbye.")
        break
