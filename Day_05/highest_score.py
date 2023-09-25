#!/usr/bin/python3
"""
claculate hihgest score without using max() function
"""

scores = input("Input a list of student scores\n").split()
max = 0

for n in scores:
    try:
        num = int(n)
    except ValueError:
        continue

    if num > max:
        max = num

print(f"The highest score in this class is: {max}")
