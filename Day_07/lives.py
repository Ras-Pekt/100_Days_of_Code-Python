#!/usr/bin/python3

import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

lives = 6

display = []

for _ in chosen_word:
    display.append("_")
print(" ".join(display))

i = 0

while True:
    chosen_letter = input("Guess a letter: ").lower()

    if lives == 0:
        print(stages[lives])
        print("You lose!!!")
        break
    
    if not chosen_letter:
        print(stages[lives])
        lives -= 1
    elif chosen_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_letter == chosen_word[i]:
                display[i] = chosen_letter
    else:
        print(stages[lives])
        print(lives)
        lives -= 1

    print(" ".join(display))

    if "_" not in display and lives != 0:
        print("You win!!!")
        break
