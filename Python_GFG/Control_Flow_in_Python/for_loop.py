# l1 = [1,2,3,4,5]
# for value in l1:
#     print(value,end= " ")
# print()
    
# for i in range(len(l1)):
#     print(l1[i],end= " ")
# print()

# # '''''''''''''
# # Reading the number of elements in the sequence
# n = int(input())

# # Reading the sequence as a list of integers
# sequence = list(map(int, input().split()))

# # Iterating through the sequence using a for loop
# for item in sequence:
#     # Your code logic for each element goes here
#     # For example, you can perform some computation or comparison
#     # and print the result if needed.
#     print(item)

# # ''''''''''''''''''''''''''''''''''''''''''''''Iterating through sequence''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Iterate through a list
# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item, end= " ")
# print()

# # Iterate through a range
# for i in range(1, 5):
#     print(my_list[i], end= " ")
# print()
    

# # Iterate through characters in a string
# my_string = "Hello"
# for char in my_string:
#     print(char, end= " ")
# print()

# my_list = [1, 2, 3, 4, 5]
# for index, value in enumerate(my_list):
#     # Your code here, you can access both index and value
#     print(f'index: {index}, value: {value}')

# # 1.Using Zip for Multiple Sequence
# '''You can iterate through multiple sequences simultaneously using zip. For example, iterating through two lists:'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for item1, item2 in zip(l1, l2):
#     print(f'{item1}: {item2}')
# print()

# for item1, item2, item3 in zip('abcdefg', range(3), range(4)):
#     print(f'{item1}, {item2}, {item3}')
# print()

# # 2.Iterating Backward with reversed:
# for item in reversed(l1):
#     print(item, end=" ")
# print()

# # 3.Using itertools for Advanced Operations
# '''The itertools module provides various advanced iterators. 
# For instance, you can use itertools.permutations and itertools.combinations to iterate through'''
# from itertools import permutations, combinations

# l1 = [1,2,3,4,5]
# for prem in permutations(l1, 2):
#     print(prem, end=" ")
# print("Hello\n")

# for comn in combinations(l1, 2):
#     print(comn, end=" ")

# # ''''''''4.Generator Expressions for Efficiency''''''''''''''''
# '''Instead of creating a list, you can use generator expressions to iterate through elements without storing them in memory:'''
# l1 = [1,2,3,4,5,6,7,8,9,10]

# for item in [x for x in l1 if x % 2 == 0]:
#     print(item, end=" ")
# print()

# # '''''''''''''5.Iterating Over Sublist(Slicing)''''''''''''''''''''''''''''
# l1 = [1,2,3,4,5]
# for sublist in [l1[i:j] for i in range(len(l1)) for j in range(i + 1, len(l1) + 1)]:
#     print(sublist)

# # ''''''''''''''''''''''''''''''''''''''''''Iterating through String''''''''''''''''''''''''''''''''''''''''
# # Method 1: Using a for loop
# input_string = "Hello, World!"
# for char in input_string:
#     print(char)

# # Method 2: Using a while loop
# index = 0
# while index < len(input_string):
#     print(input_string[index])
#     index += 1

# # Method 3: Using list comprehension
# characters = [char for char in input_string]
# for char in characters:
#     print(char)

# # Method 4: Using enumerate to get both index and character
# for index, char in enumerate(input_string):
#     print(f"Index {index}: {char}")

# # Method 5: Using a custom generator function
# def custom_generator(string):
#     for char in string:
#         yield char

# gen = custom_generator(input_string)
# for char in gen:
#     print(char)
# # '''''''''''''''''''Specifying Start, Stop, and Step Values''''''''''''''''''''''''''''''''''''''''''
# # Using range with start, stop, and step values
# for i in range(0, 100, 2):
#     print(i)

# # Using a custom iterable
# custom_iterable = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# for num in custom_iterable:
#     print(num)

# # Using a while loop with a custom condition
# start_value = 7
# stop_value = 77
# step_value = 7
# current_value = start_value
# while current_value <= stop_value:
#     print(current_value)
#     current_value += step_value

# # Using a for loop with a list comprehension
# start = 1
# stop = 10
# step = 1
# result = [x for x in range(start, stop + 1, step)]
# print(result)

# # Using a for loop with a generator expression
# start_val = 3
# stop_val = 30
# step_val = 3
# gen = (x for x in range(start_val, stop_val + 1, step_val))
# for value in gen:
#     print(value)

# # reversing using slicing
# for i in range(10, 0, -1):
#     print(i)

# # '''''''''''''''''''''''''''''Nested For Loop'''''''''''''''''''
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col],end= " ")
#     print() # Print a new line after each row
    

# # Example 2: Generating combinations of elements
# from itertools import combinations

# arr = [1, 2, 3, 4]
# k = 2  # Size of combinations

# combinations_list = list(combinations(arr, k))

# for combo in combinations_list:
#     print(combo)

# # '''''''''''''''''''''''''''Loop Control Statements''''''''''''''''''''''''''''
# # Example: Finding the first prime number greater than 100 using break and else
# for num in range(101, 1000):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print("The first prime number greater than 100 is:", num)
#         break

# # Example: Skipping even numbers using continue
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i, end=' ')

# # Example: Using nested loops and labels
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 3 and j == 3:
#             break  # Breaks the inner loop
#         print(i, j)
#     else:
#         continue  # Continue the outer loop if the inner loop completes without a break
#     break  # Break the outer loop if the inner loop was broken

# # Example: Using while loop with break
# x = 1
# while x <= 10:
#     if x == 5:
#         break
#     print(x, end=' ')
#     x += 1

# # Example: Using while loop with else
# y = 1
# while y <= 5:
#     print(y, end=' ')
#     y += 1
# else:
#     print("Loop completed without a break")

# # Example: Infinite loop with a condition to break
# z = 1
# while True:
#     if z > 10:
#         break
#     print(z, end=' ')
#     z += 1

# # '''''''''''''''''''''''''''''''''''''''Iterating Dictionaries ''''''''''''''''''''''''
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print(key, my_dict[key], end=", ")
# print()
    
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in my_dict.items():
#     print(key, value,end=", ")
# print()

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict.keys():
#     print(key,end=" ")
# print()

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for value in my_dict.values():
#     print(value,end=" ")
# print()

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# [(key, value) for key, value in my_dict.items()]

# my_dict = {'b': 2, 'a': 1, 'c': 3}
# for key in sorted(my_dict.keys()):
#     print(key, my_dict[key], end=", ")

# # Iterating with enumerate for Index and Value:
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# for idx, (key, value) in enumerate(my_dict.items()):
#     print(f"Index: {idx}, Key: {key}, Value: {value}")

# # Using List Compression for filtering
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered_dict = {key: value for key, value in my_dict.items() if value % 2 == 0}
# print(f"filtered_dict: {filtered_dict}")

# # '''''''''''''''''''''''''Dictionary Comprehension with For Loops'''''''''''''''''
# # Creating a dictionary from List of tuples
# data = [('a',1), ('b',2), ('c',3), ('d',4)]
# my_dict = {key: value for key, value in data}
# print(f'my_dict: {my_dict}')

# # Squaring values in a Dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# square_dict = {key: value*2 for key, value in my_dict.items()}
# print(f'square_dict: {square_dict}')

# # Filtering Dict Values
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# filterd_dict = {key: value for key, value in my_dict.items() if value % 2 == 0}
# print(f'filterd_dict: {filterd_dict}')

# # Creating a Dictionary with Custom Key-Value Pairs:
# keys = ['a','b','c']
# values = [1, 2, 3]
# my_dict = {key: value for key, value in zip(keys, values)}
# print(f'my_dict: {my_dict}')

# # Nested dictionary
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# nested_dict = {key: {value: value**2} for key, value in zip(keys, values)}
# print(f'nested_dict: {nested_dict}')

# teams = ['Team A', 'Team B']
# players = ['Alice', 'Bob', 'Charlie', 'David']

# team_roster = {team: {player: 0 for player in players} for team in teams}
# print(f"team_roster: {team_roster}")

# # Using Conditional Statements
# numbers = [1, 2, 3, 4, 5]
# squared_dict = {num: num**2 if num % 2 == 0 else num for num in numbers}
# print(f'squared_dict: {squared_dict}')

# # Enumarating with Custom Start Values
# colors = ["red", "green", "blue"]
# for index, color in enumerate(colors, start=1):
#     print(f"Color {index}: {color}")

# # ''''''''''''''''''''''''For Loop with else block'''''''''''''''''''''''''''''''
# # Basic Example
# numbers = [1, 2, 3, 4, 5]
# target = 60
# for num in numbers:
#     if num == target:
#         print(f"Target {target} found.")
#         break
# else:
#     print(f"Target {target} not found.")
# # ''''''''''''
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)
# else:
#     print("Loop completed without interruption")

# # ''''''''''Prime Number Checking
# num = 11
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num} is a prime number")
#         break
# else:
#     print(f"{num} is not a prime number")

# # ''''''''''''''. Finding the First Non-Negative Number:''''''''''''
# numbers = [-1, -3, 2, 4, 7]
# for num in numbers:
#     if num>=0:
#         print(f"The first non-negative number is {num}")
#         break
# else:
#     print(f"all numbers are non-negative") 

# # '''''''''''''''''''''''''''''''Iterating Custom Objects''''''''''''''''''
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# class Student_List:
#     def __init__(self):
#         self.students = []
#         self.index = 0
#     def add_Student(self, my_student):
#         self.students.append(my_student)
    
#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < len(self.students):
#             student = self.students[self.index]
#             self.index += 1
#             return student
#         raise StopIteration
    
# # Create a SuperList and add students 
# student_list = Student_List()
# student_list.add_Student(Student("Alice", 21))
# student_list.add_Student(Student("Bob", 22))
# student_list.add_Student(Student("John", 23))
# student_list.add_Student(Student("Charlie", 24))
    
# # Iterating through Custom Objects
# for student in student_list:
#     print(f"student.name: {student.name} and Age: {student.age}")

# # '''''''''''''''''. Implementing Iterable Objects with Custom Classes:'''''''''''
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         self.current = self.start
#         return self
    
#     def __next__(self):
#         if self.current < self.end:
#             result = self.current
#             self.current += 1
#             return result
#         raise StopIteration

# # Create an iterable range
# my_range = MyRange(10, 21)

# for i in my_range:
#     print(i,end=' ')
# print()

# # '''''''''''''''Custom Object Iteration Using Generator:''''''''''''''''''''
# class CustomObject:
#     def __init__(self, data):
#         self.data = data

# def custom_object_generator(custom_objects):
#     for obj in custom_objects:
#         yield obj.data

# objects = [CustomObject(1), CustomObject(2), CustomObject(3)]

# for data in custom_object_generator(objects):
#     print(data)

# # '''''''''''''''''
# # Define a custom class with operator overloading for comparison
# class CustomObject:
#     def __init__(self, value):
#         self.value = value

#     def __lt__(self, other):
#         # Customize the less-than operator for comparisons
#         return self.value < other.value

#     def __str__(self):
#         return str(self.value)

# # Define a custom iterable class with an iterator
# class CustomObjectCollection:
#     def __init__(self):
#         self.objects = []

#     def add_object(self, obj):
#         self.objects.append(obj)

#     def __iter__(self):
#         # Initialize an index for iteration
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < len(self.objects):
#             obj = self.objects[self.index]
#             self.index += 1
#             return obj
#         raise StopIteration

# # Create instances of custom objects
# objects = [CustomObject(50), CustomObject(2), CustomObject(8), CustomObject(1)]

# # Create a collection of custom objects
# collection = CustomObjectCollection()
# for obj in objects:
#     collection.add_object(obj)

# # Sort the collection using the custom comparison logic
# collection.objects.sort()

# # Iterate through the sorted custom objects
# for obj in collection:
#     print(obj)

# '''''''''''''''''''''
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    # Implement __lt__ (less than) method for custom sorting
    def __It__(self, other):
        # Compare students based on scores
        return self.score < other.score

    # Implement __str__ method for custom printing
    def __str__(self):
        return f"Name: {self.name}, Score: {self.score}"
    
# Creating a list of custom Student objects
students = [
    Student("Alice", 400),
    Student("Charlei", 480),
    Student("John", 390),
    Student("Bob", 450)
]

# Sort the list of students based on their scores (ascending order)
# students.sort() #TypeError: '<' not supported between instances of 'Student' and 'Student'

# Iterating through the custom objects
for student in students:
    print(student)