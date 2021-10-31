index = int(input("fibonacci Series upto: "))
first = 0
second = 1
print(first,second,end=' ')
for i in range(index-1):
    third = first + second
    print(third, end=" ")
    first = second
    second = third