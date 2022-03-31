
# def show():
#     print("hello students")
#     print("This is python")
# show()

# def shownum(num1, num2):
#     print(num1, num2)

# shownum(10,20)

# def sumfunc(num1, num2):
#     sum = num1+num2
#     return sum
# print(sumfunc(10,20))

def allcal(num1, num2=20):
    sum = num1 + num2
    diff = num1 - num2
    return sum, diff
print(allcal(10, 20)) #positional argument
print(allcal(num2=10, num1=20)) #keyword argument
print(allcal(10)) #default argument VALID
print(allcal(10,15)) #default argument VALID
print(allcal(num1=15)) #default argument VALID
# print(allcal(num2=10)) #default argument INVALID

# variable length argument 
def sumfunc(*numbers):
    s = 0
    for n in numbers:
        s += n
    print("the sum is ",s)
sumfunc(10) 
sumfunc(10,20) 
sumfunc(10,20,30)
sumfunc(10,20,30,3435,53,4,534,5,345,345,3,53453)
