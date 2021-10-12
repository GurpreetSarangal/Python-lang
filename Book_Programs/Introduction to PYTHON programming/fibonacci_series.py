def fibonacci_series(num):
    a = 0
    b = 1
    for i in range(num):
        c = a+b
        print(c," ",end='')
        a = b
        b = c

num2 = int(input("Enter the range of fibonacci series: "))
print("Your fibonacci series is: ")
fibonacci_series(num2)