# my_list = [1, 2, 3, 4, 5] # Creating a list
# empty_list = [] # Empty list

# first_element = my_list[0]  # Accesses the first element (1)
# third_element = my_list[2]  # Accesses the third element (3)

# last_element = my_list[-1]  # Accesses the last element (5)

# sub_list = my_list[1:4]  # Creates a new list [2, 3, 4]

# # Modify the list
# my_list[1] = 10  # Changes the second element to 10
# my_list.append(6)  # Appends 6 to the end of the list
# my_list.insert(2, 7)  # Inserts 7 at index 2, shifting other elements to the right
# my_list.remove(3)  # Removes the first occurrence of 3
# del my_list[1]  # Deletes the element at index 1
# my_list.clear()  # Removes all elements from the list, making it empty

# # List Operations
# list1 = [1, 2]
# list2 = [3, 4]
# concatenated_list = list1 + list2  # Creates [1, 2, 3, 4]

# original_list = [1, 2, 3]
# replicated_list = original_list * 3  # Creates [1, 2, 3, 1, 2, 3, 1, 2, 3]
# my_list = [1, 2, 5, 4, 10, 6, 11]
# my_list.sort()  # Sorts the list in ascending order
# my_list.reverse()  # Reverses the list in-place
# length = len(my_list)  # Returns the length of the list
# if 3 in my_list:
#     print("3 is in the list")

# # List Compression
# squared_numbers = [x**2 for x in my_list]
# even_numbers = [x for x in my_list if x % 2 == 0]

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Initialize an empty invent0ry list
# inventory = []

# # Function to add an item to the inventory empty list
# def add_item(name, price, quantity):
#     item = {
#         'name' : name,
#         'price' : price,
#         'quantity' : quantity
#     }
#     inventory.append(item)
#     print(f'Added {name}, {price}, {quantity} to the inventory')
#     print(f'inventory: {inventory}')

# # Function to update the quantity of an item
# def update_quantity(name, new_quantity):
#     for item in inventory:
#         if item['name'] == name:
#             item['quantity'] = new_quantity
#             print(f'Update the quantity of {name} to {new_quantity}')
#             return
#     print(f'{name} product not found in the inventory')

# # Function to remove an item from the inventory
# def remove_item(name):
#     for item in inventory:
#         if item['name'] == name:
#             inventory.remove(item)
#             print(f'Removed {name} from inventory')
#             return
#     print(f'{name} not found in the inventory')

# # Function to display the current inventory
# def display_info():
#     for item in inventory:
#         print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

# add_item("Widget", 5.99, 100)
# add_item("Gadget", 12.49, 50)
# display_info()
# update_quantity("Widget",500)
# update_quantity("Gadget",200)
# remove_item("Gadget")
# display_info()

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Initialize an empty list
# my_list = []

# # Populate the list with somedata
# for i in range(1,11):
#     my_list.append(i)

# # Print the Original List
# print(f'Original List: {my_list}')

# # Calculate the Sum of all elements in the original list
# print(f'Sum of all elements in original list = {sum(my_list)}')

# # Find the maximum and minimum element in the original list
# max_element = max(my_list)
# min_elemennt = min(my_list)
# print(f'Max element: {max_element}, min element: {min_elemennt}')

# # Sort the list in ascending order
# my_list.sort()

# # Reverse the list
# my_list.reverse()


# # Remove duplicates from the list
# my_list_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
# unique_list = list(set(my_list_with_duplicates))
# print("List with Duplicates:", my_list_with_duplicates)
# print("Unique List:", unique_list)

# # Check if a specific value is in the list
# value_to_check = 7
# if value_to_check in my_list:
#     print(f"{value_to_check} is in the list.")
# else:
#     print(f"{value_to_check} is not in the list.")

# # Iterate through the list and print each element
# print("List Elements:")
# for element in my_list:
#     print(element)

# # Clear the list
# my_list.clear()
# print("Cleared List:", my_list)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''
# # 1.Initialize the list with default values
# n = 5 # Size of the list
# default_value = 0
# my_list = [default_value] * n # Create a list of size 5 with all elements as default values 0

# # 2.Creating a list from Input
# my_list = list(map(int, input().split()))

# # 3.Sorting the list in Reverse order (Desending Order)
# my_list.sort(reverse=True) # Sort the list in descending order

# # 4.Using heap for Priority Queue
# '''use the heapq module to create a priority queue using a list'''
# import heapq
# my_heap = []
# heapq.heappush(my_heap, 5) # Add an element to the heap

# # 5.Using the collections.Counter for Counting the elements
# '''The collections module provides a Counter class for counting elements in a list'''
# from collections import Counter
# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# element_count = Counter(my_list) # Count the occurrences of each element

# # 6.Using enumarator for Index and Element in Loop
# my_list = [10, 20, 30]
# for index, element in enumerate(my_list):
#     print(f"Element at index {index} is {element}")

# # List Compression with conditions
# my_list = [1, 2, 3, 4, 5]
# even_squares = [x**2 for x in my_list if x % 2 == 0]  # Square of even numbers

# # Sorting with Custom Key
# original_list = ['apple', 'banana', 'cherry', 'date']
# sorted_list = sorted(original_list, key = lambda x: len(x)) # Sort by the length

# # List concatenate with extend()
# '''extend() is a method for adding multiple elements from another list to an existing list.'''
# l1 = ['a', 'b', 'c', 'd']
# l2 = [1, 2, 3, 4, 5, 6, 7, 8]

# l1.extend(l2) #Append the elements  from l2 to l1

# # Using zip() for Pairing List
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# paired_list = list(zip(list1, list2))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# # # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # 1.Initializing the list
# # Initialize a list of integers from 1 to 10
# numbers = [i for i in range(1, 11)]

# # Initialize a list of even numbers from 2 to 20
# even_numbers = [i * 2 for i in range(1, 11)]

# # Create a list with 100 elements, all initialized to 0
# zeros = [0] * 100

# # 2.Mapping the list
# # Double each element in the list
# double_list = list(map(lambda x: x * 2, numbers))

# # 3.Using Deque for Efficient Operations
# '''Deque (double-ended queue) is a data structure that allows efficient append and pop operations from both ends.'''
# from collections import deque

# #Initialize a deque
# my_deque = deque([10,20,30,40,50])

# # Append and pop elements efficiently from both ends
# my_deque.append(60)
# my_deque.appendleft(100)
# print(f'my_deque: {my_deque}')
# popped_element = my_deque.pop()
# print(f'my_deque: {my_deque}, popped_element: {popped_element}')
# popped_element_left = my_deque.popleft()
# print(f'my_deque: {my_deque}, popped_element: {popped_element_left}')

# # List Operations for 2D Lists
# #Initialize a 2D list(matrix)
# matrix = [[1,2,3], [4,5,6], [7,8,9]]

# # Accessing an element in a 2D list
# element = matrix[1][2]  # Accesses the element at row 1, column 2

# # Transpose a 2D List
# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

# # Removing Duplicates While Preserving Order (Python 3.7+)
# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# unique_nums = list(dict.fromkeys(nums))
# print(f'unique_nums: {unique_nums}')

# # Rotate the List
# k = 3 # Rotate by 3 positions
# rotated_num = nums[-k:] + nums[:-k]

# # Counting Elements in a Range
# count_in_range = sum(1 for x in nums if 3 <= x <= 6)

# # Copying the list
# copy_of_num = nums.copy()
# print(f'copy_of_num: {copy_of_num}')

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''List Methods'''''''''''''''''''''''''''''''''
# # ''''''''''''''1.append()'''''''''''''''''''''''''
# # Appending an element to the list
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_list.append(110)

# # Appending Multiples elements to the list
# '''append multiple elements at once by passing a list or another iterable to append().'''
# my_list = [1, 2, 3]
# my_list.append([4, 5, 6, 7, 8])
# print(f'my_list: {my_list}')

# # Appending a list
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(list2)
# print(f'list1: {list1}')  # Output: [1, 2, 3, [4, 5, 6]]


# # Appending elements in Loop
# '''use a loop to append elements to a list dynamically.'''
# my_list = []
# for i in range(1, 6):
#     my_list.append(i)
# print(f'my_list: {my_list}')

# # Appending Different Data Types
# '''append() can be used to add elements of different data types to a list.'''
# my_list = [1, 2, 3, 4]
# my_list.append('Hello, world')
# my_list.append(123.45)
# print(f'my_list: {my_list}')

# # Appending User Input
# '''use user input and append() to build a list of values.'''
# my_list = []
# while True:
#     user_input = input("Enter a number (or 'q' for quite)")
#     if user_input == 'q':
#         break
#     try:
#         num = int(user_input)
#         my_list.append(num)
#     except ValueError:
#         print(f'Invalid Input. Please Enter a number.')
# print(my_list)

# # Appending Elements in a List of List
# matrix = [[] for _ in range(3)]  # Creating a 3x3 matrix
# for i in range(3):
#     for j in range(3):
#         matrix[i].append(i * 3 + j)

# print(f'matrix: {matrix}')
# # Output: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# # ''''''Using collections.deque for Efficient Appends:
# from collections import deque

# # Creating a deque
# my_deque = []

# # Appending elements efficiently
# my_deque.append(10)
# my_deque.append(20)
# my_deque.append(30)

# print(f'my_deque: {my_deque}')

# # '''''''''Using heapq to Append Elements with Priority:
# import heapq

# # Creating a heap(min-heap)
# my_heapq = []
# heapq.heappush(my_heapq, 10)
# heapq.heappush(my_heapq, 20)
# heapq.heappush(my_heapq, 30)
# heapq.heappush(my_heapq, 40)

# print(f'my_heapq: {my_heapq}')

# # ''''''''''''''''Appending elements using stack
# # implementating a stack and appending elements
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(f'stack: {stack}')

# # ''''''''Appending elements using Queue
# from queue import Queue
# # Implementating a queue and appending elements
# my_queue = Queue()
# my_queue.put(10)
# my_queue.put(20)
# my_queue.put(30)
# my_queue.put(40)

# print(f'my_queue: {list(my_queue.queue)}')

# # Competitive Programming Example
# n = int(input()) # Read the number of elements in the list
# my_list = [] # Initialize an empty list


# for _ in range(n):
#     element = int(input()) # Read an element
#     my_list.append(element) # Append the element to the list

# # '''''''''''''''''''''''2.extend(iterable)
# # 1.Using extend with lists
# my_list = [1, 2, 3, 4]
# iterable = [5, 6, 7, 8, 9, 10]
# my_list.extend(iterable)
# print(f'my_list: {my_list}') # Output: my_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 2.Using extend with an empty list
# my_list = []
# iterable = [1, 2, 3, 4, 5]
# my_list.extend(iterable)
# print(f'my_list: {my_list}') # Output: [1, 2, 3, 4, 5]

# # Using extend with a tuple
# my_list = [1, 2, 3, 4, 5]
# my_tuple = (6, 7, 8)
# my_list.extend(my_tuple)
# print(f'my_list: {my_list}') # Output my_list: [1, 2, 3, 4, 5, 6, 7, 8]

# # 4.Using extend with string
# my_list = ['Hello']
# string_1 = 'World'
# my_list.extend(string_1)
# print(f'my_list: {my_list}')

# # 5.Using extend with set
# my_list = [1, 2, 3]
# set1 = {3, 4, 5}
# my_list.extend(set1)
# print(f'my_list: {my_list}')  # Output: [1, 2, 3, 3, 4, 5]

# # 6.Using extend with Generator
# my_list = [1, 2, 3, 4, 5]
# generator = (x for x in range(6, 11))
# my_list.extend(generator)
# print(f'my_list: {my_list}')

# # 7.Using extend with Range
# my_list = [1, 2, 3, 4, 5]
# range_value = range(6, 11)
# my_list.extend(range_value)
# print(f'my_list: {my_list}')


# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # '''''''''''''''''''''''''''''''''''''''''Creating List''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Using Sqaure Brackets
# my_list = [1, 2, 3, 4, 5]

# # Creating a List with
# # the use of Numbers
# # (Having duplicate values)
# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)

# # Creating a List with
# # mixed type of values
# # (Having numbers and strings)
# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print("\nList with the use of Mixed Values: ")
# print(List)

# # Define a list
# heterogenousElements = [3, True, 'Michael', 2.0]

# # Using the 'list()' Constructor
# '''use the list() constructor to create a list from an iterable object like a string, tuple, or another list.'''
# my_list = list('Hello, world')
# print(my_list) # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd']
# my_list = list()
# print(my_list) # Output: []
# my_list = list((1, 2, 3, 4, 5))
# print(my_list) # Output: [1, 2, 3, 4, 5]
# my_list = list({'name': 'Ranjit', 'age': 22})
# print(my_list) # Output: ['name', 'age'
# # print(my_list['name']) # Output: TypeError: list indices must be integers or slices, not str
# print(my_list[0]) # Output: name

# # Using List Comprehension
# my_list = [x ** 2 for x in range(5)]
# print(my_list) # Output: [0, 1, 4, 9, 16, 25]

# # Using 'range()' function
# my_list = list(range(5))

# # Using repetition operator -> Use the repetition operator '*' to create a list with repeated elements
# my_list = [2] * 5
# print(my_list) # Output: [2, 2, 2, 2, 2]

# # Using Nested Lists -> List contains other List
# nested_list = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
# print(nested_list) # Output:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Using 'append()' method -> Start with an empty list and dynamically add elements using the 'append()' method
# my_list = []
# my_list.append(10)
# my_list.append(20)
# print(my_list) # Output: [10, 20]

# # Using List Concatenation -> Concatenate two or more lists using '+'Operator
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# my_list = l1 + l2
# print(my_list)

# # Using List Slicing -> Create a list from a part of another list using slicing
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = l1[4 : 8]
# print(my_list) # Output: [5, 6, 7, 8]

# # Using 'split()' on string
# my_string = "Hello world Hii My Name is Ranjit"
# my_list = my_string.split()
# print(f'my_list : {my_list} and type(my_list): {type(my_list)}') # # Output: ['Hello', 'world', 'Hii', 'My', 'Name', 'is', 'Ranjit'], <class 'list'>

# # Using list Comprehension with condition
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = [x for x in l1 if x % 2 == 0]
# print(my_list) # Output: [2, 4, 6, 8, 10]

# # Using 'map()' function with lambda
# my_list = list(map(lambda x: x ** 2, range(1, 10)))
# print(my_list) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# # Using list comprehension with nested loops
# my_list = [(x, y) for x in range(1, 4) for y in range(1, 5)] # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)]
# print(my_list)

# # Using Unpacking
# '''Creating a list by unpacking elements from another iterable'''
# my_string = 'Hello, world'
# unpacked_list = [*my_string]
# print(f'unpacked_list: {unpacked_list} and type(unpacked_list): {type(unpacked_list)}')


# # Reading space-separated integers as a list
# my_list = list(map(int, input().split()))
# print(my_list, type(my_list))

# # Reading space-separated strings as a list
# str_list = input().split()
# print(str_list, type(str_list))

# # Creating a list with a specific size filled with default values
# size = 5
# my_list = [1] * size
# print(my_list)

# # Creating a list of lists (2D List)
# rows, cols = 3, 5
# mtrix = [[0] * cols for _ in range(rows)]
# print(mtrix)

# # sorting a list
# my_list = [1, 2, 5, 3, 7, 9, 4]
# sorted_list = sorted(my_list)
# print(sorted_list)

# # Reversing a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# reversed_list = reversed(my_list)
# print(reversed_list, type(reversed_list))
# reversed_list_2 = list(reversed(my_list))
# print(f'reversed_list_2: {reversed_list_2} and type(reversed_list_2): {type(reversed_list_2)}')

# # Applying a function to call all elements of the list
# def add_one(x):
#     return x + 1
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# modified_list = list(map(add_one, my_list))
# print(f'Modified list: {modified_list} and type(modified_list): {type(modified_list)}')

# # Maximum element in the list
# max_ele = max(my_list)
# print(max_ele)

# # Minimum element in the list
# min_ele = min(my_list)
# print(min_ele)

# # Sum of all elements of the list
# print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# sum_of_all = sum(my_list) # 36
# print(sum_of_all)

# # Index of element in the list
# element_to_check = 5
# index_of_ele = my_list.index(element_to_check)
# print(index_of_ele)

# # Counting occurences of element in the list
# count_to_check = my_list.count(5)
# print(count_to_check) # 1

# # Copying a list(shallow copy)
# copied_list = my_list[:]
# print(f'copied list: {copied_list}')

# # Shallow Copy
# import copy

# copied_list_2 = my_list.copy()
# copied_list_2 = copy.copy(my_list)
# print(f'copied_list_2: {copied_list_2}')

# # Deep Copy
# deep_copy = copy.deepcopy(my_list)
# print(f'deep_copy: {deep_copy}')

# # Aliasing
# alised_lsit = my_list
# print(f'alised_lsit: {alised_lsit}')

# # Check if all elements satisfy the condition
# all_positive = all(x > 0 for x in my_list)
# print(f'all elements satisfy: {all_positive} and type(all_positive):{type(all_positive)}') # Output: True, <class 'bool'>

# # Check if any element satisfies the condition
# any_negative = any(x < 0 for x in my_list)
# print(f'any element satisfies: {any_negative} and type(any_negative): {type(any_negative)}') # Output: False, <class 'bool'>

# # Applying a function to specific elements of a list
# def is_odd(x):
#     # if x % 2 != 0:
#     #     return x

#     return x % 2 != 0

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# filtered_list = list(filter(is_odd, my_list))
# print(f'filtered list: {filtered_list}')

# # Finding the first occurrence of a condition
# first_odd_index = next((i for i , x in enumerate(my_list) if is_odd(x)), None)
# print(f'first_odd_index: {first_odd_index} and type(first_odd_index): {type(first_odd_index)}')

# # Swapping two elements in a list
# my_list[0], my_list[1] = my_list[1], my_list[0]
# print(my_list)

# # # Creating a list from user input
# # n = int(input('Enter the number of elements: '))
# # my_list = [int(input()) for _ in range(n)]
# # print(my_list)

# # my_list = list(map(int, input('Enter elements separated by space: ').split()))
# # print(my_list)

# # Clear the list
# my_list.clear()

# #  remove duplicates from a list
# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
# removed_list = list(set(my_list))

# # To check if a list is stored in the non-decreasing order
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list == sorted(my_list))

# # Reverse a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reversed_list = my_list[::-1]
# print(f'reversed list: {reversed_list}')

# # List of Strings seperated by spaces
# my_list = 'Hello, world'
# l1 = list(' '.join(my_list))
# print(l1)
# print('-'.join(my_list))

# # Using Zip Function for combining two lists element-wise
# l1 = [1, 2, 3, 4, 5]
# l2 = ['a', 'b', 'c', 'd']
# zipped_list = list(zip(l1, l2))
# print(f'zipped_list: {zipped_list}') # Output: zipped_list: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# print(f'zip(l1, l2: {zip(l1, l2)}') # Output: <zip object at 0x000002514ED56B40>

# #  Using list comprehension for generating a list of lists
# my_list = [[0 for _ in range(3)] for _ in range(4)]
# print(my_list)


# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''Accessing Elements in List'''''''''''''''''''''''''''''''''''''
# # Creating a Sample List
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # Accessing Elements by Index
# first_ele = my_list[0]
# second_ele = my_list[1]
# last_ele = my_list[-1]
# second_last_ele = my_list[-2]
# print(f'first_ele: {first_ele}, second_ele: {second_ele}, last_ele: {last_ele}, second_last_ele: {second_last_ele}')

# # Slicing to get a sub_list
# sub_list = my_list[2 : 6]
# print(f'sub_list: {sub_list}') # [30, 40, 50] -> Elements from index 2 to 5(exclusive 6)
# first_three_ele = my_list[:3]
# print(f'first_three_ele: {first_three_ele}') # [10, 20, 30] -> Elements from index 0 to 2
# last_three_ele = my_list[-3:]
# print(f'last_three_ele: {last_three_ele}') # [80, 90, 100] -> Elements from index -3 to end of list

# # Iterating over elements
# for element in my_list:
#     print(element, end=' ')
# print()

# # Accesssing Elements using enumerated() for both index and values
# for key, value in enumerate(my_list):
#     print(f'key: {key}, value: {value}', end=' ')
# print()

# # Accessing the elements in the reverse order
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# last_ele = my_list[-1]
# reverse_list = my_list[::-1] # Reveres the entire list
# reversed_sublist = my_list[-3::-1] # Reverse sublist starting from index -3
# print(f'reversed sublist: {reversed_sublist}') # Output: [8, 7, 6, 5, 4, 3, 2, 1]

# # Accessing elements in nested list
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# element = nested_list[1][2] # Accessing element at row 1 and column 2 -> 6
# print(element)

# # Accessing every nth element
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# every_second_ele_list = my_list[::2]
# every_third_ele_list = my_list[::3]
# print(f'every_second_ele_list: {every_second_ele_list}') # Output: [1, 3, 5, 7, 9]
# print(f'every_third_ele_list: {every_third_ele_list}') # Output: [1, 4, 7, 10]

# # Using loops to Access elements
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for element in my_list:
#     print(element, end=' ')

# # ''''''''''''''''''''''''''''''''''''''''''''''''Slicing List''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Original list
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slicing from index 2 to 5 (exclusive)
# sliced_list = original_list[2:5]

# print(sliced_list)  # Output: [3, 4, 5]

# # Omitting start index (from beginning to index 3)
# sliced_list_start = original_list[:3]

# # Omitting end index (from index 4 to the end)
# sliced_list_end = original_list[4:]

# print(sliced_list_start)  # Output: [1, 2, 3]
# print(sliced_list_end)    # Output: [5, 6, 7, 8, 9]

# # Slicing from the second last element to the end
# sliced_list_negative = original_list[-2:]

# print(sliced_list_negative)  # Output: [8, 9]

# # Slicing with a step of 2
# sliced_list_step = original_list[1::2]

# print(sliced_list_step)  # Output: [2, 4, 6, 8]

# # Reversing the list
# reversed_list = original_list[::-1]

# print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# # Copying the list
# copied_list = original_list[:]

# print(copied_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''Modifying List''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Appending Elements
# my_list = [1, 2, 3]
# my_list.append(4) # Append the single element
# print(f'my_list: {my_list}')
# my_list.extend([5, 6, 7, 8]) # Append the multiple elements
# print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# # Inserting Element at specific index
# my_list = [1, 2, 3, 4]
# my_list.insert(2, 'x')
# print(my_list) # [1, 2, 'x', 3, 4]

# # Removing Element by value
# '''Remove the first occurrence of an element'''
# my_list = [1, 2, 'x', 3, 4]
# my_list.remove('x')
# print(my_list) # [1, 2, 3, 4]

# # Remove elements by indexing
# my_list = ['a', 'b', 'c', 'd', 'e']
# removed_element = my_list.pop(2) # Remove elements at index 2
# print(f'removed element: {removed_element}') # Output: c
# print(my_list) # Output: ['a', 'b', 'd', 'e']

# # Remove last element
# my_list = ['a', 'b', 'c', 'd', 'e']
# removed_last_element = my_list.pop()
# print(f'removed last element: {removed_last_element}')
# print(my_list) # Output: ['a', 'b', 'c', 'd']

# # Updating Elements
# my_list = ['a', 'b', 'c', 'd', 'e']
# my_list[0] = 'A'
# print(my_list)

# # Cearing a list
# # Clear the entire list
# my_list.clear()
# print(my_list)  # Output: []

# # Sorting a list
# my_list = ['b', 'c', 'agh', 'de', 'e']
# my_list.sort()
# print(my_list)


# #  Sort the list in decending order
# my_list = ['b', 'c', 'agh', 'de', 'e']
# my_list.sort(reverse=True) # Output: ['agh', 'b', 'c', 'de', 'e']
# print(my_list) # Output: ['e', 'de', 'c', 'b', 'agh']

# # Slicing and Assignment
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list[2:6] = [30, 40, 50] # Modify elements in slice
# print(my_list)

# # Delete elements in slice
# my_list[2:6] = [] # Output: [1, 2, 30, 40, 50, 7, 8, 9, 10]
# print(my_list) # Output: 1, 2, 8, 9, 10]

# # Insert an element at a specific position
# my_list.insert(2, 10)
# print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# # Deleting Slice
# # Delete a slice from the list
# del my_list[1:3]
# print(my_list)  # Output: [1, 4, 6, 7, 8, 9]

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''List Methods and Functions'''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''''with 'key' parameters
# # Sorting based on built-in functions
# my_list = [-3, 1, -4, 1, 5, 9, 2, 6, -5, 3, -5]
# my_list.sort(key=abs)  # Sorting based on the absolute value of elements
# print(my_list)  # Output: [1, 1, 2, -3, 3, -4, 5, -5, -5, 6, 9]
# my_list.sort(key=abs, reverse=True)
# print(my_list)  # Output: [9, 6, 5, -5, -5, -4, -3, 3, 2, 1, 1]


# # ''''''''''''''''''
# def custom_len_fun(str):
#     return len(str)


# my_list = ["apple", "banana", "cherry", "date"]

# my_list.sort(
#     key=custom_len_fun
# )  # Sorting based on custom_len_fun which returns length of string
# my_list.sort(key=len)  # Sorting based on the length of strings
# print(my_list)  # Output: ['date', 'apple', 'banana', 'cherry']


# # Sorting based on custom function
# def custom_key_function(value):
#     print(f"Hello {value}")
#     return value % 5  # Sort based on remainder when divided by 5


# my_list = [10, 25, 3, 17, 9]
# my_list.sort(key=custom_key_function)
# print(my_list)


# # Sorting based on Specific Attributes of Objects
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# peoples = [Person("Alice", 25), Person("Bob", 20), Person("Charlie", 30)]
# print(
#     peoples
# )  # [<__main__.Person object at 0x0000018E44B2AB40>, <__main__.Person object at 0x0000018E44B2ABD0>, <__main__.Person object at 0x0000018E44B2AC00>]
# for people in peoples:
#     print(f"{people.name}  and {people.age}")
# """Output:
# Alice  and 25
# Bob  and 20
# Charlie  and 30"""
# print()
# # ''''''''''''''''''
# peoples = [Person("Alice", 25), Person("Bob", 20), Person("Charlie", 30)]


# def custom_object_sorting_function(value):
#     return value.age


# peoples.sort(key=custom_object_sorting_function)

# for people in peoples:
#     print(f"{people.name}  and {people.age}")
# print()
# # ''''''''''''''''''
# peoples = [Person("Alice", 25), Person("Bob", 20), Person("Charlie", 30)]
# peoples.sort(key=lambda x: x.age)

# for people in peoples:
#     print(f"{people.name}  and {people.age}")


# # Sorting based on multiple keys:
# def custom_sort_func(tup):
#     return tup[1], tup[0]  # Sort first by age, then by name


# my_list = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Boby", 25)]
# my_list.sort(key=custom_sort_func)
# print(my_list)
# # '''''''''''''''''
# my_list = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Boby", 25)]
# my_list.sort(key=lambda x: (x[1], x[0]))  # Sort first by age, then by name
# print(my_list)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Define a list of tuples with different data types
# data = [
#     ('Alice', 25),
#     ('Bob', 20),
#     ('Charlie', 30),
#     ('David', 22),
#     ('Eve', 28)
# ]

# # Sort by name
# sorted_by_name = sorted(data, key=lambda x: x[0])
# print("Sorted by name:")
# print(sorted_by_name)

# # Sort by age
# sorted_by_age = sorted(data, key=lambda x: x[1])
# print("\nSorted by age:")
# print(sorted_by_age)

# # Sort by name length
# sorted_by_name_length = sorted(data, key=lambda x: len(x[0]))
# print("\nSorted by name length:")
# print(sorted_by_name_length)

# # Sort by reverse age
# sorted_by_reverse_age = sorted(data, key=lambda x: x[1], reverse=True)
# print("\nSorted by reverse age:")
# print(sorted_by_reverse_age)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the name key in asscending order
# print("Sorted by name (ascending):")
# my_list.sort(key=lambda x: x["name"])
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # ''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the name key in descending order
# print("Sorted by name (descending):")
# my_list.sort(key=lambda x: x["name"], reverse=True)
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # ''''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the age key in ascending order
# print("Sorted by age (ascending):")
# my_list.sort(key=lambda x: x["age"])
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # '''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the age key in descending order
# print("Sorted by age (descending):")
# my_list.sort(key=lambda x: x["age"], reverse=True)
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # ''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by length of 'name' key in ascending order
# my_list.sort(key=lambda x: len(x['name']))
# print("\nSorted by length of name (ascending):")
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # ''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the 'name' key and then by 'age' key
# my_list.sort(key=lambda x: (x['name'], x['age']))
# print("\nSorted by the 'name' key and then 'age' key(ascending):")
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # ''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the 'name' key ignoring key
# my_list.sort(key=lambda x: x['name'].lower())
# print("\nSorted by name (case-insensitive):")
# print(my_list)
# for item in my_list:
#     print(item)
# print()

# # # ''''''''''''
# # # Define sample data
# # my_list = [
# #     {"name": "John", "age": 30},
# #     {"name": "Alice", "age": 25},
# #     {"name": "Bob", "age": 35},
# #     {"name": "Charlie", "age": 20},
# # ]

# # # Sort by age in descending order, then by name in ascending order
# # my_list.sort(key=lambda x: (-x['name'], x['age'])) # TypeError: bad operand type for unary -: 'str'
# # print("\nSort by age in descending order, then by name in ascending order")
# # print(my_list)
# # for item in my_list:
# #     print(item)
# # print()

# # ''''''''''''
# # Define sample data
# my_list = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 20},
# ]

# # Sort by the last character of name
# my_list.sort(key=lambda x: x['name'][-1]) # TypeError: bad operand type for unary -: 'str'
# print("\n Sort by the last character of name")
# print(my_list)
# for item in my_list:
#     print(item)
# print()


# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Define a list with different types of elements
# my_list = [10, 'apple', (3, 4), {'name': 'John'}, [5, 6], 'banana', 7, {'age': 30}, 'cherry', 2]

# # Sort by absolute value (for numerical elements)
# def abs_key(value):
#     if isinstance(value, int):
#         return abs(value)
#     else:
#         return value

# my_list.sort(key=abs_key) # TypeError: '<' not supported between instances of 'str' and 'int'
# print("Sorted by absolute value:", my_list)

# # Sort by length (for strings and collections)
# my_list.sort(key=lambda x: len(str(x)) if isinstance(x, (str, list, tuple, dict)) else 0)
# print("Sorted by length:", my_list)

# # Sort by numeric value (for strings that can be converted to numbers)
# my_list.sort(key=lambda x: float(x) if isinstance(x, str) and x.isdigit() else x)
# print("Sorted by numeric value:", my_list)

# # Sort by dictionary value (for dictionary elements)
# def dict_key(value):
#     if isinstance(value, dict):
#         return value.get('name', '') if 'name' in value else value.get('age', 0)
#     else:
#         return value

# my_list.sort(key=dict_key)
# print("Sorted by dictionary value:", my_list)

# # Sort by last element (for lists)
# def last_element_key(value):
#     if isinstance(value, list) and len(value) > 0:
#         return value[-1]
#     else:
#         return value

# my_list.sort(key=last_element_key)
# print("Sorted by last element:", my_list)

# # Sort by type (for all elements)
# def type_key(value):
#     return type(value)

# my_list.sort(key=type_key)
# print("Sorted by type:", my_list)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Define some example data
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 30},
#     {'name': 'David', 'age': 25},
#     {'name': 'Eve', 'age': 22},
# ]

# # Define a variety of key functions
# key_functions = [
#     lambda x: x['name'],                           # Sort by name
#     lambda x: x['age'],                            # Sort by age
#     lambda x: len(x['name']),                      # Sort by name length
#     lambda x: (x['age'], x['name']),               # Sort by age, then by name
#     lambda x: (-x['age'], x['name']),              # Sort by age (descending), then by name (ascending)
#     lambda x: x['name'][-1],                       # Sort by the last character of name
#     lambda x: x['name'][0].lower(),                # Sort by the first character of name (case insensitive)
#     lambda x: x['name'][::-1],                     # Sort by name in reverse order
#     lambda x: x['name'][::-1].lower(),            # Sort by name in reverse order (case insensitive)
#     lambda x: x['name'][::-1][-1],                # Sort by the last character of name in reverse order
# ]

# # Perform sorting using each key function
# for key_function in key_functions:
#     sorted_data = sorted(data, key=key_function)
#     print(f"\nSorting by {key_function.__name__}:")
#     for item in sorted_data:
#         print(item)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''
# # Define some example data
# my_list = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 30},
#     {'name': 'David', 'age': 25},
#     {'name': 'Eve', 'age': 22},
# ]

# def print_sorted_list(key_function, reverse = False):
#     my_list.sort(key=key_function, reverse=reverse)
#     print(f'Sort by {key_function.__name__}')
#     for item in my_list:
#         print(item)
#     print()

# # Sort by name in ascending order
# print_sorted_list(lambda x: x['name'])

# # Sort by name in descending order
# print_sorted_list(lambda x: x['name'], reverse=True)

# # Sort by age in ascending order
# print_sorted_list(lambda x: x['age'])

# # Sort by age in descending order
# print_sorted_list(lambda x: x['age'], reverse=True)

# # Sort by name length in ascending order
# print_sorted_list(lambda x: len(x['name']))

# # Sort by name length in descending order
# print_sorted_list(lambda x: len(x['name']), reverse=True)

# # Sort by the last character of name in ascending order
# print_sorted_list(lambda x: x['name'][-1])

# # Sort by the last character of name in descending order
# print_sorted_list(lambda x: x['name'][-1], reverse=True)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Sample data
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 30},
#     {'name': 'David', 'age': 25},
#     {'name': 'Eve', 'age': 22},
# ]

# # Sorting by different keys
# sorting_methods = [
#     ('Name (ascending)', lambda x: x['name'], False),
#     ('Name (descending)', lambda x: x['name'], True),
#     ('Age (ascending)', lambda x: x['age'], False),
#     ('Age (descending)', lambda x: x['age'], True),
#     ('Name Length (ascending)', lambda x: len(x['name']), False),
#     ('Name Length (descending)', lambda x: len(x['name']), True),
#     ('Last Character of Name', lambda x: x['name'][-1], False),
# ]

# # Sorting and printing results
# for method_name, key_func, reverse in sorting_methods:
#     print(f"Sorting by {method_name}:")
#     sorted_data = sorted(data, key=key_func, reverse=reverse)
#     for item in sorted_data:
#         print(item)
#     print()

# # '''''''''''''''''''''''''''''''''''''''''''''''append() method'''''''''''''''''''''''''''''''''''''''''''''''''''''
# # The append() method in Python is used to add an element to the end of a list. It modifies the original list in-place and does not return any value (returns None).
# '''Syntax:
# list.append(element)
# '''
# '''
# Parameters:
# element: The element to be added to the end of the list.
# Return Value:
# The append() method doesn't return anything. It modifies the original list by adding the specified element to the end.
# '''
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Appending a Single Element to a List:
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)
# print(my_list)

# # append with different data types
# my_list = [1, 2, 'Apple']
# my_list.append(True)
# my_list.append([3, 4, 5])
# print(my_list)

# # Appending Elements to an Empty List:
# empty_list = []
# empty_list.append(10)
# empty_list.append(20)
# print(empty_list)  # Output: [10, 20]

# # Appending a List to Another List:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(list2)
# print(list1)  # Output: [1, 2, 3, [4, 5, 6]]

# # Appending Elements in a Loop:
# my_list = []
# for i in range(10):
#     my_list.append(i)
# print(my_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Appending Elements Using List Comprehension:
# my_list = [i for i in range(5)]
# print(my_list)  # Output: [0, 1, 2, 3, 4]

# # Appending different data types
# mixed_list = []

# mixed_list.append(10)        # Integer
# mixed_list.append(3.14)      # Float
# mixed_list.append("Hello")   # String
# mixed_list.append(True)      # Boolean
# mixed_list.append([1, 2, 3]) # List

# print(mixed_list) # Output: [10, 3.14, 'Hello', True, [1, 2, 3]]

# # Using concatenation
# original_list = [1, 2, 3]
# new_list = original_list + [4]  # Using concatenation
# print(new_list)  # Output: [1, 2, 3, 4]

# another_list = original_list[:]  # Using slicing to create a copy
# another_list.append(5)
# print(another_list)  # Output: [1, 2, 3, 5]
# print(original_list)  # Output: [1, 2, 3] (original list is not modified)

# '''''''''''''''''''''''''''''''extend() method''''''''''''''''''''''''''
# 1. Basic Usage
# Define a list
my_list = [1, 2, 3]

# Extend the list with elements from another list
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 2. Extending with Different Data Types:
# Extend a list with elements from another list
my_list = [1, 2, 3, 4]
