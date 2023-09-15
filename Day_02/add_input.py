#!/usr/bin/python3
"""sums the digits inputted by user"""

user_input = input("Enter a number: ")
if user_input == "":
    sum = 0
elif len(user_input) < 2:
    sum = int(user_input[0])
else:
    sum = 0
    for i in range(len(user_input)):
        sum += int(user_input[i])

print(sum)
