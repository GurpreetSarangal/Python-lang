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
### Functions with list

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


* append(): The append() method adds a single item to the existing list. It doesn't return new list, rather is modifies the original list. If a list is passed, it just nests' the lists unlike extend method.
    - list.append(item)
* count(): The method count() returns count of how many times the particular item occurs in list.
    - list.count(item)
* extend(): This method extend() appends the contents of sequence to list as individaual elements.
    - list.extend(seq)
* index(): The method index() returns the index value of object.
    - list.index(obj)
    - list.index(obj, start, end)
        - where start and end are integers
* insert():
    - list.insert(index, object)
* pop(): removes and returns the element at the index specified.
    - list.pop()
    - list.pop(index)
        -  If index is out of range it throws an error.
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
### Functions with Dictionaries

   
* print(dict): 
    - prints the entire dictionary
* dict ['key']:
    - returns the value for "key"
    - [IF the 'key' is not present in dictionary it will cause an error]
    - [this and get() function does the same job but here it is programmers responsibility to ensure the 'key' exists in the dictionary or there will be an error]
* sorted(dict.items):
    - to iterate through dictionaries in order.
* dict1 = dict(zip(keys,values)):
    - where 'keys' and 'values' are list which are zipped together to make a dict
* sorted_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
    - IDK what this dude does
----
### Methods with dictionaries*

* keys: returns all the keys
    - list(tuple)
* values: returns all the values
    - dict.values()
* items: returns a list of dict's tuple pairs.
    - dict.items()
* update: The method update() adds items of dictionary2 to first dictionary.
    - dict1.update(dict2)
* clear: The method clear() removes all items from the dictionary.
    - dict.clear()
* fromkeys(sequence) / fromkeys(seq, values)
    : The method fromkeys() creates a new dictionary with keys from seq and values set to value.
    - dict.fromkeys(seq,[values])
* copy: the method copy() returns an ordered copy of the data.
    - new_dict = dict.copy()
* get: the method get() returns value corresponding to the key
    - dict.get("key")
    - [IF the 'key' is not present in the dictionary the get() returns None]

----
**Range**

* range(5) : 0 until 4
* range(2,6) : 2 until 5
* range(2, 10, 2) : 2 until 9 with 2 steps :[2, 4, 6, 8]
----
### sets and its methods

* Set is a collection for non repetitive elements.
* set = {1,2,4,5} :
    - example of set
* set = set():
    - empty set
* set.add(3):
* set.add((6,7,8)):
    - a tuple can be added in set like this
    - repeatedly adding a value in set does not change the list


* these are invalid because they are not hashable
    - set.add([6,7,8])
    - set.add({4:5})

* properties of sets:
    - unordered
    - unindexed
    - there is no way to change items in sets.
    - sets cannot contain duplicate values.
**methods**

* print(len(set)):
    - prints the length of this set
* set.remove(1):
    - removes the element from set
    - throws an error if tried remove the element which is not present in set
* set.pop
