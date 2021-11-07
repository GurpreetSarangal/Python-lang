# this is a experimental program on lists and its 

fruits = ['apple','mango','guava','orange']
fruits.extend(['grapes','mango'])

# list comprehension 
# list = [(x/2)**2 for x in [1,2,3,4,5,6]]
# newlist = [EXPR for LIST_ELEMENT in ITERABLE [if condition] ]


# fruits.index('mango')
# fruits.index('mango',2,5)

# fruits.pop(4)
# fruits.pop('mango') ERROR
# fruits.pop(90) ERROR

# fruits.remove('apple')
# fruits.remove(4) ERROR
# fruits.remove() ERROR


# fruits.append(['carrot','reddish'])
# fruits.append(['carrot','reddish'])

# fruits.extend(['grapes','mango'])

# just for insert method
# fruits.insert(-1,'banana')
# ['apple', 'mango', 'guava', 'orange', 'grapes', 'mango', 'banana']
#    0,-6     1,-5     2,-4     3,-3       4,-2      5,-1,    6 and above

# fruits.reverse()
# fruits.reverse(4) ERROR

# fruits.sort() 
# sort takes no arguments

print(fruits.sort() )
