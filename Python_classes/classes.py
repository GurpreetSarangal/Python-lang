# from multiprocessing import Condition


# # if (Condition):
# #     pass
# # elif (Condition):
# #     pass
# # else:
# #     pass

# # if(condition):
# #     if(Condition):
# #         pass
# #     else:
# #         pass
# # else:
# #     if(Condition):
# #         pass
# #     else:
# #         pass

# b = ''' docstring
# dsdfsnfa
# adfansdkf
# adfadksll '''
# print(b)
# # definite loop   
# # here we know after how many iterations loop will terminate
# for a in range(10):
#     pass # pass statement is used as place holder where we don't know yet what to do but as all blocks in python require a statement 'pass' is used to keep a block empty
#     # without this python will throw an error

# a = 1
# # indefinite loop
# # here we don't know after how many iterations loop will termintate
# while a != 0:
#     a = int(input())
# # this is also an example of sentinel loop

# a = (lambda a,b,c: a+b+c)

# sum = a(10, 20, 30)
# print(sum,end='')
# (first * second )+third


def func(first, second, third):
    def mult(first2 , second2):
        return first2*second2
    m=mult(first,second)
    return m+third


# cal= func(10, 20, 30)
# print(cal)

# sum = func(10,20,30)
# func(second=20,first=10,third=30)

# list = [10,20,30,40]
# list.append([10,12302,231])
# print(list*2)

# list2 = list
# print(list2==list)

# # *, +, =, in, not in,==
# ()
# {}
# [] 

dict = {
    "sandi" : 10,
    "me" : 20,    
    "a" : [122,231,4,2]
}
# print(dict["a"])