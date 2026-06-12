'''
Before learning modules, think about this:

If your Python program becomes **5,000 lines long**, would you keep everything in one file?

Probably not. It would be difficult to read, debug, and reuse.

That's why Python has **modules**.

## What is a Module?

A **module** is simply a Python file (`.py`) that contains code such as:

* Functions
* Variables
* Classes

which can be reused in other Python programs.

For example, suppose you have a file named:

```text
calculator.py
```

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

This file itself is a **module**.

---

## How to Use a Module?

```python
import calculator

print(calculator.add(10, 20))
```

Output:

```text
30
```

---

## Why Do We Use Modules?

### 1. Code Reusability

Write once, use many times.

### 2. Better Organization

Keep related code in separate files.

### 3. Easier Maintenance

Finding and fixing bugs becomes easier.

### 4. Team Development

Different developers can work on different modules.

---

## Built-in Modules

Python already provides many modules.

Examples:

```python
import math
print(math.sqrt(25))
```

```python
import random
print(random.randint(1, 10))
```

```python
import datetime
print(datetime.datetime.now())
```

---

## Different Ways to Import

### Import Entire Module

```python
import math

print(math.sqrt(16))
```

### Import Specific Function

```python
from math import sqrt

print(sqrt(16))
```

### Use Alias

```python
import math as m

print(m.sqrt(16))
```

---

## Module vs Function

| Module                     | Function                      |
| -------------------------- | ----------------------------- |
| A Python file              | A block of code inside a file |
| Can contain many functions | Performs a specific task      |
| Imported using `import`    | Called using function name    |

Example:

```text
calculator.py  ← Module
    add()      ← Function
    sub()      ← Function
    mul()      ← Function
```

## Interview Definition

**A module is a Python file containing functions, variables, and classes that can be imported and reused in another Python program. Modules help organize code and improve reusability.**

'''
from functions_.functions1 import greet, operate
print(greet("Anshu"))
print(operate(15, 23))


import math 
print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.pow(2, 3))
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.ceil(2.3))
print(math.floor(2.7))


# how to know the functions in math module?
print(dir(math))
print(help(math.sqrt))
print(help(math))


# it should be imported understand 
import functions_ as f_
print(dir(f_))  

import functions_.functions1 as f1_
print(dir(f1_)) 