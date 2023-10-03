#!/usr/bin/python3

import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

for _ in chosen_word:
    display.append("_")
print(display)

i = 0

while True:
    chosen_letter = input("Guess a letter: ").lower()

    if chosen_letter == "":
        continue

    for i in range(len(chosen_word)):
        if chosen_letter == chosen_word[i]:
            display[i] = chosen_letter

    print(display)

    if "_" not in display:
        break

print("You win!!!")
