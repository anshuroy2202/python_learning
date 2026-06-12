'''
Interview Definition

A statement is an instruction written in a Python program 
that the Python interpreter can execute. Statements are used 
to perform actions such as assignment, decision making, looping,
 importing modules, and function definition.


If you're studying Python fundamentals, statements are usually grouped like this:

### 1. Simple Statements

Statements written in a single line.

```python
a = 10
print(a)
x = y = z = 5
```

Examples:

* Assignment statement
* Import statement
* Pass statement
* Return statement
* Break statement
* Continue statement

---

### 2. Conditional Statements (Decision Making)

Used to make decisions.

```python
if x > 10:
    print("Greater")

if x > 10:
    print("Greater")
else:
    print("Smaller")

if x > 10:
    ...
elif x > 5:
    ...
else:
    ...
```

Types:

* `if`
* `if-else`
* `if-elif-else`
* Nested `if`

---

### 3. Looping (Iterative) Statements

Used to repeat code.

```python
for i in range(5):
    print(i)

while x > 0:
    x -= 1
```

Types:

* `for`
* `while`
* Nested loops

---

### 4. Jump / Control Transfer Statements

Change the normal flow of execution.

```python
break
continue
pass
return
```

---

### 5. Exception Handling Statements

Handle errors.

```python
try:
    x = 10 / 0
except:
    print("Error")
finally:
    print("Done")
```

Keywords:

* `try`
* `except`
* `else`
* `finally`
* `raise`

---

### 6. Function Definition Statements

```python
def add(a, b):
    return a + b
```

---

### 7. Class Definition Statements

```python
class Student:
    pass
```

---

### 8. Import Statements

```python
import math
from math import sqrt
```

---

### Exam-Oriented Classification

Most colleges teach Python statements in **3 main categories**:

1. **Sequential Statements** (normal execution)
2. **Selection Statements** (if, if-else)
3. **Iteration Statements** (for, while)

and separately discuss:

* Jump statements (`break`, `continue`, `pass`)
* Exception handling statements (`try`, `except`)

This is the classification most examiners expect when they ask about "types of statements in Python."


'''

# if else
# ---------------------------->
'''
Don't just memorize `if`, `else`, and nested `if`. Ask yourself:

**Can a program make decisions without them?**

The answer is **no**.

---

## Why do we need `if`?

`if` is used when you want code to run **only if a condition is true**.

Example:

'''
age=int(input('Enter the age'))

if age>=18:
    print("you are eligible for the voting")
else:
    print("you are not eligible for the voting")
'''


Question:
What if the age is 15?

Should Python still print "You can vote"?

No.

That's why we need `if`.

---

## Why do we need `else`?

`if` handles the **true** case.

But what about the **false** case?

Example:

'''

age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
'''


Now both possibilities are handled.

Think of it as:

```text
Condition True  → Do this
Condition False → Do that
```

Without `else`, you may not know what should happen when the condition is false.

---

## Why do we need `elif`?

Suppose there are more than two possibilities.

Example:

'''

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
'''


There are multiple outcomes, not just true or false.

That's why `elif` exists.

---

## Why do we need Nested `if`?

A nested `if` means an `if` inside another `if`.

We use it when a second decision should be checked **only after the first condition is true**.

Example:
'''
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
'''

Think carefully:

Would it make sense to check for a driving license if the person is only 10 years old?

No.

First check:

```text
Is age >= 18?
```

Only then check:

```text
Does the person have a license?
```

That's why nested `if` is useful.

---

## Real-World Example

ATM Machine:
'''

if card_is_valid:
    if pin_is_correct:
        if balance > amount:
            print("Withdraw successful")

'''
The machine doesn't jump directly to the balance check.

It checks conditions step by step.

---

## Summary

| Statement   | Why We Need It                                                       |
| ----------- | -------------------------------------------------------------------- |
| `if`        | Execute code only when a condition is true                           |
| `else`      | Handle the false case                                                |
| `elif`      | Handle multiple conditions                                           |
| Nested `if` | Check another condition only after a previous condition is satisfied |

The core idea is simple:

> Conditional statements allow a program to make decisions. Without them, every line of code would execute in the same way regardless of the input, and programs would not be intelligent or interactive.

'''



# why can't the multiple if can be used instead of the elif

'''
Yes, you **can** use multiple `if` statements instead of `elif`, but you need to understand the consequence.

Suppose you have:

```python
marks = 75

if marks >= 90:
    print("A")

if marks >= 70:
    print("B")

if marks >= 50:
    print("C")
```

Output:

```text
B
C
```

Because both conditions are true.

But if your goal is to assign **one grade only**, then this is wrong.

You should write:

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
```

Output:

```text
B
```

---

Now, if your conditions are completely independent, multiple `if`s are perfectly fine:

```python
age = 25

if age >= 18:
    print("Can vote")

if age >= 21:
    print("Can drink in some countries")

if age >= 25:
    print("Can rent some vehicles more easily")
```

Output:

```text
Can vote
Can drink in some countries
Can rent some vehicles more easily
```

Here, you **want all applicable messages**, so multiple `if`s are correct.

### Rule

Ask yourself:

> Should only one block execute?

Use `if-elif-else`.

> Can multiple blocks execute?

Use multiple `if` statements.

That's the real difference—not syntax, but the logic you want in the program.


---------------------------------------------------->
Yes, that's another important difference: **execution time**.

Consider this:

```python
marks = 95

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
```

What happens?

1. Python checks `marks >= 90` → True.
2. Prints `"A"`.
3. **Stops checking the remaining conditions.**

So only **1 condition** is evaluated after a match is found.

---

Now look at multiple `if`s:

```python
marks = 95

if marks >= 90:
    print("A")

if marks >= 70:
    print("B")

if marks >= 50:
    print("C")
```

What happens?

1. Checks `marks >= 90` → True.
2. Checks `marks >= 70` → True.
3. Checks `marks >= 50` → True.

Python evaluates **all conditions**, even after finding a true one.

---

### Time Difference

For 3 conditions, the difference is tiny.

But imagine:

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
...
elif condition1000:
    ...
```

If `condition1` is true, Python stops immediately.

With 1000 separate `if`s:

```python
if condition1:
    ...

if condition2:
    ...

if condition3:
    ...
```

Python may check all 1000 conditions.

So:

* `if-elif-else` → generally faster when only one outcome is needed.
* Multiple `if`s → necessary when multiple actions may need to run.

---

### Major Difference Summary

| Multiple `if`                       | `if-elif-else`                         |
| ----------------------------------- | -------------------------------------- |
| Checks every condition              | Stops at first true condition          |
| Multiple blocks can execute         | Only one block executes                |
| Can take more time                  | Usually more efficient                 |
| Use when conditions are independent | Use when choosing one option from many |

The **main reason** to choose `elif` is usually **logic (one choice only)**. The performance benefit is real, but in most beginner programs it's much less important than getting the logic correct.
'''



# MATCH
# -------------------------------->
# there is no switch-case like c in python
# match-case was introduced in Python 3.10. It is similar to the switch-case statement in languages like C, C++, and Java.


'''
`match-case` was introduced in **Python 3.10**. It is similar to the **switch-case** statement in languages like C, C++, and Java.

## Why do we need `match-case`?

Suppose you have many `elif` conditions:

'''

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
'''


This becomes long and difficult to read.

Using `match-case`:

'''

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
'''


Output:

```text
Wednesday
```

---

## Syntax

```python
match expression:
    case value1:
        statements

    case value2:
        statements

    case _:
        default statements
```

The `_` means:

> "If no case matches, execute this."

Similar to `else`.

Example:

'''

day = 10

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")
'''


Output:

```text
Invalid Day
```

---

## Rules

### Rule 1: Python 3.10+

`match-case` works only in Python 3.10 and above.

Check your version:

'''

import sys
print(sys.version)
'''

---

### Rule 2: `match` comes first

```python
match value:
    case 1:
        ...
```

Not:

```python
case 1:      # ❌ Invalid
```

---

### Rule 3: Indentation is required

```python
match x:
    case 1:
        print("One")
```

---

### Rule 4: Use `_` as the default case

```python
case _:
    print("Default")
```

---

## Multiple Values in One Case
'''
day = 1

match day:
    case 1 | 7:
        print("Weekend")
    case _:
        print("Weekday")
'''


The `|` means OR.

---

## Matching Strings

'''
color = "red"

match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case _:
        print("Unknown")
'''

---

## When to Use It?

Use `match-case` when:

* Comparing one variable against many fixed values.
* Replacing long `if-elif-else` chains.
* Making code cleaner and easier to read.

Use `if-elif-else` when:

* Conditions involve ranges (`age > 18`)
* Conditions involve logical operators (`and`, `or`)
* Complex comparisons are needed.

For example:

```python
if age > 18 and salary > 50000:
    ...
```

This is usually better with `if`, not `match`.

---

### Interview Definition

**`match-case` is a pattern matching statement introduced in Python 3.10 
that allows a value to be compared against multiple patterns and executes 
the code block of the first matching case.
 It is used as an alternative to long `if-elif-else` chains.**



 Yes, you **can use floats** in `match-case`.

Example:

'''
num = 3.14

match num:
    case 3.14:
        print("Pi")
    case 2.71:
        print("Euler")
    case _:
        print("Unknown")
'''

Output:

```text
Pi
```

However, there's a catch.

Floats can have **precision issues**:

'''
x = 0.1 + 0.2

print(x)
'''

Output:

```text
0.30000000000000004
```

Now:

'''
match x:
    case 0.3:
        print("Matched")
    case _:
        print("Not Matched")
'''

Output:

```text
Not Matched
```

because `0.30000000000000004` is not exactly equal to `0.3`.

So while Python allows floats in `case` patterns, it's often safer to use:

'''
if abs(x - 0.3) < 1e-9:
    print("Matched")
'''

### Rule of thumb

✅ Good for:

```python
match temperature:
    case 36.5:
        ...
    case 37.0:
        ...
```

⚠️ Be careful when the float comes from calculations like:

'''
0.1 + 0.2
10 / 3
math.sqrt(2)
'''

because exact matching may fail due to floating-point representation.

'''