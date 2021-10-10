factorial=1
number= int(input("Enter an integer: "))
while number > 0:
    factorial = factorial * number
    number -= 1

print("factorial is: ",factorial)