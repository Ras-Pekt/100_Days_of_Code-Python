#!/usr/bin/python3

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year < 1:
        return "Invalid year"
    elif month > 12 or month < 1:
        return "Invalid month"

    leap = is_leap(year)
    if leap and month == 2:
        return 29
    return month_days[month - 1]


while True:
    try:
        year = int(input("Enter a year: "))
        break
    except Exception as e:
        continue

while True:
    try:
        month = int(input("Enter a month: "))
        break
    except Exception as e:
        continue


days = days_in_month(year, month)
print(days)