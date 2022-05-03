def palindromeFunction(num):
    temp, reverse = num,0
    while (num > 0):
        digi = num % 10
        num = num // 10
        reverse = reverse * 10 + digi
    if(temp == reverse):
        return True
    else:
        return False

print("input any number: ",end='')
num = int(input())
pal = palindromeFunction(num)
if(pal == True):
    print("The number",num,"is a palindrome.")
else:
    print("The number",num,"is not a palindrome.")