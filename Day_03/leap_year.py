#!/usr/bin/python3
"""
checks if an year is a leap year
"""

while True:
    year = input("Which year do you want to check: ")
    if year == "":
        continue

    year = int(year)
    if year < 1:
        continue

    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Leap year")
            break
        else:
            print("Not a leap year")
            break
    else:
        print("Not a leap year")
        break
