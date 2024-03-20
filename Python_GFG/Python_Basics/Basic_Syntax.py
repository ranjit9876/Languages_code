# # 1.Comments
# # This is a single line comment
# '''
# This is a 
# Multiple lines Comments
# '''

# # 2.Statements
# # Using Backslash(\)
# statement = "This is a very long sentence that we want to "\
#             "split over multiple lines for better readability."
# print(statement) #output; This is a very long sentence that we want to split over multiple lines for better readability.

# # for mathematical operations
# sum = 1 + 2 + 3 +\
#       4 + 5 + 6 +\
#       7 + 8 + 9
# print(sum) #output: 45

# # '''''''''''''
# # Using Parenthesis
# # Create list
# numbers = [1, 2, 3,
# 		4, 5, 6,
# 		7, 8, 9]

# def total(num1, num2, num3, num4):
#     print(num1+num2+num3+num4)

# # Function call
# total(23, 34,
# 	22, 21)
# # ''''''''''''''''Triple Quotes for String''''''''''''
# text = """GeeksforGeeks Interactive Live and Self-Paced
# Courses to help you enhance your programming.
# Practice problems and learn with live and online
# recorded classes with GFG courses. Offline Programs."""

# print(text)
# # '''''''''''''''''''Quotation in Python'''''''''''''''''''''
# # Embedded single quote inside double.
# text1 = "He said, 'I learned Python from GeeksforGeeks'"

# # Embedded double quote inside single.
# text2 = 'He said, "I have created a project using Python"'

# print(text1)
# print(text2)
# # '''''''''''''''''''''''''''''''''''''''''Continuation of Statements in Python''''''''''''''''''''''''''''''''
# # Implict Continuation 
# # Line continuation within square brackets '[]'
# numbers = [
# 	1, 2, 3,
# 	4, 5, 6,
# 	7, 8, 9
# ]

# # Line continuation within parenthesse '()'
# result = max(
# 	10, 20,
# 	30, 40
# )

# # Line continuation within curly braces '{}'
# dictionary = {
# 	"name": "Alice",
# 	"age": 25,
# 	"address": "123 Wonderland"
# }

# print(numbers)
# print(result)
# print(dictionary)
# # '''''''''''''''''Explict Continuation'''''''''''''''''
# # Explicit continuation
# s = "GFG is computer science portal " \
# 	"that that is used by geeks."

# print(s)
# # '''''''''''''''''''''''''''''''String''''''''''''''''''''''
# text = '''A Geek can help other
# Geek by writing article on GFG'''

# message = "Hello, " "Geeks!"

# print(text)
# print(message)
# # '''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 1.Printing
print("Hello, world!")

# 2.Variables and Data Types
x = 5 #integer
y = 5.8 #float
name = "John" #string
is_true = True #boolean

# 3.Comments
# This is a single line comment
'''This is 
Multiple 
Line Comment'''

"""This is 
Multiple 
Line Comment"""

# 4.List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 5.Tuples
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 6.Dictionaries
my_dict = {"name" : "Charlie", "age" : 22}

# 7.Condition
if (x > 0):
    print("x is positive")
elif(x == 0):
    print("x is zero")
else:
    print("x is negative")

# 8.loop
for i in range(5):
    print(i)

# 9.function
def fun(name):
    print(f"Hello, {name}")
fun("Charlie")

# 10.classes
class My_Class:
    def __init__(self, name):
        self.name = name
        
    def great(self):
        # print("Hello, " + self.name)
        print(f'Hello, {self.name}')

# # 11.File Handling
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
        
# 12.Exception Handling
try:
    result = 1
    # result = 10 / 10
    print("result: ", result)
except ZeroDivisionError as e:
    print("Can't divide by zero: ")

# 13.Importing module
import math
print(math.sqrt(81))

# 14.List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# 15.Lambda Function
square = lambda x: x**2 
print(square(10))

# 16.Map and Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(map(lambda x: x % 2 == 0, numbers))
evens_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)
print(evens)
print(evens_2)

# 17.Generators
def my_generator():
    yield 1
    yield 2
    yield 3

# 18.Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()
my_decorator(say_hello())

# 19.Classes and Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog's sound: Woof!")

# 20. Module Creation and Usage
# (See below)

# Example Module: mymodule.py
"""
def greet(name):
    print("Hello,", name)
"""
import mymodule
mymodule.great("Charlie")

# 21.String Manipulation
text = "Hello, world!"
print(text.upper())
print(text.lower())
substring = text[2:10]
print(substring)

# 22.Regular Expression
import re
pattern = re.compile(r'\d+')

# result_2 = pattern.match("abc123")
# if (result_2):
#     print("Pattern matched found")
# else:
#     print("Pattern not matched found")

if result_2 := pattern.match("abc123"):
     print("Pattern matched found")
else:
     print("Pattern not matched found")

# 23. Sets
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 24. Boolean Operations
and_result = True and False
or_result = True or False
not_result = not True

# 25. Date and Time
from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(current_time)
print(formatted_time)

# 26. list Slicing
my_lsit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sub_list = my_list[2: 6]
print(sub_list)

# 27. Zip function
names = ['Alice', 'Bob', 'Charlie']
ages = [22, 24, 26]
zipped_data = zip(names,ages)
print(zipped_data)

# 28. Enumerate function
for key, value in enumerate(zip(names,ages)):
    print(key, value)

for key, value in enumerate(names):
    print(key, value)

# 29. JSON Handling
import json
data = '{"name" : "Alice", "age" : 25}'
parsed_data = json.loads(data)
print(parsed_data)

# 30. Try-Except-Finally
try: 
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("Finally block always excuted")

# 31. List concatenation
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
my_list = l1 + l2
print(my_list)

# 32. Range Function
numbers = list(range(10))
print(numbers)

# 33. pass statement
def fun():
    pass

# 34. Global and Local Variables
global_var = 10

def my_fun():
    local_var = 15
    print(global_var + local_var)

# 35. Named Arguments
def print_info(name, age):
    # print(name + ": ", age)
    print(f'{name} : ', age)

# Example Call
print_info(age=25, name="Alice")

# 36. Mutable and Immutable
# List are mutable
l1 = [1, 2, 3, 4, 5]
l1[0] = 10
print(l1)

# Strings are immutable
name = "Alice"
# name[0] = 'A' #TypeError: 'str' object does not support item assignment
print(name)

# 37. List Methods
l1 = [1, 2, 3, 4, 5].append(6)
# l1.append(6)
print(l1) # [1, 2, 3, 4, 5, 6]
l1.extend([7,8,9])
print(l1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
removed_element = l1.pop(2) # remove element at 2nd position i.e 3
print(l1) # [1, 2, 4, 5, 6, 7, 8, 9]
print(removed_element) # 3

# 38. Dictionary Methods
my_dict = {'name' : 'Alice', 'age': 24}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print(keys) # dict_keys(['name', 'age'])
print(values) # dict_values(['Alice', 24])
print(items) # dict_items([('name', 'Alice'), ('age', 24)])

# 39.String Formatting
name = "Alice"
age = 25
print("Hello " + {name} + " You are " + {age} + " years old.") # Hello Alice. You are 25 years old.
print(f"Hello {name}. You are {age} years old.") # Hello Alice. You are 25 years old.
print(f"Hello {name}. You are {age} years old.") # Hello Alice. You are 25 years old.

# 40.Tuple Unpacking
coordinate = (1, 2, 3)
x, y, z = coordinate
print(f'x = {x}, y = {y}, z = {z}')

# 41. List Sorting
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()

# 42.File Writting 
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write('This is an example file.\n')
    file.write('This is the second line of the file.\n')
    file.write('This is the third line of the file.\n')

# 43. File Appending
with open("example.txt", "a") as file:
    file.write('This is the fourth line of the file.\n')

# 44. List Iteration 
l1 = [1, 2, 3, 4, 5]
for item in l1:
    print(item, end=" ")
print(end="\n")

# 45. Tuple packing
coordinate = 1, 2, 3
print(coordinate) # (1, 2, 3)

# 46. Shorthand ternary operator
result = 'positive' if x > 0 else 'negative'
print(result)
print(x)

# 47.Set Operations
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {3, 4, 5, 6, 7, 8, 9, 10}
intersection = set_1.intersection(set_2)
union = set_1.union(set_2)
difference = set_1.difference(set_2)
print(intersection, union, difference)
