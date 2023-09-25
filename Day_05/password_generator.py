#!/usr/bin/python3
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

while True:
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        break
    except ValueError:
        continue

while True:
    try:
        nr_symbols = int(input("How many symbols would you like?\n"))
        break
    except ValueError:
        continue

while True:
    try:
        nr_numbers = int(input("How many numbers would you like?\n"))
        break
    except ValueError:
        continue

password = []

for _ in range(nr_letters):
    password.append(random.choice(letters))

for _ in range(nr_symbols):
    password.append(random.choice(symbols))

for _ in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password = "".join(password)
print(f"Here is your password: {password}")