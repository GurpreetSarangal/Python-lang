

my_dict = {
    # 'key' : 'value'
    'name' : 'sushil',
    'class' : 'bca',
    'roll_no' : 3423,
    'subject' : 'math',
    'marks' : 34
}

print(my_dict) #prints whole dictionary

# print(my_dict['name']) # accessing the specific value using key

# print(my_dict.keys()) # returns a list of all the available keys in the dictionary

my_dict['grade'] = 'A' # update the dictinary by adding a new key-value pair

# del my_dict['name'] deletes single element 
# del(my_dict) deletes entire dictionary

#                        DICTIONARY FUNCTIONS
# print(len(my_dict)) # returns the number of keys in dict

# string = str(my_dict) # converts the dictionary into a string

# print(string)

#                       DICTIONARY METHODS
# print(my_dict.keys()) # returns a list of all the available keys in the dictionary

# print(my_dict.values()) # returns a list of all the available values in the dictionary

# print(my_dict.items()) # returns a list of dict's (key,value) tuple pairs

# my_dict2 = {
#     'percentage' : 54.3,
#     'grade' : 'B'
# }
# my_dict.update(my_dict2)
# print(my_dict)

# my_dict.clear() removes all items from the dictionary

# seq = ('name','age','class')
# # my_dict2 = my_dict.fromkeys(seq) # creates a new dictionary with keys from seq and 
# # my_dict2 = my_dict.fromkeys(seq,43) # values set to values
# print(my_dict2)

# my_dict2 = my_dict.copy() # returns an ordered copy of the data
# print(my_dict2)

#                                   LOOPING THROUGH ALL KEYS IN A DICTIONARY

# looping through all keys in a dictionary 
# for key in my_dict.keys():
#     print(key)

# looping through all values in a dictionary 
# for values in my_dict.values():
#     print(values)

# looping through all key-value pairs
# for key, value in my_dict.items():
#     print(key,"::",value)

# looping through a dictionary in order
# for key, value in sorted(my_dict.items()):
#     print(key,"::",value)

#                               CREATING A DICTIONARY FROM USER INPUT

# student = {}
# def get_input():
#     key = input("enter a key: ")
#     val = input("enter a value: ")
#     student[key] = val
# def display():
#     for key, val in student.items():
#         print(key,'::',val)
# get_input()
# display()
# get_input()
# display()

