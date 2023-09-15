#!/usr/bin/python3
"""checks if a number is odd or even"""

while True:
    num = input("Which number do you want to check: ")
    if num == "":
        continue
    else:
        num = int(num)
        if num % 2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")

        break
