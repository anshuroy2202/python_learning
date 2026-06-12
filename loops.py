'''
Before learning loops, ask yourself:

If you want to print `"Hello"` **100 times**, would you write:

```python id="j2xk0s"
print("Hello")
print("Hello")
print("Hello")
...
```

100 times?

That would be inefficient and hard to maintain.

That's why we use **loops**.

# What is a Loop?

A **loop** is a programming construct that repeatedly executes a block of code until a condition is met or a sequence is exhausted.

In simple words:

> A loop allows us to run the same code multiple times without rewriting it.

---

# Why Do We Use Loops?

### 1. Reduce Repetition

Without a loop:

'''
print(1)
print(2)
print(3)
print(4)
print(5)
'''

With a loop:

'''
for i in range(1, 6):
    print(i,end=" ")
'''

---

### 2. Process Large Amounts of Data

'''
names = ["Anshu", "Rahul", "Priya"]

for name in names:
    print(name,end="<->")
'''

---

### 3. Automate Repeated Tasks

'''
for i in range(100):
    print("Sending email")
'''

---

# Types of Loops in Python

Python has **2 main loops**.

## 1. `for` Loop

Used when you know what you want to iterate over.

### Syntax

```python id="ofz5m2"
for variable in sequence:
    statements
```

### Example

'''
for i in range(5):
    print(i,end=' ')
'''

Output:

```text id="34n84s"
0
1
2
3
4
```

---

### Iterating Through a List

```python id="pwp97v"
names = ["Anshu", "Rahul", "Priya"]

for name in names:
    print(name)
```

---

## 2. `while` Loop

Used when repetition depends on a condition.

### Syntax

```python id="8ik6um"
while condition:
    statements
```

### Example

'''
i = 1

while i <= 5:
    print(i)
    i += 1
'''

Output:

```text id="tkdf16"
1
2
3
4
5
```

---

# Difference Between `for` and `while`

| `for` Loop                       | `while` Loop                        |
| -------------------------------- | ----------------------------------- |
| Used for sequences               | Used for conditions                 |
| Number of iterations often known | Number of iterations may be unknown |
| Simpler for collections          | More flexible                       |

Example:
'''
for i in range(10):
    print(i)
'''

Known iterations: 10.

```python id="u1dzar"
while password != "admin":
    password = input("Enter Password: ")
```

Unknown iterations.

---

# Nested Loops

A loop inside another loop.

'''
for i in range(3):
    for j in range(2):
        print(i, j)
'''

Output:

```text id="j25eb7"
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# Loop Control Statements

### `break`

Stops the loop immediately.

'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''


Output:

```text id="k4nj5u"
0
1
2
3
4
```

---

### `continue`

Skips the current iteration.

'''
for i in range(5):
    if i == 2:
        continue
    print(i)
'''

Output:

```text id="bmr0hk"
0
1
3
4
```

---

### `pass`

Does nothing; acts as a placeholder.

'''
for i in range(5):
    pass
'''

---

# Interview Definition

**A loop is a control structure that repeatedly executes a block of code until a specified condition becomes false or until all elements of a sequence have been processed. Python mainly provides `for` and `while` loops for iteration.**

'''

# BREAK and CONTINUE
# ------------------------------->
'''
Before learning **break** and **continue**, think about this:

A loop normally executes until its condition becomes false.

'''
for i in range(10):
    print(i)
'''

Output:

```text
0
1
2
3
4
5
6
7
8
9
```

What if you want to stop at `5`?

That's where **break** comes in.

---

# 1. `break`

### Why do we use it?

To **exit a loop immediately** before it finishes naturally.

### Syntax

```python
break
```

### Example

'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''

Output:

```text
0
1
2
3
4
```

When `i` becomes `5`, Python exits the loop completely.

### Real-world Example

ATM PIN verification:

'''
correct_pin = "1234"

for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break
'''

As soon as the correct PIN is entered, there is no need to continue checking attempts.

---

# 2. `continue`

### Why do we use it?

To **skip the current iteration** and move to the next one.

### Syntax

```python
continue
```

### Example

'''
for i in range(5):
    if i == 2:
        continue
    print(i)
'''

Output:

```text
0
1
3
4
```

When `i` is `2`, Python skips the remaining code for that iteration and moves to the next value.

---

## Visual Difference

### `break`

'''
for i in range(5):
    if i == 2:
        break
    print(i)
'''

Output:

```text
0
1
```

Loop ends completely.

---

### `continue`

'''
for i in range(5):
    if i == 2:
        continue
    print(i)
'''

Output:

```text
0
1
3
4
```

Loop continues after skipping `2`.

---

## Simple Analogy

Imagine you're reading pages of a book.

### `break`

```text
Page 1 ✓
Page 2 ✓
Page 3 ✓
STOP READING
```

You close the book.

### `continue`

```text
Page 1 ✓
Page 2 ✓
Skip Page 3
Page 4 ✓
Page 5 ✓
```

You keep reading, but skip one page.

---

## Interview Answer

* **`break`** is used to terminate a loop immediately when a specific condition is met.
* **`continue`** is used to skip the current iteration and proceed with the next iteration of the loop.

### Key Difference

| Statement  | Effect                                                  |
| ---------- | ------------------------------------------------------- |
| `break`    | Exits the loop completely                               |
| `continue` | Skips only the current iteration and continues the loop |

'''
