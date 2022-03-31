str = "reverse this"
str= list(str)
str.reverse()

revstr = []
for ch in str:
    revstr.append(ch)
    
revstr = ''.join(revstr)
print(revstr)