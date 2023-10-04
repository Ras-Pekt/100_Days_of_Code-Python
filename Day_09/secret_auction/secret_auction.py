#!/usr/bin/python3

from art import logo

"""
This exercise requires the screen to be cleared once a bidder is done bidding
However, since this is for learning purposes
(and there isn't a straightforward way to accomplish this in the terminal)
this feature will not be included
"""

print(logo, "\n\n")

print("Welcome to the secret auction program.")

bid_dict = {}

while True:
    
    while True:
        bidder_name = input("What is your name?: ").lower()
        if not bidder_name:
            continue
        break

    while True:
        try:
            bid = int(input("What is your bid?: $"))
            break
        except Exception as e:
            continue

    bid_dict[bidder_name] = bid

    prompt = input("Are there any other bidders: Type 'Yes' or 'No'\n").lower()
    if not prompt or prompt != "yes":
        break

highest_bid = max(bid_dict.values())
highest_bidder = max(bid_dict, key=bid_dict.get)

print(f"The winner is {highest_bidder.title()} with a bid of ${highest_bid}.")