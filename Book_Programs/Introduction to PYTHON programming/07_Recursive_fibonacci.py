from typing import Sequence


def fibo(num):
    if num<=1:
        return num
    else:
        return (fibo(num-1)+fibo(num-2))

Sequence = []
nterms = int(input("How many terms= "))
if nterms <= 0:
    print("please enter a positive integer")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        Sequence.append(fibo(i))
    
print(Sequence)