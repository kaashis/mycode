#!/usr/bin/env python3

get_counter=0
post_counter=0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as file:
    for line in file:
        if "INFO" in line:
            if "GET" in line:
                get_counter += 1
            elif "POST" in line:
                post_counter += 1
        elif "- - - - -] Authorization failed" in line:
            print(line.split(" ")[-1],end="")
print("The number of GET requests is : ",get_counter)
print("The number of POST requests is : ", post_counter)
