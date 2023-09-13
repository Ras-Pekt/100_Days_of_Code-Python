#!/usr/bin/python3
"""
BMI calculator
"""

print("Welcome to BMI Calculator")

while True:
    height = float(input("Enter your height in meters: "))
    if height < 1:
        print("Enter a valid height")
    else:
        break

while True:
    weight = float(input("Enter you weight in kilograms: "))
    if weight < 1:
        print("Enter a valid weight")
    else:
        break

bmi = weight / height ** 2

print(f"Your BMI is: {bmi:.2f}")
