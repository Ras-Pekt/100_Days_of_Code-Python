#!/usr/bin/python3

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

choice_1 = input("You are at a cross road. Where do you want to go? left or right\n").lower()
if choice_1 == "left":
    choice_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across\n").lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if choice_3 == "yellow":
            print("Congratulations! You have found the treasure. You win")
        elif choice_3 == "red":
            print("You have entered a room filled with fire and you are burned to death!")
            print("Game Over!")
        elif choice_3 == "blue":
            print("You have entered a room full of man-eating beasts and they eat you!!!")
            print("Game Over!")
        else:
            print("Game Over!")
    elif choice_2 == "swim":
        print("The lake is filled with sharks and they eat you!")
        print("Game Over!")
    else:
        print("Game Over!")
elif choice_1 == "right":
    print("You have fallen into a deep hole, broke your neck and died")
    print("Game Over!")
else:
    print("Game Over!")

