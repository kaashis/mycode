#!input/env/bin env

n=1
i=0
for n in range(10):
    if n<6:
        for i in range(n):
            print("*",end="")
            i +=1;
        print()
        n +=1
    else:
        for i in range(5,0,-1):
            print("*",end="")
            i -=1
        print()
        n +=1
    
