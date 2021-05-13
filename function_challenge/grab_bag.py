#!/usr/bin/env Python3
import os
from sys import exit
clear = lambda: os.system('clear')

clear()
print("****** Welcome to Grab Bag Function! ******* \n\n")

def prompter():
    print("\nPlease choose one of the functions below that you'd like to use:\n")
    print("1. Max of three numbers")
    print("2. Sum of all the numbers in a list")
    print("3. Product of all the numbers in a list")
    print("4. Reverse a String")
    print("\n Please enter the corresponding number eg. 1 for Max")
    print(" Or Press q to quit") 
    user_input = input(">")

    if user_input =="1":
        max3()
    elif user_input =="2":
        sumList()
    elif user_input == "3":
        productList()
    elif user_input == "4":
        reverseString()
    elif user_input.lower()== "q":
        exit()
    else:
        print("Not a valid entry")
        prompter()

def max3():
    num1=int(input("Please enter the first  number: "))
    num2=int(input("Please enter the second number: "))
    num3=int(input("Please enter the third  number: "))
            
    def max_of_three(a,b,c):
        max=a
        if b>a:
            max=b
            if c>b:
                max=c
        else:
            if c>a:
                max=c
        return max;

    print(f"\nThe max of {num1},{num2},{num3} is ",max_of_three(num1,num2,num3))

def sumList():
    sum=0
    listxyz=[]
    counter=1
    user_input=""
    while user_input.lower() !="d":
        user_input=input(f"Please enter number {counter} of the list or press d when done:")
        if user_input !="d":
            listxyz.append(user_input)
        counter +=1
    for num in listxyz:
        sum +=int(num)

    print("\nHere is the list you entered:",listxyz)
    print("The sum of the numbers in the list is",sum)

def productList():
     product=1
     listxyz=[]
     counter=1
     user_input=""
     while user_input.lower() !="d":
        user_input=input(f"Please enter number {counter} of the list or press d when done:")
        if user_input !="d":
            listxyz.append(user_input)
        counter +=1
     for num in listxyz:
         product *=int(num)

     print("\nHere is the list you entered: ",listxyz)
     print("The product of the numbers in the list is",product)

def reverseString():
    string= input("Enter the string that you would like to reverse:\n >")
    
    x=len(string)-1
    print("\nHere is your reversed string: ",end="")
    while x>=0:
        print(string[x],end="")
        x -= 1
    print()

def looper():
    prompter()
    looper()

looper()
