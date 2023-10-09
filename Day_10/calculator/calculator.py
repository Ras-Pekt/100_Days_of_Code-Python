#!/usr/bin/python3
from art import logo
from sys import exit

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0.0:
        return "ZeroDivisionError"
    return n1 / n2

calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    while True:
        try:
            num1 = float(input("What is the first number?: "))
            break
        except Exception as e:
            continue

    for key in calc_operations:
        print(key)

    while True:
        while True:
            operation = input("Pick an operation: ")
            if not operation or operation not in calc_operations:
                continue
            break

        while True:
            try:
                num2 = float(input("What is the next number?: "))
                break
            except Exception as e:
                continue

        answer = calc_operations[operation](num1, num2)

        if answer == "ZeroDivisionError":
            print("ZeroDivisionError")
            break

        print(f"{num1} {operation} {num2} = {answer}")
        num1 = answer

        prompt = input(f"Type 'yes' to continue calculating with {answer}, 'new' to start a new calculation, 'exit' to exit: ").lower()
        if prompt == "yes":
            continue
        elif prompt == "new":
            calculator()
        elif prompt == "exit":
            exit()

print(logo)
calculator()
