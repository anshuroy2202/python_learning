
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