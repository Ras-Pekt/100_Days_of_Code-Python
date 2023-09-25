#!/usr/bin/python3
import random

while True:
    names = input("Enter the names of everyone seperated by a comma and a space\n").lower()
    if names == "":
        continue

    names_list = names.split(", ")

    name_length = len(names_list)

    random_num = random.randint(0, name_length - 1)

    random_name = names_list[random_num].title()

    print(f"{random_name} is going to buy the meal today!")
    break
