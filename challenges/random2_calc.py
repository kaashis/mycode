#PEMDAS

def calc(a,b,x,y,z):
    print(((x**2 * y)/z)+a-b)

calc(1,2,3,4,5)
calc(5,4,3,2,1)

def pythagorean(a,b,c):
    assert a**2 + b**2 == c**2

pythagorean(3,4,5)
pythagorean(2,5,4)
