weight = float(input())
amount = 0
i=0
if(weight < 20):
    amount = 20
elif(weight < 100):
    amount = 50
elif(weight < 500):
    amount = 100
elif(weight < 1000):
    amount = 200
else:
    temp = weight
    while(temp>0):
        rem = temp%10
        amount += rem*i*3
        i += i*10
        temp = temp//10

print("your payable amount is: ",amount)