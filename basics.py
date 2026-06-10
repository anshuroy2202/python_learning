
# python support the scripting
# python --> to activate the python shell
# quit() or exit()  --> to exit the python shell

# operators
# arithmetic operators
# +, -, *, /, //, %, **

# assignment operators
# =, +=, -=, *=, /=, //=, %=, **=

# comparison operators
# ==, !=, >, <, >=, <=

# logical operators
# and, or, not

# Bitwise Operators
# &, |, ^, ~, <<, >>

# Membership Operators
# in, not in

# Identity Operators
# is, is not


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
# int, float, complex

# Text Type
# str

# Sequence Types
# list, tuple, range

# Mapping Type
# dict

# Set Types
# set, frozenset

# Boolean Type
# bool

# Binary Types
# bytes, bytearray, memoryview

# None Type
# None

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

print(name+2)  # TypeError: can only concatenate str (not "int") to str
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