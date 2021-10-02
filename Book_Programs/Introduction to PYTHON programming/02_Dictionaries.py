student={
    "name" : "Gupreet Sarangal",
    "class": "BCA 2nd",
    "marks": "67",
    "rollNo": 7354,
}
# print (student)
# print(student['marks'])
# student["marks"] = int(student["marks"])
# print(type(student['marks']))
# print(student.keys())
# print(student.values())

# student["subject"] = "Python" # creates a new element
# # print (student)
# del student['marks']

print (student)
dup = student.copy() # duplicates the dictionary
print(dup)
dup.clear() # as the name suggests
print(dup)

