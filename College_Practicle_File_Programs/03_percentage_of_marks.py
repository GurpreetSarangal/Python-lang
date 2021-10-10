# input marks of three subjects and calculate percentage
print("MM in each subject => 100")
sub1= float(input("Input marks of first subject: "))
sub2= float(input("Input marks of second subject: "))
sub3= float(input("Input marks of third subject: "))
if sub1>100 or sub2>100 or sub3>100:
    print("WRONG INPUT")
else:
    sum=sub1+sub2+sub3
    per=(sum/300)*100
    print("Percentage : ",per,"%")