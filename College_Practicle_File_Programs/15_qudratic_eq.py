import math
print("Enter values for a,b,c: ")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

d = (b**2)-4*a*c
if d>0:
    x1 = b + (math.sqrt(d)/(2*a))
    x2 = b - (math.sqrt(d)/(2*a))
    print("Roots are: ")
    print("x1 =",x1)
    print("x2 =",x2)
elif d == 0:
    x = - b / (2*a)
    print("There is a single root: ")
    print("x1 = x2 =",x)
else:
    print("Roots are imaginary")