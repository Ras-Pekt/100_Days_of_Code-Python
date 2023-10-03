#!/usr/bin/python3
from math import ceil

def paint_calc(height, width, cover):
    if (height > 0 and height) and (width > 0 and width):
        area = height * width
        paint_cans = ceil(area / cover)
        print(f"You'll need {paint_cans} cans of paint")

def user_input(input_name):
    while True:
        try:
            user_input = int(input(f"{input_name} of wall: "))
            return user_input
        except ValueError:
            continue

test_h = user_input("Height")
test_w = user_input("Width")

coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
