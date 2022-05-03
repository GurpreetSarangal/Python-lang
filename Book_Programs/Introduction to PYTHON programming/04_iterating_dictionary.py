dict1 = { # diclaring a dictionary
    'virat': 150,
    'rohit': 100,
    'dhoni': 174
}
for key in dict1.keys():
    print(key,end='  ')

print() #for an enter

for val in dict1.values():
    print(val,end='  ')

print()

for key in dict1.items():# to iterate through all items
    print(key)
