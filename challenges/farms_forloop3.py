#!/usr/bin/env python3
  
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

veggies=["carrots", "celery"]

print(" Please choose a farm from below:")
print("a. NE Farm")
print("b. W Farm")
print("c. SE Farm")

users_farm=input(">")

if users_farm=="a":
    for animal in farms[0]["agriculture"]:
        if animal not in veggies:
            print(animal)
elif users_farm=="b":
    for animal in farms[1]["agriculture"]:
        if animal not in veggies:
            print(animal)
elif users_farm=="c":
    for animal in farms[2]["agriculture"]:
        if animal not in veggies:
            print(animal)
