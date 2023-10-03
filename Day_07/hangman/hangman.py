#!/usr/bin/python3

from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

print(logo, "\n\n")

chosen_word = choice(word_list)

lives = 6

display = []

for _ in chosen_word:
    display.append("_")
print(" ".join(display))

i = 0

while True:
    guessed_letter = input("Guess a letter: ").lower()

    if not guessed_letter:
        print(stages[lives])
        lives -= 1
    elif guessed_letter in chosen_word:
        if guessed_letter in display:
            print(f"You have already guessed the letter '{guessed_letter}'")
            print(" ".join(display))
        else:
            for i in range(len(chosen_word)):
                if guessed_letter == chosen_word[i]:
                    display[i] = guessed_letter
            print(" ".join(display))
    else:
        print(f"The letter '{guessed_letter}' is not in the word. You lose a life")
        print(" ".join(display))
        print(stages[lives])
        lives -= 1

    if lives == 0:
        print(f"The letter '{guessed_letter}' is not in the word. You lose a life")
        print(" ".join(display))
        print(stages[lives])
        print("You lose!!!")
        break

    if "_" not in display and lives != 0:
        print("You win!!!")
        break
