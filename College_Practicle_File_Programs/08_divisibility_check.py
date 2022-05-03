# to determine a given number is divisible by 5 or 7 or not
num = float(input("input the number: "))
if (num%5==0 and num%7==0):
    print(num,"is divisible by both 5 and 7.")
elif (num%5==0):
    print(num,"is divisible by 5 only.")
elif (num%7==0):
    print(num,"is divisible by 7 only.")
else:
    print(num,"is not divisible by either 5 or 7.")