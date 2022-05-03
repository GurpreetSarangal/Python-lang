class addition:
    def add(self, a, b):
        return a+b
class multiplication(addition):
    def mul(self, a, b):
        return a*b
    
class division(multiplication):
    def div(self, a, b):
        return a/b
    
class calc(division):
    def cal_all(self, a, b):
        sum = addition.add(self,a,b)
        prod = multiplication.mul(self,a,b);
        quot = division.div(self,a,b);
        return [sum,prod,quot]

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    obj = calc()
    res = obj.cal_all(a,b);
    print("sum = ",res[0])
    print("product = ",res[1])
    print("quotient = ",res[2])

main()
