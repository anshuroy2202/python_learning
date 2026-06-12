a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")

# Swapping without using a temporary variable
a = 5
b = 10

# here packing and unpacking of tuple is happening
x=b,a  # packed
print(x)
a, b = b, a    #unpacked
print(f"After swapping: a = {a}, b = {b}")

# swapping using arithmetic operations
a = 5
b = 10
a = a + b  # a now holds the sum of a and b
b = a - b  # b now holds the original value of a
a = a - b  # a now holds the original value of b
print(f"After swapping: a = {a}, b = {b}")


# swapping using the bitwise operators
a=5
b=10

a=a^b
b=a^b
a=a^b
print(f"After swapping: a = {a}, b = {b}")
