i=1
j=1
limit = int(input("Enter the number of rows: " ))

while j<=limit:
    k = i * 8 + j
    print(i,"*",8,"+",j,"=",k)
    j+=1
    i = i*10+j