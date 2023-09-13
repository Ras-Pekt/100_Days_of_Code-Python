#!/usr/bin/python3
"""
Band name generator program
"""

print("Welcome to the Band Name Generator.")

while True:
    city_name = input("What's the name of the city you grew up in?\n")
    if (city_name == ""):
        print("Please enter a name")
    else:
        break

while True:
    pet_name = input("What's your pet's name?\n")
    if (pet_name == ""):
        print("please enter a name")
    else:
        break

print(f"Your band name could be {city_name} {pet_name}")
