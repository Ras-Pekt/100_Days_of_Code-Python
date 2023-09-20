#!/usr/bin/python3
"""
An automatic pizza order program
"""

print("Welcome to Python Pizza Deliveries!\n")

while True:
    size = input("What size pizza do you want? S, M or L: ")
    if size.upper() != "S" and size.upper() != "M" and size.upper() != "L":
        continue
    break

while True:    
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if  add_pepperoni.upper() != "Y" and add_pepperoni.upper() != "N":
        continue
    break

while True:
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.upper() != "Y" and extra_cheese.upper() != "N":
        continue
    break

if size.upper() == "S":
    bill = 15
    if  add_pepperoni.upper() == "Y":
        bill += 2
    if extra_cheese.upper() == "Y":
        bill += 1
elif size.upper() == "M":
    bill = 20
    if  add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1
elif size.upper() == "L":
    bill = 25
    if  add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1

print(f"Your bill is: ${bill}.")
