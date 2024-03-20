# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''Function Parameters'''''''''''''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''1.Positional Parameters'''''''''''''''
# def fun(x, y):
#     return x + y
# result  = fun(10, 20) # x = 10, y = 20
# print(f'result = {result}')

# # '''''''''''''''2.Default Parameters'''''''''''''''''''''
# '''Default parameters have predefined values, and if a value is not provided when calling the function, the default value is used.'''
# '''They are specified using the assignment operator = in the function definition.'''
# def fun(name = "Charlie"):
#     print(f'name = {name}')
# fun() # Use the default value is "Charlie"
# # fun("John")

# # ''''''''''''''''''3.Keyword Parameters''''''''''''''''''''
# '''Keyword parameters allow you to specify values for function parameters by name, rather than by position.'''
# def divide(dividend, divisor):
#     return dividend / divisor
# result = divide(dividend=15, divisor=4) # Using Keyword Parameters
# print(f'result = {result}')

# # '''''''''''''''4.Arbitary Positional Parameters(*args)'''''''''''''''
# '''Sometimes, you might want to pass a variable number of positional arguments to a function.'''
# '''You can use *args to collect any number of positional arguments into a tuple within the function.'''
# def sum_all(*args):
#     return sum(args)
# result = sum_all(1, 2, 3, 4) # args = (1, 2, 3, 4)
# print(f'resum = {result}')

# # '''''''''''''5.Arbitary Keyword Parameters(*kwargs)''''''''''''''''''''''''''''
# '''Similar to *args, **kwargs allows you to pass a variable number of keyword arguments to a function.'''
# '''These arguments are collected into a dictionary within the function.'''
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}:{value}')
# display_info(name = 'Alice', age = 30, city = 'New York')

# # '''''''''''''''''6.Mixing Parameter Types''''''''''''''''''''''''''
# '''You can use a combination of positional, default, keyword, *args, and **kwargs parameters in a single function definition.'''
# '''Be mindful of the parameter order, as positional and keyword parameters should come before *args and **kwargs.'''
# def complex_fun(a , b = 0, *args, x = 1, y = 2, **kwargs):
#     # Function Body Here
#     pass
# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''Advanced Positional Parameters in Sorting'''''''''''''''''''''''''''''
# students = [("Alice", 10), ("Bob", 88), ("Charlie", 92)]

# def sort_students_by_grade(student):
#     name, grade = student
#     return -grade, name  # Sort by descending grade, then ascending name

# sorted_students = sorted(students, key=sort_students_by_grade)
# print(sorted_students)

# # '''''''''''Using Lambda function with Positional Parameters
# '''Lambda functions are handy for short functions that take positional parameters.'''
# numbers = [1, 5, 3, 9, 2, 8]

# # sort in descending order
# # sorted_number = sorted(numbers, key=lambda x: x) # Asscending order
# sorted_number = sorted(numbers, key=lambda x: x) # Descending order
# print(f'sorted numbers = {sorted_number}')

# # ''''''''''''''''''''''Returning Multiple Values'''''''''''''''''''
# def divide_remainder(dividend, divisor):
#     quotent = dividend // divisor
#     remainder = dividend % divisor
#     return quotent, remainder

# quotent, remainder = divide_remainder(23, 7)
# print(f'quotent = {quotent}')
# print(f'remainder = {remainder}')

# # '''''''''''''''''''''''''''Arbitrary Arguments with Other Parameters:'''''''''''''''''''
# '''Combine arbitrary positional parameters with regular positional parameters in a function.'''
# def process_data(header, *data):
#     print("Header:", header)
#     print("Data:", data)

# # Usage
# process_data("ID", 101, 102, 103)
# # Output:
# # Header: ID
# # Data: (101, 102, 103)

# # ''''''''''''''''''''''Combining Arbitrary Arguments with Keyword Arguments:'''''''''''''''''''
# def display_info(*args, **kwargs):
#     print("Positional Arguments:", args)
#     print("Keyword Arguments:", kwargs)

# # Usage
# display_info(1, 2, name="Alice", age=30)

# # '''''''''''''''''''''''''''Unpacking Sequences as Arguments:''''''''''''''
# '''You can use the * and ** operators to unpack sequences (lists, tuples, dictionaries) as function arguments.'''
# def greet_all(*names):
#     for name in names:
#         print(f"Hello, {name}!")
# names = ["Alice", "Bob", "Charlie"]
# greet_all(*names)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''Function Return'''''''''''''''''''''''''''''''
# '''''''''''1.Basic Return Statements'''''''''''''''''''''''
def add(x, y):
    result = x + y
    return result

sum_result = add(3, 5)
print("Sum:", sum_result)  # Output: 8

# ''''''''''''''''''''2.Return Multiple Values'''''''''''''''
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(10, 3)
print("Quotient:", q)  # Output: 3
print("Remainder:", r)  # Output: 1

# '''''''''''''''''''''''''3.Returning Eary from a Function'''''''''''''''''
'''Use return to exit a function early, even before reaching the end of the function.'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = is_even(25)
print(f'result = {result}')

# # '''''''''''''''''''4.Returning None'''''''''''''''''''
# def do_nothing():
#     print('Hii')
#     pass
# do_nothing()

def do_nothing():
    pass
result = do_nothing()
print(f'result = {result}') # Output: None

# '''''''''''''''''''''''''5.Returning Early with a condition
def is_positive(number):
    if number > 0:
        return True
    return False # Implict Return None for negative or Zero Number

print(f'result = {is_positive(10)}') # Output: True
print(f'result = {is_positive(-10)}') # Output: False

# '''''''''''''''''''''''''6.Returning in a Loop'''''''''''''''''''''''''''
'''Using return within a loop to exit the function when a condition is met.'''
def find_first_negative(numbers):
    for num in numbers:
        if num < 0:
            return num
    return None  # Return None if no negatives are found

# Usage
result = find_first_negative([1, 2, -3, 4, -5])
print("First Negative:", result)  # Output: -3

# '''''''''''''''''''''''''7.Returning a Function as an Object
def get_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_two = get_multiplier(2)
result = times_two(5)
print(f'result = {result}')

# '''''''''''''''''''''''''''''8.Returning Lambda function
def get_power_function(power):
    return lambda x: x ** power

square = get_power_function(2)
cube = get_power_function(3)

result_1 = square(5)
result_2 = cube(5)
print(f'result_1 = {result_1}')
print(f'result_2 = {result_2}')

# '''''''''''''''''''''9.Return Multiple Values as Named Tuples
'''se named tuples to return multiple values with named fields.'''
from collections import namedtuple
def get_person_info(name, age):
    Person = namedtuple('Person_Info',['name', 'age'])
    return Person(name, age)

Person_1 = get_person_info('Alice', 25)
print(f'Person_1 = {Person_1}')
print(f'Person_1.name = {Person_1.name}')
print(f'Person_1.age = {Person_1.age}')

# ''''''''''''''''''''''''10.Retruning Decorator Functions
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        result = func('Alice', **kwargs)
        print('After function call')
        func('Bob', **kwargs)
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f'Hello, {name}')

say_hello('Charlie')

# ''''''''''''''''''''''''''''11.Returning Generator Functions
'''Generators allow for lazy evaluation, returning values one at a time.'''
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a +b 
        
fib_gen = fibonacci_sequence(5)
for num in fib_gen:
    print(num, end=" ")

# ''''''''''''''''''Returning Custom Objects
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def create_rectangle(width, height):
    return Rectangle(width, height)

rect = create_rectangle(4, 5)
print("Area:", rect.area())  # Output: 20

# '''''''''''''''''''Returning Complex Data Structure
def get_student_data():
    Student = {
        'Alice' : {'age' : 20, 'grade' : 'A'},
        'Bob' : {'age' : 22, 'grade' : 'B'},
    }
    return Student

student_info = get_student_data()
print(student_info['Alice']['age']) # output: 20

# '''''''''''''''''''''''Returning Multiple Functions
def function_dispatch():
    def add(x, y):
        return x + y 
    
    def diff(x, y):
        return x - y
    
    return {'add' : add, 'diff' : diff}

address_of_func = function_dispatch
print(f'address_of_func: {address_of_func}') # Output: address_of_func: <function function_dispatch at 0x0000015E1BD3E200>

func = function_dispatch() # func == {'add' : add, 'diff' : diff}
print(f"func['add']: {func['add']}") # Output: func['add']: <function function_dispatch.<locals>.add at 0x000001DB1B38E2A0>
print(f"func['add'](15, 10): {func['add'](15, 10)}") # Output: 25

sum = func['add'](15, 10)
diff = func['diff'](15, 10)
print(f'sum = {sum}')
print(f'diff = {diff}')
