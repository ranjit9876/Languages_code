# # '''''''''''''''''''''1.To Find the Memory Address of Integer Data Types by id()''''''''''''''''''''''''''''
# '''(function) def id(__obj: object,/) -> int'''
# # id(__obj: object) -> int; Return the identity of an object

# num1 = 3
# # Return the identity of an int data type.
# print(f"Memory Address of Integer Data Type {num1}: {id(num1)}")

# str1 = 'Ranjit Kumar Gupta'
# # Return the identity of an str data type
# print(f"Memory Address of String Data Type, {str}: {id(num1)}")

# x = 5
# y = 5
# z = [1, 2, 3]

# print(id(x))  # Print the id of variable x
# print(id(y))  # Print the id of variable y (which will be the same as x)
# print(id(z))  # Print the id of list z
# # '''''''''''''''
# # Define a function that takes an object and returns its id


# def get_object_id(__obj: object):
#     return id(__obj)


# # Creates some objects
# x = 10
# y = 20
# z = [10, 20]
# str1 = "Hello, world!"

# # Get and print the id of these objects
# x_id = get_object_id(x)
# y_id = get_object_id(y)
# z_id = get_object_id(z)
# str1_id = get_object_id(str1)

# print(f'id of x: {x_id}')
# print(f'id of y: {y_id}')
# print(f'id of z: {z_id}')
# print(f'id of str1: {str1_id}')

# # Check if tho objects have the same identifier
# if (x_id == y_id):
#     print(f"{x} and {y} have the same identifier")
# else:
#     print(f"{x} and {y} have the different identifier")

# if (x_id == z_id):
#     print(f"{x} and {z} have the same identifier")
# else:
#     print(f"{x} and {z} have the different identifier")

# # ''''''''''''''''id() for competitive programming''''''''''''''
# # Import defaultdict from collections module
# # Function to find the number of unique objets in a list

# from collections import defaultdict
# def count_unique_objects(arr):
#     unique_ids = set()

#     count_dict = defaultdict(int)
#     print(count_dict)

#     for obj in arr:
#         obj_id = id(obj)
#         if obj_id not in unique_ids:
#             unique_counts.add(obj_id)
#             count_dict[obj_id] += 1
#     return count_dict


# if __name__ == '__main__':
#     # Sample list of objects
#     objects = [1, 2, 3, 2, 4, 5, 3, 'apple', 'bannana', 'apple']

#     # Count the number of unique objects and their occurrences
#     unique_counts = count_unique_objects(objects)
#     for obj_id, count in unique_counts.items():
#         obj = [item for item in objects ]

# # ''''''''''''''''''''
# class ObjectManager:
#     def __init__(self):
#         self.objects = {}
#         self.counter = 0

#     def create_object(self, data):
#         # Generate a unique ID for the object
#         unique_id = self.counter
#         self.counter += 1

#         # Store the object with its unique ID
#         self.objects[unique_id] = data

#         return unique_id

#     def get_object(self, unique_id):
#         # Retrieve an object by its unique ID
#         return self.objects.get(unique_id, None)

# # Create an instance of ObjectManager
# object_manager = ObjectManager()

# # Create some objects and get their unique IDs
# id1 = object_manager.create_object([1, 2, 3])
# id2 = object_manager.create_object("Hello, World!")
# id3 = object_manager.create_object(42)
# id4 = object_manager.create_object(42)
# # Get objects by their unique IDs
# object1 = object_manager.get_object(id1)
# object2 = object_manager.get_object(id2)
# object3 = object_manager.get_object(id3)
# object4 = object_manager.get_object(id4)

# # Print the unique IDs and objects
# print(f"Unique ID 1: {id1}, Object 1: {object1}")
# print(f"Unique ID 2: {id2}, Object 2: {object2}")
# print(f"Unique ID 3: {id3}, Object 3: {object3}")
# print(f"Unique ID 4: {id4}, Object 4: {object4}")


# # # ''''''''''''''''''''''''2.Assingning The Singal and  Multiple Values at the same time''''''''''''''''''''''''''
# # num1  = 10 # Assigning the integer value to num variable
# # print(type(num1)) # <class 'int'>

# # num2: str = 10
# # print(type(num2)) # <class 'int'>
# # print(num2)

# # a, b, c = 10, 20, 30
# # print(f'a= {a}, b= {b}, c= {c}')

# # a, b, c = 10, 'ChatGPT', 3.0
# # print(f'a= {a}, b= {b}, c={c}')

# # Unpacking Sequence: unpack values from sequences like lists or tuples into multiple variables.
# l1 = [1,2,3]
# x,y,z = l1
# print(f'x= {x}, y= {y}, z= {z}')

# # Swaping variables:
# x, y = 10, 20
# x, y = y, x
# print(f'x= {x}, y= {y}')

# # Extended Unpacking: extended unpacking using the * operator to capture multiple values into a single variable.
# l1 = [1,2,3,4,5,6,7,8,9,10,"Hello world!"]
# first, *rest = l1
# print(f'first: {first}, rest: {rest}')
# print(f'l1: {l1}')
# first, second, *rest = l1
# print(f'first: {first}, second: {second}, rest: {rest}')

# first, *middle, last = l1
# print(f'first: {first}, middle: {middle}, last: {last}')

# # Using extended unpacking for function return values.
# def get_numbers():
#     return 1,2,3,4,5,6,7,8,9,10,11,"hello world"

# first, second, *rest = get_numbers()
# print(f'first: {first}, second: {second}, rest: {rest}')

# # Unpacking in the functional argument
# def add(a,b):
#     return a + b

# values = (1,2)
# sum = add(*values) # unpack the tuple
# print(f'sum: {sum}')

# # '''''''''''''''''''''''''''''''''''''''Unlimited Size of int''''''''''''''''''''''''''''''''''''''''''
# # 1.Performing Operations with Large Integer'''''''''''''''''
# import math
# a = 10 ** 20  # very large integer
# b = 20 ** 100  # another big integer
# # print(a + b)

# # 2. Exponentiation with large Integer
# num = 2 ** 1000
# print(num)

# # 3.Factorial Calculations
# num = 1000  # Calculate 1000!
# result = math.factorial(num)
# print(result)

# # 4.Modular Arithmetics
# a = 10**50
# b = 7
# mod = 1000000007 # A Common Modulo value
# # Calculate (a ^ b) % mod
# result = pow(a,b,mod)
# print(result)

# # 5.Factorization with Large Primes:
# import sympy

# large_prime = sympy.nextprime(10 ** 100)  # Find the next prime larger than 10^100
# print(f'large_prime: {large_prime}')

# # 6.Large Summation
# large_list = [10 ** 18] * 10**6
# total_sum = sum(large_list)  # Efficiently sum a large list of integers
# print(total_sum)

# # 7.Prime Number Generation
# import sympy

# n = 10**100
# primes = list(sympy.primerange(n, n + 100))
# print(primes)

# # ''''''''''''''''''''''''''''''''''''Numeric Operations''''''''''''''''''''''''''''''''''
# # 1.Addition
# a, b = 10, 15
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #Division(Float-Point Division)
# print(a//b) # Integer Division(Floor Division)
# print(a%b) # Modulus(Remainder)
# print(a ** b) # Exponentiation
# print(abs(-10)) # Absolute Value
# print(max(a,b))

# #''''''''''''''''''''''''Bitwise Operations''''''''''''''''''''''''''''''
# a = 5  # Binary: 101
# b = 3  # Binary: 011

# # Bitwise AND
# result_and = a & b  # result_and is 1 (Binary: 001)

# # Bitwise OR
# result_or = a | b  # result_or is 7 (Binary: 111)

# # Bitwise XOR
# result_xor = a ^ b  # result_xor is 6 (Binary: 110)

# # Left shift
# result_left_shift = a << 2  # result_left_shift is 20 (Binary: 10100)

# # Right shift
# result_right_shift = a >> 1  # result_right_shift is 2 (Binary: 10)

# # '''''''''''''''''''''''Rounding and Floor''''''''''''''''''''
# import math

# x = 3.75

# # Round to the nearest integer
# rounded_value = round(x)  # 4

# # Floor value (round down)
# floor_value = math.floor(x)  
# num1 = 10
# print(num1.bit_length())

# # '''''''''''''''''''''''''Converion''''''''''''''''
# # String to int
# str1 = '42'
# num = int(str1, 10)

# # Float to int
# float_number = 3.14
# num2 = int(float_number)
# num3 = int(float_number)    
# print(num2, num3)

# # Converting int to str
# num = 10
# str1 = str(num)
# print(str1)

# # Convertig int to float
# num = 15
# float_number = float(num)
# print(float_number)

# # Convert Hexadecimal or Binary  to int
# hex_string = "1A"  # Hexadecimal representation
# int_from_hex = int(hex_string, 16)  # Result: 26
# print(int_from_hex)

# binary_string = "1010"  # Binary representation
# int_from_Binary = int(binary_string, 2)
# print(int_from_Binary)

# # Convert Character to int
# ch ='A'
# num = ord(ch)
# print(num)

# # Convert Integer to Characer
# num =10
# ch = chr(num)

# # Convert List of the String to the List of Integer
# l1 = ['1', '2', '3']
# l2 = [int(x) * 10 for x in l1]
# print(l2)

# # Convert integer to Binary Strings
# num = 15
# binary_str = bin(num)[0:].zfill(4)
# # binary_str = binary_str.lstrip('0b')
# print("Actual Binary Representation: " + binary_str)