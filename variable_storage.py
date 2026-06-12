'''
When you create a variable in Python, Python stores the **value somewhere in memory**, and the variable name acts like a **label (reference)** pointing to that value.

Example:

```python
a = 10
```

What happens internally?

1. Python creates the integer object `10` in memory.
2. Python creates the variable name `a`.
3. `a` points to the memory location where `10` is stored.

You can check the memory address using `id()`:

```python
a = 10

print(id(a))
```

Output (will vary):

```python
140732345678912
```

This number represents the memory address (object ID) of the value.

### Another Example

```python
a = 10
b = a

print(id(a))
print(id(b))
```

Both may show the same ID because both variables refer to the same object `10`.

### Important Concept

Variables do **not store the actual value directly**. They store a **reference** to an object in memory.

Think of it like this:

```text
a ───► 10
b ───► 10
```

Both `a` and `b` point to the same object.

### Interview Answer (Short)

**Variable storage in Python means that a variable stores a reference to an object in memory rather than storing the actual value itself. Python automatically manages memory allocation and deallocation through its memory manager and garbage collector.**

'''

# Everthing in Python is an object, and variables are references to those objects.
a=5
print(id(a)) #140706471363624
b=5
print(id(b)) #140706471363624
# Both `a` and `b` point to the same object.
c=10
print(id(c)) #140706471363696

# here it will check the value of c and it will create a new object in memory because 10 is not present in memory
# but for a and b it will check the value 5 and it will find that 5 is already present in memory so it will point to the same object in memory.
#  if the value is not present in memory then it will create a new object in memory and it will point to that object.

# if the value of the variable is changed then it will create a new object in memory and it will point to that object.
# the older value or object will be garbage collected by the garbage collector if there are no references to it.
# so the memory management in Python is done by the memory manager and garbage collector.


# STRING INTERNING
# ---------------------------
# Python automatically interns some strings for memory efficiency. This means that identical string literals may point to the same memory location.
str1 = "hello"
str2 = "hello"
print(id(str1)) # 140706471364432
print(id(str2)) # 140706471364432
# Both `str1` and `str2` point to the same interned string object "hello".

# but it doesn't intern all strings, especially if they are created dynamically or contain special characters.
str3 = "hello world of python programming"
str4 = "hello world of python programming"
print(id(str3)) # 140706471364528
print(id(str4)) # 140706471364998
# In this case, `str3` and `str4` may point to different objects