# importing the required greet function from functions1.py
from functions1 import greet

# importing the whole functions1.py module as f1
import functions1 as f1


print(greet("Anshu"))
print(f1.greet("Rahul"))
print(f1.operate(15, 23))