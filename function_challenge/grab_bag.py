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
    print("5. Press q to quit")
    
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
    num1=int(input("Please enter the first number: \n >"))
    num2=int(input("Please enter the first number: \n >"))
    num3=int(input("Please enter the first number: \n >"))
            
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

    print(f"The max of {num1},{num2},{num3} is ",max_of_three(num1,num2,num3))

def sumList():
    sum=0
    listxyz=[]
    counter=1
    user_input=""
    while user_input.lower() !="d":
        user_input=input(f"Please enter number {counter} of the list or press d when done:")
        listxyz.append(user_input)
        counter +=1
    for num in listxyz:
        sum +=num
    print("The sum of the numbers in the list is",sum)

def productList():
    def product_list(listxyz=[44,55,10,30]):
         product=1
         for num in listxyz:
             product *=num
         return product 

    print("The product of the numbers in the list is",product_list())

def reverseString():
    string= input("Enter the string that you would like to reverse:\n >")
    def reverse_string(string):
        x=len(string)-1
        print("Here is your reversed string: ",end="")
        while x>=0:
            print(string[x],end="")
            x -= 1
        print()
    reverse_string(string)

def looper():
    prompter()
    looper()

looper()
