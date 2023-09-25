#!/usr/bin/python3
"""
claculate average height without using len() and sum() functions
"""

heights = input("Input a list of student heights\n").split()
count = 0
sum = 0

for n in heights:
    try:
        num = int(n)
    except ValueError:
        print(f"{n} not a valid height")
        continue

    sum += num
    count += 1

average_height = round(sum / count)
print(f"Average Height of Students: {average_height}")
