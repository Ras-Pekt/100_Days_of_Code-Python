#!/usr/bin/python3
"""
Tip calculator
"""

print("Welcome to the tip calcultor")

while True:
    bill = float(input("What was the total bill? $"))
    if bill < 0:
        print("Enter a valid number")
    else:
        break

while True:
    people = int(input("How many people to split the bill? "))
    if people < 1:
        print("Enter a valid number")
    else:
        break

while True:
    percentage_tip = float(input("What percentage tip would you like to give? "))
    if percentage_tip < 1:
        print("Enter a valid number")
    else:
        break

tip = (percentage_tip / 100) * bill
individual_bill = (bill + tip) / people

print(f"Each person should pay: {individual_bill:.2f}")
