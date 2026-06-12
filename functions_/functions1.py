'''
A **function** is a block of code that performs a specific task and can be used multiple times.

### Why do we use functions?

Imagine you need to print `"Hello Anshu"` 100 times.

Without a function:

```python
print("Hello Anshu")
print("Hello Anshu")
print("Hello Anshu")
# ... 100 times
```

With a function:

```python
def greet():
    print("Hello Anshu")

greet()
greet()
greet()
```

You write the code once and use it many times.

---

### How do we create a function?

```python
def greet():
    print("Hello")
```

Here:

* `def` → keyword used to create a function
* `greet` → function name
* `()` → parentheses
* `:` → start of function body

To run it:

```python
greet()
```

Output:

```text
Hello
```

---

### Function with input (parameters)

```python
def greet(name):
    print("Hello", name)

greet("Anshu")
greet("Rahul")
```

Output:

```text
Hello Anshu
Hello Rahul
```

---

### Function that returns a value

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

### Where are functions used?

Functions are used everywhere in Python:

#### 1. Calculations

```python
def square(x):
    return x * x
```

#### 2. Machine Learning

```python
model.fit()
model.predict()
```

#### 3. Web Development

```python
def login():
    pass
```

#### 4. Games

```python
def move_player():
    pass
```

#### 5. Data Analysis

```python
def clean_data():
    pass
```

---

### Built-in Functions

Python already provides many functions:

```python
print("Hello")
len("Anshu")
type(10)
input()
```

These are all functions.

---

### Interview Definition

**A function is a reusable block of code that performs a specific task. It helps reduce code repetition, improves readability, and makes programs easier to maintain.**

'''



'''
In Python, functions are commonly divided into **2 main types**:

### 1. Built-in Functions

These are already provided by Python.

Examples:

```python
print("Hello")
len("Anshu")
type(10)
input()
max(10, 20, 30)
```

Here, `print()`, `len()`, `type()`, `input()`, and `max()` are built-in functions.

---

### 2. User-defined Functions

These are functions created by the programmer using `def`.

Example:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

### More Detailed Classification

Many interviewers also classify functions into:

1. Built-in Functions
2. User-defined Functions
3. Lambda (Anonymous) Functions
4. Recursive Functions
5. Generator Functions

#### Lambda Function

```python
square = lambda x: x * x
print(square(5))
```

#### Recursive Function

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
```

#### Generator Function

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

---

### For Exams (Short Answer)

**Types of functions in Python:**

1. Built-in Functions
2. User-defined Functions

### For Interviews (Detailed Answer)

**Functions in Python can be categorized as:**

1. Built-in Functions
2. User-defined Functions
3. Lambda Functions
4. Recursive Functions
5. Generator Functions

If you're learning Python fundamentals, focus first on **built-in** and **user-defined** functions. Those are the foundation for everything else.

'''



'''
User-defined functions are often classified based on **arguments (parameters)** and **return values**.

There are **4 common types**:

### 1. No Arguments, No Return Value

```python
def greet():
    print("Hello")

greet()
```

* Takes no input.
* Returns nothing.

---

### 2. Arguments, No Return Value

```python
def greet(name):
    print("Hello", name)

greet("Anshu")
```

* Takes input.
* Returns nothing.

---

### 3. No Arguments, Return Value

```python
def get_number():
    return 100

num = get_number()
print(num)
```

* Takes no input.
* Returns a value.

---

### 4. Arguments and Return Value

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

* Takes input.
* Returns a value.

---

### Interview/Exam Answer

**Types of User-Defined Functions:**

1. Function without arguments and without return value.
2. Function with arguments and without return value.
3. Function without arguments and with return value.
4. Function with arguments and with return value.

These 4 types are the most commonly asked classification in Python exams and interviews.
'''


def greet(name):
    return f"Hello, {name}!"

def operate(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Baboi"))
    print(operate(10, 20))

# python functions_/functions1.py