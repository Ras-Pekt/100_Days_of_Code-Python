#!/usr/bin/python3
"""
calculates how many days, weeks, months left if we live until 90 years old
"""

while True:
    age = input("What is your current age? ")
    if age == "" or int(age) < 1:
        print("Enter a valid age")
    else:
        age = int(age)
        age_remaining = 90 - age
        months_remaining = age_remaining * 12
        weeks_remaining = age_remaining * 52
        days_remaining = age_remaining * 365
        print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
        break
