i=1
factor=0
num = int(input("Enter a number: "))
while i <= num:
    if num%i==0:
        factor += 1
    i += 1
if factor==2:
    print(num,"is a prime number.")
else:
    print(num,"is a composite number.")