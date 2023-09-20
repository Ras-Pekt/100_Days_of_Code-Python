#!/usr/bin/python3
"""
A program that calculates the compatibility of two people
"""

print("Welcome to the Love Calculator!\n")

while True:
    name1 = input("What is you name?\n")
    if name1 == "":
        continue
    break

while True:
    name2 = input("What is their name?\n")
    if name2 == "":
        continue
    break

true_count = 0
love_count = 0

for i in "true":
    true_count += name1.lower().count(i)
    true_count += name2.lower().count(i)

for i in "love":
    love_count += name1.lower().count(i)
    love_count += name2.lower().count(i)

love_score = int(f"{true_count}{love_count}")

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")
