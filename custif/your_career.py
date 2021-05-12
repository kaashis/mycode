#!/usr/bin/env python3
import os
clear = lambda: os.system('clear')

spending_list =["vacation", "charity", "stocks"]
desert_island_list = ["books", "grill", "buddy"]

clear()
print("******** Welcome to your career guide program********* \n")
print("Please follow the prompts to proceed.\n")

print("What would you to spend your tax refund on?")
print(spending_list)
spending = input(">").lower()

print("\nWhat would you bring on a desert island?")
print(desert_island_list)
desert_island = input(">").lower()
print()

if spending =="vacation":
    if desert_island == "books":
    	print("You should be a guide")
    elif desert_island =="grill":
    	print("You should be a cook")
    elif desert_island =="buddy":
        print("You should be a travel journalist")  
    else:
        print("You did not pick correctly from the list provided")
elif spending =="charity":
    if desert_island == "books":
    	print("You should be a fundraiser")
    elif desert_island =="grill":
    	print("You should be a chef")
    elif desert_island =="buddy":
    	print("You should be a philanthropist") 
    else:
        print("You did not pick correctly from the list provided")

elif spending =="stocks":
    if desert_island == "books":
    	print("You should be a stock trader")
    elif desert_island =="grill":
    	print("You should be a food critic")
    elif desert_island =="buddy":
    	print("You should be a full time investor")
    else:
        print("You did not pick correctly from the list provided")
else:
        print("You did not pick correctly from the list provided")
