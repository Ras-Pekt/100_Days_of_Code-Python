#!/usr/bin/python3

import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

while True:
    chosen_letter = input("Guess a letter: ").lower()
    if chosen_letter == "":
        continue
    for i in chosen_word:
        if chosen_letter == i:
            print("Right")
        else:
            print("Wrong")
    break
