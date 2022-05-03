num= int(input("Enter how many numbers in fibonacci series: "))
i=1
a=0
b=1
print("first", num,"Fibonacci numbers: ")
while i<=num:
    print(a, end=' ')
    c = a+b
    a = b
    b = c
    i += 1

