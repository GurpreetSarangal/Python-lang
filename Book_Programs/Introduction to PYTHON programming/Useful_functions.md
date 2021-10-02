# Useful Functions

### Functions with variables
* type(): used to know which class a variable or a value belongs to.
    - syntax:type(var)
* isinstance(): to check if an object belongs to a particular class
    - isinstance(var)
-----
### Functions with string

* len(): returns the number of characters in string or no. to elements in list
    - len(string) or len(list)
* count(): returns the number of times a character/element repeates in the string or list.
    - str.count(' ') will return number of times ' ' is there in str
* str.upper()
* str.swapcase()
* replace(): accepts two inputs, one for substring which is to be replaced and one which is to be placed in.
    - str.replace("old substring", "new substring")
    
------
### List Functions

* print(list): prints the entire list
* len(): returns the total number of elements 
    - len(list)
* index(): returns the index of the element in the list
    - list.index(34)
* remove(): removes the element from the list
    - list.remove(43)
* append(): addes a new element at the end of list
    - list.append('new element')
* reverse(): reverses the whole list
    - list.reverse()
* max(): This function returns the elements from the Python list with maximum value.
    - max(list)
* min(): This function returns the elements from the list with minimum value
    - min(list)
* list(): This function converts the sequence such as python tuple into python list.
    - list1 = list(tuple)


### List Methods

* append(): The append() method adds a single item to the existing list. It doesn't return new list, rather is modifies the original list.
    - list.append(item)
* count(): The method count() returns count of how many times the particular item occurs in list.
    - list.count(item)
* extend(): This method extend() appends the contenst of sequence to list.
    - list.extend(seq)
* index(): The method index() returns the index value of object.
    - list.index(obj)
* insert():
    - list.insert(index, object)
* pop():
    - list.pop()
    - list.pop(index)
* remove():
    - list.remove()
* reverse():
    - list.reverse()
* sort():
    - list.sort()

------
**Tuples**

    Tuples are similar to Lists except their values cannot be changed. 
-------
**Functions with Dictionaries**

* print(dict): prints the entire dictionary
* dict ['key']: returns the value for "key"
* dict.keys(): returns all the keys
* dict.values(): returns all the values

----