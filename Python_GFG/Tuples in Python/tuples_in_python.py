# # ''''''''''''''''''''Creating Tuple''''''''''''''''''''''''''''
# my_tuple = (1, 2, 3, 4, 5) # Create a tuple with parentheses
# my_tuple = 1, 2, 3, 4, 5, 6 # Create a tuple without parentheses
# print(f'my_tuple: {my_tuple}')
# empty_tuple = () # Empty tuple
# mixed_tuple = (1, 'Hello', 3.14) # Creating a tuple with Mixed Data Types
# single_element_tuple = (42,) # Creating a tuple with Single element
# packed_tuple = 1, 'apple', 3.0 # Creating a Tuples with Tuple Packing
# print(f'packed_tuple: {packed_tuple}') # Output: (1, 'apple', 3.0)
# a, b, c = packed_tuple # Create a Tuples with Tuple Unpacking

# # Using Built-in tuple() method
# my_list = [1, 2, 3]
# tuple_from_list = tuple(my_list)

# my_string = "Python"
# tuple_from_string = tuple(my_string)

# # Using tuples concatenation
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# concatenated_tuple = tuple1 + tuple2

# # Using tuple comprehension
# my_tuple = tuple(x for x in range(5))

# # Creating a nested tuples
# my_tuple = ((1, 2), (3, 4), (5, 6))

# # Using * Operator
# my_tuple = (0, ) * 5 # Creates a tuple with five 0's


# # ''''''''''''''''''''''''''''''''''''''''
# # 1.Creating tuple with list comprehension
# even_sqaure_tuples = tuple(x  ** 2 for x in range(1,11) if x % 2 == 0)

# # '''''''2.Tuple unpacking in loops
# # Iterate through the list of tuples containing coordinates
# points = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for x, y in points:
#     print(f'X = {x}, Y = {y}')
    
# # 3.Using zip() to Combine Tuples
# '''zip() to combine multiple tuples element-wise.'''
# tuple1 = (1, 2, 3, 4, 5, 6)
# tuple2 = ('a', 'b', 'c', 'd')
# my_tuple = tuple(zip(tuple1, tuple2))
# print(f'my_tuple: {my_tuple}')

# # '''''''''''4.Sorting Tuples Based on a Specific Element
# #  Sorting a list of tuples by the second element (ascending)
# points = [(3, 4), (1, 2), (5, 6)]
# sorted_points = sorted(points, key = lambda x: x[1])
# print(f'sorted_points: {sorted_points}')

# # ''''5.Named Tuples
# '''Using namedtuple from the collections module to create tuples with named fields.'''
# from collections import namedtuple

# # Define a named tuple
# Person = namedtuple('Person', ['name', 'age'])

# # Create a instance of a named tuple Person
# Charlie = Person(name = 'Charlie', age = 22)
# David = Person(name = 'David', age = 25)
# print(f'Charlie: {Charlie}')
# print(f'Charlie Info, Name: {Charlie} Age: {Charlie.age}')

# # ''''''''''''
# from collections import namedtuple

# # Define a named tuple type
# Point = namedtuple('Point', ['x', 'y'])

# # Create instances of the named tuple
# p1 = Point(1, 2)
# p2 = Point(3, 4)


# # '''''''''Type Concatenation
# t1 = (1, 2, 3, 4)
# t2 = ('a', 'b', 'c', 'd', 'e', 'f')
# my_tuple = t1 + t2
# print(f'my_tuple: { my_tuple}')

# # '''''''Using Tuples as Key in Dictionary
# student_grade = {('Alice', 'Math'): 95, ('Bob', 'Science'): 97}
# print(f"Student grade: { student_grade}")
# print(f"Student grade: { student_grade[('Alice', 'Math')]}")

# # '''''''Using enumerate() with tuples
# '''enumerate() can be combined with tuples to get both index and value during iteration.'''
# # Enumerate elements of a list with their indices as tuples
# my_list = ['a', 'b', 'c', 'd']
# my_tuple = tuple(enumerate(my_list))
# print(f'my_tuple: {my_tuple}')

# # ''''''''''''Using the * Operator for Extended Unpacking:
# # Extended Unpacking with * operator
# my_tuple = (1, 2, 3, 4, 5) * 3
# first, *rest = my_tuple
# print(f'first: {first}')
# print(f'rest: {rest}')

# # '''''''''Tuple length
# length = len(my_tuple)

# # # ''''''''Tuple Comparison
# '''Tuples can be compared element-wise.'''
# # tuple_from_list = tuple([1, 2, 3])
# # tuple_from_generator = tuple((x for x in range(1, 4)))
# # result = tuple_from_list = tuple_from_generator
# # print(f'result: {result}')

# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = t1 < t2
# print(f'result: {result}') # True because (1 < 4)

# # ''''''Tuple as a Function Return Values
# def get_coordinates():
#     return 3, 4
# x, y = get_coordinates()
# print(f'x = {x} y = {y}')
# print()

# # '''''''''Tuple Packing and Unpacking in Loop
# ''' use tuple packing and unpacking in loops for multiple return values.'''
# for x, y in [(1, 2), (3, 4), (5, 6)]:
#     print(f'x = {x} y = {y}')

# # Tuples are hashable
# ''' use them as keys in dictionaries.'''
# # my_dict = {[1, 2]: 'value'} # unhashable type: 'list
# my_dict = {(1, 2): 'value'} # hashable type: tuple
# print(f'my_dict: {my_dict}')

# # # Tuples Immutablity
# # my_tuple = (1, 2, 3)
# # my_tuple[0] = 4  # This will raise a TypeError

# # Reassigning Tuple
# ''' can't modify a tuple, you can reassign it to a new value.'''
# my_tuple = (1, 2, 3)
# my_tuple = (4, 5, 6)  # Reassignment is allowed
# print(my_tuple)  # Output: (4, 5, 6)

# # Using Tuple as Dictionary Key
# my_dict = {(1, 2): 'value'}
# print(my_dict[(1, 2)])  # Output: 'value'

# # Iterating over Tuple
# my_tuple = (1, 2, 3)
# for element in my_tuple:
#     print(element)

# # Checking for Existence
# my_tuple = (1, 2, 3)
# if 2 in my_tuple:
#     print("2 exists in the tuple")

# # Tuple with Mutable Objects
# '''A tuple can contain mutable objects like lists, but the tuple itself remains immutable.'''
# my_tuple = (1, [2, 3], 4, 5)
# my_tuple[1].append(['a', 'b', 'c']) # Modified the list inside the tuple is allowed
# print(f'my_tuple: {my_tuple}')

# # Tuple as Function Return Values
# '''Using tuples to return multiple values from a function:'''
# def divide_and_remainder(a, b):
#     quotient = a // b
#     remainder = a % b
#     return quotient, remainder

# q, r = divide_and_remainder(10, 3)  # q will be 3, r will be 1

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''Tuples Methods'''''''''''''''''''
# # 1.count(value)
# my_tuple = (1, 2, 3, 2, 2, 3, 1, 4, 5, 4)
# '''This method returns the number of times a specified value appears in the tuple.'''
# count = my_tuple.count(2)
# print(f'count: {count}')

# # 2.index(value, start, end)
# '''Returns the index of the first occurrence of the specified value in the tuple. 
# You can also specify optional start and end indices to search within a specific range.'''
# my_tuple = (1, 2, 3, 2, 2, 3, 1, 2, 4, 5, 4)
# index = my_tuple.index(2)  # Returns 1
# print(f'index: {index}')
# index_2 = my_tuple.index(2, 5, len(my_tuple))
# print(f'index_2 = {index_2}')

# # Tuple length
# my_tuple = (1, 2, 3, 4, 5)
# length = len(my_tuple)  # Returns 5

# # ''''''''''''''''''''''Iterating Tuple through Loops''''''''''''''''''''''''''
# # ''''''''''''1.Using a while loop with index
# my_tuple = (1, 2, 3, 4, 5)
# index = 0
# while index < len(my_tuple):
#     print(my_tuple[index])
#     index += 1

# # '''''''''''''''''2.Using zip for iterating multiple tuples:
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# for item1, item2 in zip(tuple1, tuple2):
#     print(item1, item2)

# # ''''''''''''''''''Tuple packing and unpacking
# # '''''''''''1.Ignoring Value
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# first, _, third, *_ = my_tuple
# print(f'first: {first}, _ : {_}, third: {third}, *_ : {_}')

# # ''''''''''2.Unpacking with zip
# '''use the zip function to unpack values from tuples.'''
# packed_tuple = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# l1, l2 = zip(*packed_tuple)
# print(f'l1 = {l1}, l2 = {l2}')

# # ''''''''''3.Packing value during input
# a, b, c = map(int, input().split()) # Input: 10, 20, 30
# my_tuple = a, b, c # Tuple Packing

# # ''''''4.Unpack and pass multiple values to a function
# def unpacking_example(a, b, c, d, e):
#     print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# values = (10, 20, 30, 40, 50)
# unpacking_example(*values)  

# # Advanced Unpacking
# nested_tuple = (1, [2, 3], (4, 5), 6, 'a', 'b', 'c')
# first, [second, third], (forth, fivth), sixth, *rest = nested_tuple
# print(f'first: {first}')
# print(f'second: {second}')
# print(f'third: {third}')
# print(f'forth: {forth}')
# print(f'fivth: {fivth}')
# print(f'sixth: {sixth}')
# print(f'rest: {rest}')


