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
        print("Enter a valid height")
    else:
        break

bmi = round(weight / height ** 2, 2)

if bmi <= 18.5:
    print(f"You BMI is {bmi}. You are underweight!!!")
elif bmi <= 25:
    print(f"You BMI is {bmi}. You have normal weight")
elif bmi <= 30:
    print(f"You BMI is {bmi}. You are overweight!!!")
elif bmi <= 35:
    print(f"You BMI is {bmi}. You are obese!!!")
else:
    print(f"You BMI is {bmi}. You are clinically obese!!!")
