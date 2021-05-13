import random
string= "Memology is a young man's game"

def rand_Uppercase(string):
    newstring= ""
    for char in string:
        case= random.randint(0,1)
        if case == 0:
            newstring += char.upper()
        else:
            newstring += char.lower()
    print(newstring)

rand_Uppercase("This guy is crazy!")
