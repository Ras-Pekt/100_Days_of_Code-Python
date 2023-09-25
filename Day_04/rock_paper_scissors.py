#!/usr/bin/python3
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

roshambo = [rock, paper, scissors]
rosha = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose?\n0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

try:
    print(roshambo[user_choice])
    print(f"\n Computer chose:\n{roshambo[computer_choice]}\n")

    if user_choice == 0 and computer_choice == 2:
        print(f"{rosha[user_choice]} wins againist {rosha[computer_choice]}")
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print(f"{rosha[user_choice]} wins againist {rosha[computer_choice]}")
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print(f"{rosha[user_choice]} wins againist {rosha[computer_choice]}")
        print("You win")
    elif user_choice == computer_choice:
        print("Draw")
    else:
        print(f"{rosha[computer_choice]} wins againist {rosha[user_choice]}")
        print("You lose")
except IndexError:
    print("Wrong choice.\nYou lose.")
