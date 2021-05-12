#!/usr/bin/env python3

import csv

with open("csv_users.txt","r") as data:
    counter=0
    #generate unique numbers
    #give all my files unique name
    for row in csv.reader(data):
        counter +=1
        filename = f"admin.rc{counter}"

        with open(filename, "w") as rcfile:
        print("hshh"+row[0], file=rcfile)
