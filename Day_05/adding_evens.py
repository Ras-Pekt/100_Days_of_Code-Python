#!/usr/bin/python3
"""
add all even numbers between 1 and 100
"""

sum_evens = 0

for number in range(0, 101, 2):
    sum_evens += number

print(f"Sum of even numbers from 1 to 100: {sum_evens}")
