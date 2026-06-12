
# python support the scripting
# python --> to activate the python shell
# quit() or exit()  --> to exit the python shell

# operators
# arithmetic operators
# +, -, *, /, //, %, **

x,y=6,7
print(x+y)  # 13 (addition)
z=-x  # -6 (negation)


# assignment operators
# =, +=, -=, *=, /=, //=, %=, **=

# comparison operators or relational operators ( returns a boolean value)
# ==, !=, >, <, >=, <=

# logical operators
# and, or, not
x,y=7,8
# Assignment statements cannot be placed inside another expression.
# z=x>5 and ((y=y+1)==10) # ERROR: SyntaxError: assignment expression cannot be used in a generator expression (because assignment statements cannot be used inside expressions, including logical expressions)

# Bitwise Operators
# &, |, ^, ~, <<, >>

# Membership Operators
# in, not in
l=[1, 2, 3, 4, 5]
print(3 in l)  # True (membership operator)
print(6 not in l)  # True (membership operator)

# Identity Operators
# is, is not
x=[1, 2, 3]
y=[1, 2, 3]
print(x is y)  # False (because x and y are different objects in memory, even though they have the same content)
print(x == y)  # True (because x and y have the same content, but they are different objects in memory)
z=x
print(x is z)  # True (because x and z refer to the same object in memory)



a = 10
b = 3

print(a + b)      # Arithmetic
print(a > b)      # Comparison
a += 5            # Assignment
print(a)

print(True and False)  # Logical

print(5 & 3)      # Bitwise

name = "Anshu"
print("A" in name)     # Membership

x = [1, 2]
y = x
print(x is y)          # Identity

print(50*'*')


# -----------------------------------------------------------
# data types

# Numeric Types
# ----------------
# int, float, complex
x=6
pi=3.14
z=2+3j
print(type(x))  # <class 'int'>
print(type(pi))  # <class 'float'>  
print(type(z))  # <class 'complex'>
complex_num = complex(2, 3)  # creates a complex number with real part 2 and imaginary part 3
print(complex_num)  # (2+3j)
int_num = int(3.14)  # converts the float 3.14 to an integer (truncates the decimal part)
print(int_num)  # 3
float_num = float(5)  # converts the integer 5 to a float
print(float_num)  # 5.0



# Text Type
# ----------------
# str
name="Anshu"
print(type(name))  # <class 'str'> (string is a sequence of characters enclosed


# Sequence Types
# ----------------
# list, tuple, range
r=range(1, 10)  # creates a range object representing the sequence of numbers from 1 to 9
print(r)  # range(1, 10)
print(type(r))  # <class 'range'> (range is a built-in sequence type that represents an immutable sequence of numbers)

print(list(range(0,10,2)))  # [0, 2, 4, 6, 8] (creates a list of numbers from 0 to 9 with a step of 2)  
print(tuple(range(0,10,3)))  # (0, 3, 6, 9) (creates a tuple of numbers from 0 to 9 with a step of 3)   


# Mapping Type
# ----------------
# dict
even=range(0, 10, 2)
squared={x: x**2 for x in even}  # creates a dictionary where the keys are the even numbers from 0 to 8 and the values are their squares
print(dict(enumerate("Anshu")))  # {0: 'A', 1: 'n', 2: 's', 3: 'h', 4: 'u'} (creates a dictionary by enumerating the characters in the string "Anshu", where the keys are the indices and the values are the characters at those indices)
print(enumerate(even))  # <enumerate object at 0x7f8b8c8c8c8> (creates an enumerate object that can be used to iterate over the even numbers with their indices using a for loop or by converting it to a list or dictionary)


# Set Types
# ----------------
# set, frozenset
print(set(range(0,10,3))) # {0, 3, 6, 9} (creates a set of numbers from 0 to 9 with a step of 3)    



# Boolean Type
# ----------------
# bool
a=True
b=False
print(type(a))  # <class 'bool'> (boolean type represents one of two values: True or False)
print(a and b)  # False (logical AND)
print(a or b)   # True (logical OR)
print(a+1)    # 2 (True is treated as 1 in arithmetic operations)
print(b+1)    # 1 (False is treated as 0 in arithmetic operations
print(int(a))  # 1 (converts True to 1)
print(int(b))  # 0 (converts False to 0)


# Binary Types
# ----------------
# bytes, bytearray, memoryview

# None Type
# ----------------
# None
x=None
print(type(x))  # <class 'NoneType'>
# print(x+1)  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' (None cannot be used in arithmetic operations)
print(int(x)+1)  # 1 (converts None to 0)


a = 10          # int
b = 3.14        # float
c = "Anshu"     # str
d = [1, 2, 3]   # list
e = (1, 2, 3)   # tuple
f = {"name": "Anshu", "age": 21}  # dict
g = {1, 2, 3}   # set
h = True        # bool
i = None        # NoneType

print(type(a))  # <class 'int'>
print(type(c))  # <class 'str'>

print(50*'*')
# -----------------------------------------------------------
# strings
# ----------
# string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# strings are immutable sequences of characters so whatever we do with the string it will always return a new string and the original string will remain unchanged
name = "Anshu Kumar Roy"
print(name[0])    # A
print(name[-2])    #o
print(name[6:11]) # Kumar
print(name[-3:])  # Roy
print(len(name))   # 17
print(name.upper())  # ANSHU KUMAR ROY
print(name.lower())  # anshu kumar roy
print(name.split())  # ['Anshu', 'Kumar', 'Roy']
print(name.replace("Anshu", "Anshul"))  # Anshul Kumar Roy
print(name.find("Kumar"))  # 6
print(name.startswith("Anshu"))  # True
print(name.endswith("Roy"))  # True
print(name.count("a"))  # 2
print(name.isalpha())  # False (because of spaces)
print(name.isalnum())  # False (because of spaces)
print(name.strip())  # Anshu Kumar Roy (removes leading and trailing whitespace)
print(name.center(30, "*"))  # *****Anshu Kumar Roy*****
print('reversing the string:',name[::-1])  # yoR ramuK uhnsA (reverses the string)
print(name[::2])  # AsuKmrRy (every second character)

# print(name+2)  # TypeError: can only concatenate str (not "int") to str
print(name +str(2))  # Anshu Kumar Roy2 (concatenating string with number)

print(50*'*')
# ------------------------------------------------------------------
# List
# list is a collection which is ordered and changeable. Allows duplicate members.
my_list = [1, 2, 3, "Anshu", [4, 5], (6, 7), {"name": "Anshu"}, {8, 9}]
print(my_list[0])  # 1
print(my_list[3])  # Anshu
print(my_list[4])  # [4, 5]
print(my_list[5])  # (6, 7)
print(my_list[6])  # {'name': 'Anshu'}
print(my_list[7])  # {8, 9}
print(len(my_list))  # 8
my_list.append(10)  # [1, 2, 3, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 10]
my_list.insert(1, "Hello")  # [1, 'Hello', 2, 3, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 10]
my_list.remove(3)  # [1, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 10]
my_list.pop()  # [1, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}]
my_list[0] = 100  # [100, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}]
print(my_list)


print(my_list + [11, 12])  # [100, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 11, 12]
print(my_list * 2)  # [100, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 100, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}]    
print(my_list[1:4])  # ['Hello', 2, 'Anshu']
print(my_list[::-1])  # [{8, 9}, {'name': 'Anshu'}, (6, 7), [4, 5], 'Anshu', 2, 'Hello', 100] (reverses the list)
print(len(my_list))  # 8


my_list.append([13, 14])  # [100, 'Hello', 2, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, [13, 14]]
my_list.count(2)  # 1
my_list.index("Anshu")  # 3
# my_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
my_list.reverse()  # [{8, 9}, {'name': 'Anshu'}, (6, 7), [4, 5], 'Anshu', 2, 'Hello', 100] (reverses the list)
my_list.remove("Hello")  # [{8, 9}, {'name': 'Anshu'}, (6, 7), [4, 5], 'Anshu', 2, 100] (removes the first occurrence of "Hello")
my_list.clear()  # [] (clears the list)

# multiple values addition and deletion
my_list.extend([13, 14]) # [13, 14] (adds multiple values to the end of the list)
my_list += [15, 16] # [13, 14, 15, 16] (adds multiple values to the end of the list)
my_list.append([17, 18]) # [13, 14, 15, 16, [17, 18]] (adds a list as a single element to the end of the list)
del my_list[2:6] # deletes the elements from index 2 to 5
print(my_list)  # [{8, 9}, {'name': 'Anshu'}, 100] (after deleting elements from index 2 to 5)


print(50*'*')
# -------------------------------------------------------------------
# TUPLE
# tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# A tuple is immutable, which means you cannot change, add, or remove elements after the tuple is created
# A tuple is immutable. We cannot add, remove, or modify its elements after creation. If it seems like we are adding elements using +, Python is actually creating a new tuple rather than modifying the existing one.

my_tuple = (1, 2, 3, "Anshu", [4, 5], (6, 7), {"name": "Anshu"}, {8, 9})
print(my_tuple[0])  # 1
print(my_tuple[3])  # Anshu
print(my_tuple[4])  # [4, 5]
print(my_tuple[5])  # (6, 7)
print(my_tuple[6])  # {'name': 'Anshu'}
print(my_tuple[7])  # {8, 9}    
print(len(my_tuple))  # 8

# A new tuple  is  created.
print(my_tuple + (10, 11))  # (1, 2, 3, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 10, 11)
print(my_tuple * 2)  # (1, 2, 3, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9}, 1, 2, 3, 'Anshu', [4, 5], (6, 7), {'name': 'Anshu'}, {8, 9})
print(my_tuple[1:4])  # (2, 3, 'Anshu')
print(my_tuple[::-1])  # ({8, 9}, {'name': 'Anshu'}, (6, 7), [4, 5], 'Anshu', 3, 2, 1) (reverses the tuple)
print(len(my_tuple))  # 8
print(my_tuple.count(2))  # 1
print(my_tuple.index("Anshu"))  # 3
print(my_tuple)


t = ([1, 2], [3, 4])

t[0].append(5)
print(t) # ([1, 2, 5], [3, 4])
# Because the tuple itself did not change. The tuple still contains two list objects. Lists are mutable, so the contents of the list can change even though the tuple cannot.


t1= (1, 2, 3)
a, b, c = t1
print(a,b,c)  # 1 2 3 (unpacking the tuple into variables)

print(3 in t1)  # True (membership operator)

# IMPORTANT: 
# If a tuple contains only one element, it must have a comma after the element to be recognized as a tuple. Otherwise, it will be treated as a regular value enclosed in parentheses.
t2 = (1)  # This is not a tuple, it's just the integer 1 enclosed in parentheses.
print(type(t2))  # <class 'int'>
t3 = (1,)  # This is a tuple with one element.
print(type(t3))  # <class 'tuple'>

print(50*'*')
# -----------------------------------------------------------------
# SET
# set is a collection which is unordered and unindexed. No duplicate members so duplicates are automatically removed.
# set stores the elements in a hash table, which allows for fast membership testing and eliminates duplicates. When you create a set, it automatically removes any duplicate elements, ensuring that each element is unique within the set. This is why sets do not allow duplicate members. If you try to add a duplicate element to a set, it will simply ignore the duplicate and keep only one instance of that element in the set.

my_set = {1, 2, 3, "Anshu", (4, 5), frozenset({6, 7}), frozenset({"name": "Anshu"}), frozenset({8, 9})}
print(1 in my_set)  # True (membership operator)
print("Anshu" in my_set)  # True (membership operator)
print(len(my_set))  # 8

# Adds one single element to a set.
my_set.add(10)  # {1, 2, 3, 'Anshu', (4, 5), frozenset({6, 7}), frozenset({'name': 'Anshu'}), frozenset({8, 9}), 10}

# Adds multiple elements from another iterable (list, tuple, set, string, etc.).
my_set.update({11, 12})  # {1, 2, 3, 'Anshu', (4, 5), frozenset({6, 7}), frozenset({'name': 'Anshu'}), frozenset({8, 9}), 10, 11, 12}
my_set.remove(3)  # {1, 2, 'Anshu', (4, 5), frozenset({6, 7}), frozenset({'name': 'Anshu'}), frozenset({8, 9}), 10, 11, 12} (removes the element 3)
my_set.discard(4)  # {1, 2, 'Anshu', (4, 5), frozenset({6, 7}), frozenset({'name': 'Anshu'}), frozenset({8, 9}), 10, 11, 12} (does nothing because 4 is not in the set)
my_set.pop()  # removes and returns an arbitrary element from the set
print(my_set)  # {2, 'Anshu', (4, 5), frozenset({6, 7}), frozenset({'name': 'Anshu'}), frozenset({8, 9}), 10, 11, 12} (after popping an element)
my_set.clear()  # set() (clears the set)

set1={}
print(type(set1))  # <class 'dict'> (because {} creates an empty dictionary, not a set)
set2=set()
print(type(set2))  # <class 'set'> (because set() creates an empty set)


# remove all the chaarcters from the string except the vowels using set
string = set("Anshu Kumar Roy")
vowels = set("AEIOUaeiou")
result = string.intersection(vowels)
print(result)  # {'a', 'u', 'o'} (the vowels present in the string)
print(string.difference(vowels))  # {' ', 'n', 'h', 's', 'K', 'm', 'r', 'R', 'y'} (the characters in the string that are not vowels )
print(string.union(vowels))  # {' ', 'n', 'h', 's', 'K', 'm', 'r', 'R', 'y', 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'} (all unique characters from both sets  )
print(string.symmetric_difference(vowels))  # {' ', 'n', 'h', 's', 'K', 'm', 'r', 'R', 'y', 'A', 'E', 'I', 'O', 'U', 'e', 'i'} (characters that are in either set but not in both)
# -(difference) |(union) &(intersection) ^(symmetric_difference)
# (which are not present in the other set) (which are present in either set) (which are present in both sets) (which are present in one set but not both sets)


print(50*'*')
# --------------------------------------------------------------------

# DICTIONARY
# dict is a collection which is unordered, changeable and indexed. No duplicate members.
my_dict = {"name": "Anshu", "age": 21, "city": "Kolkata", "hobbies": ["coding", "gaming"], "education": {"degree": "B.Tech", "field": "CSE"}, "is_student": True}
print(my_dict["name"])  # Anshu
print(my_dict["age"])  # 21
print(my_dict["hobbies"])  # ['coding', 'gaming']
print(my_dict["education"])  # {'degree': 'B.Tech', 'field': 'CSE'}
print(len(my_dict))  # 6
my_dict["name"] = "Anshul"  # {'name': 'Anshul', 'age': 21, 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True} (updates the value of the key "name")
my_dict["country"] = "India"  # {'name': 'Anshul', 'age': 21, 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True, 'country': 'India'} (adds a new key-value pair to the dictionary)
print(my_dict)

my_dict['is_married'] = False  # {'name': 'Anshul', 'age': 21, 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True, 'country': 'India', 'is_married': False} (adds a new key-value pair to the dictionary)
my_dict.pop("age")  # {'name': 'Anshul', 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True, 'country': 'India', 'is_married': False} (removes the key "age" and its associated value)
my_dict.popitem()  # {'name': 'Anshul', 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True, 'country': 'India'} (removes the last inserted key-value pair)
print(my_dict)  
# multiple key-value pairs addition and deletion
my_dict.update({"age": 21, "is_married": False})  # {'name': 'Anshul', 'city': 'Kolkata', 'hobbies': ['coding', 'gaming'], 'education': {'degree': 'B.Tech', 'field': 'CSE'}, 'is_student': True, 'country': 'India', 'age': 21, 'is_married': False} (updates the dictionary with the key-value pairs from another dictionary)
print(my_dict)

# print(my_dict[2]) # KeyError: 2 (because there is no key 2 in the dictionary, dictionaries are accessed by keys, not by index)
print(my_dict.get(2)) # None (because there is no key 2 in the dictionary, get() method returns None if the key is not found)
print(my_dict.get(2,'Not found'))

# key is a collection of set and frozenset because they are immutable and can be hashed, which allows them to be used as keys in a dictionary. Lists and dictionaries cannot be used as keys because they are mutable and cannot be hashed.
dict1={'a':1, 'b':2, 'c':3,'a':4} # {'a': 4, 'b': 2, 'c': 3} (because keys must be unique in a dictionary, the second occurrence of 'a' overwrites the first one)
print(dict1)

# values can be of any data type and can be duplicated, but keys must be unique and immutable (cannot be changed after creation). If you try to use a mutable data type (like a list or a dictionary) as a key, it will raise a TypeError because mutable types cannot be hashed.

keys=[1, 2, 3]
values=['one', 'two', 'three']
my_dict2=dict(zip(keys, values)) # {1: 'one', 2: 'two', 3: 'three'} (creates a dictionary by zipping together two lists of keys and values)
print(my_dict2)







# INPUT
# --------------------------------
a=input()
b=input('Enter the value:')
print('a+b',a+b)
# it returns the string value

# type casting is neccesary 
a=int(input("enter the number"))
b=int(input("enter the number"))
print('a+b',a+b)

li=list(map(int,input('enter the list:').split()))
print(li)