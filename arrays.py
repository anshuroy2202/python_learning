'''
This is exactly the right question to ask. Don't start by memorizing arrays. Ask:

> If Python already has lists, why do arrays exist?

## First, Why Do We Need Arrays?

Imagine storing marks of 1,000 students.

Without an array or list:

```python
m1 = 80
m2 = 75
m3 = 90
...
m1000 = 85
```

This is impossible to manage.

So we need a data structure that can store **many values under one name**.

That's the basic idea behind arrays.

---

## What is an Array?

An **array** is a collection of elements of the **same data type** stored together.

Example:

```python
from array import *

arr = array('i', [10, 20, 30, 40])
```

Here all elements are integers.

---

## Then Why Does Python Have Lists?

Python's list is much more powerful.

```python
lst = [10, 20, "Anshu", 3.14, True]
```

A list can store different data types together.

An array cannot.

---

## Major Differences

| Array                   | List                        |
| ----------------------- | --------------------------- |
| Same data type only     | Multiple data types allowed |
| Less memory usage       | More memory usage           |
| Faster for numeric data | Slightly slower             |
| Need `array` module     | Built into Python           |
| Mainly for numbers      | General-purpose             |

---

## Example

### List

```python
lst = [10, "Anshu", 3.14]
```

Valid.

### Array

```python
from array import *

arr = array('i', [10, 20, 30])
```

Valid.

```python
arr = array('i', [10, "Anshu", 30])
```

❌ Error because `"Anshu"` is not an integer.

---

## Why Use Arrays If Lists Exist?

This is the real question.

### Reason 1: Memory Efficiency

Suppose you store 1 million integers.

A list stores:

* The integer objects
* References to those objects

An array stores:

* Only the raw integer values

Therefore arrays use less memory.

---

### Reason 2: Faster Numeric Operations

For large numerical datasets:

```python
from array import *

arr = array('i', range(1000000))
```

Arrays are generally more efficient than lists.

---

### Reason 3: Scientific Computing

Libraries such as:

* [NumPy](https://numpy.org/?utm_source=chatgpt.com)

use specialized arrays because they are much faster for mathematical operations.

Example:

```python
import numpy as np

a = np.array([1, 2, 3])
```

In Machine Learning, Data Science, and AI, you'll mostly work with NumPy arrays rather than Python lists.

---

## Why Do Most Python Beginners Rarely Use `array`?

Because Python lists already solve most problems:

```python
marks = [80, 75, 90, 88]
```

This is simple and convenient.

That's why Python developers often use:

* Lists for general programming
* NumPy arrays for scientific computing

The built-in `array` module is less commonly used.

---

## Interview Answer

**An array is a data structure that stores multiple elements of the same data type in contiguous memory locations. Arrays are used because they are more memory-efficient and faster for numerical data. Although Python lists can also store multiple values, lists consume more memory and allow mixed data types, whereas arrays are optimized for storing homogeneous data.**

'''

from array import *
# print(dir(array))
# print(help(array))

# arr=array([1,2,3])  TypeError: array() argument 1 must be a unicode character, not list
arr=array('i',[1,2,3])
print(f"Array:{arr}, Type:{type(arr)}") 
print(f"List:{arr.tolist()}, Type:{type(arr.tolist())}")

print('Buffer:',arr.buffer_info())

for num in arr:
    print(f'number:{num} , id:{id(num)}')


# float
arr = array('f', [1.5, 2.7, 3.9, 4.2])
print(f"Array:{arr}, Type:{type(arr)}") 

# double
arr = array('d', [1.5, 2.7, 3.9])  

# string
# The array module does not support strings.

arr = array('u', ['A', 'B', 'C'])
# Actually, 'u' supports single Unicode characters, not full strings.

arr = array('u', 'ABC')
print(arr)

# array('u', ['Anshu', 'Rahul']) TypeError: array item must be unicode character


'''
`buffer_info()` is a method of the Python **array** module.

It gives information about the memory buffer used by the array.

### Syntax

```python
array_name.buffer_info()
```

### Example

```python
from array import *

arr = array('i', [10, 20, 30, 40])

print(arr.buffer_info())
```

Output (example):

```python
(2456789123456, 4)
```

The output is a tuple containing:

```text
(memory_address, number_of_elements)
```

---

### Understanding the Output

Suppose:

```python
(2456789123456, 4)
```

* `2456789123456` → Starting memory address of the array.
* `4` → Number of elements in the array.

---

### Accessing Individual Values

```python
from array import *

arr = array('i', [10, 20, 30, 40])

address, size = arr.buffer_info()

print("Address:", address)
print("Size:", size)
```

Output:

```text
Address: 2456789123456
Size: 4
```

---

### Why is it Used?

Mostly for:

* Low-level memory operations
* Interfacing with C/C++ code
* Understanding how arrays are stored internally

For normal Python programming, Machine Learning, Web Development, etc., you will almost never use `buffer_info()`.

---

### Interview Answer

**`buffer_info()` is a method of the array module that returns a tuple containing the memory address of the array buffer and the number of elements stored in the array. It is mainly used for low-level memory-related operations.**
'''

print(50*'-')
# same like list array also creates the object 

def compare_array(a1,a2):
    print(20*'|')
    print(f'Before change: a1:{a1} a2:{a2}')
    if a1 is a2:
        print('Same reference to the object')
    else:
        print("They are not refereing the same object")
    print(f'ID a1:{id(a1)} a2:{id(a2)}')

    a2[3]=400
    print(f'After change at a2[3]: a1:{a1} a2:{a2}')

# SAME REFERENCE
a1=array('i',[1,2,3,4,5])
a2=a1
compare_array(a1,a2)

# COPY OF ARRAY
a3=array('i',[1,2,3,4,5])
a4=array(a3.typecode,a3.tolist())
compare_array(a3,a4)
# but here while converting that array into the list also takes the memory  hence it is not the optimised one


a4=array(a3.typecode,(n for n in a3))
compare_array(a3,a4)
