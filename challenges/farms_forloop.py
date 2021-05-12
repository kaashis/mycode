#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

veggies=["carrots", "celery"]

for farm in farms:
    if farm["name"]=="NE Farm":
        for animal in farm["agriculture"]:
            if animal not in veggies:
                print(animal, end=", ")
        print()
