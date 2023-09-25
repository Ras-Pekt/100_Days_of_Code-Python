#!/usr/bin/python3

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure[row, column]?\n")
try:
    row = int(position[0]) - 1
    column = int(position[1]) - 1
    map[row][column] = "X"
    print(f"{row1}\n{row2}\n{row3}")
except IndexError:
    print("Out of range")
