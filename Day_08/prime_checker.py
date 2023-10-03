#!/usr/bin/python3
from math import sqrt

def prime_checker(number):
    for num in range(2, int(sqrt(number)) + 1):
        if number % num == 0:
            print("It's a not prime number")
            return
    print("It's a prime number")

while True:
    try:
        n = int (input("Check this number: "))
        break
    except ValueError:
        continue

prime_checker(number=n)
