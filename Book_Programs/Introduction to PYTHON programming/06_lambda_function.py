# Python supports the creation of anonymous functions at runtime, using a construct called lambda. While normal functions are defined using the def keyword, in python anonymous functions are defined using lambda keyword.
#---- lambda functions are mainly used in combination with the functions 
# filter()
# map()
# reduce()

# syntax:
# lambda arg1, arg2,..., argN : expression using arguments
# lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
# lambda is an EXPRESSION, not a statement.
# lambda's body is a single expression, not a block of statements.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# to find the sum of numbers using lambda functions=
# sum = lambda x,y,z: x+y+z

# print('total is :',sum(1.3,2.6,3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# list of lambda functions
# l = [lambda x,y: x+y,
#     lambda x,y: x-y,
#     lambda x,y: x*y]
# for f in l:
#     print(f(10,20))

# print("Subtraction of two numbers:")
# print(l[1] (25,17))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Use of filter() function to filter out only even numbers from a list.
# my_list = [11, 334,32,45,33,66,645,4345,54,246,574]
# new_list = list(filter(lambda x: (x%2==0) , my_list))
# print(new_list)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Use of map() function to double all the items in a list
# my_list = [11, 334,32,45,33,66,645,4345,54,246,574]
# new_list = list( map( lambda x: x*2 , my_list )  )
# print(new_list)

