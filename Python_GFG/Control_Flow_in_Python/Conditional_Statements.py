# # '''''''''''''''''''''''''''''''1.if Statement''''''''''''''''''''''''''
# def main():
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You are eligible to vote.")
#         if age >= 65:
#             print("You are also eligible for senior citizen benefits.")
#         else:
#             print("You are not eligible for senior citizen benefits.")
#     else:
#         print("You are not eligible to vote.")
#         if age < 5:
#             print("You are too young to attend school.")
#         else:
#             print("You can attend school.")

#     grade = input("Enter your grade (A, B, C, D, F): ")
#     if grade == 'A':
#         print("Excellent!")
#     elif grade == 'B':
#         print("Good job!")
#     elif grade == 'C':
#         print("You can do better.")
#     elif grade == 'D':
#         print("You need to improve.")
#     else:
#         print("You failed!")

#     for i in range(1, 11):
#         if i % 2 == 0:
#             print(f"{i} is even.")
#         else:
#             print(f"{i} is odd.")

#     total = 0
#     numbers = [1, 2, 3, 4, 5]
#     for num in numbers:
#         total += num

#     if total > 10:
#         print("The sum of numbers is greater than 10.")
#     else:
#         print("The sum of numbers is not greater than 10.")

#     if age >= 21 and grade == 'A':
#         print("You are eligible for a scholarship.")

# if __name__ == "__main__":
#     main()

# # ''''''''''''''''nested if statements''''''''''''''''''
# # Input data
# exam_score = 75
# participation = "yes"

# # Outer if statement checks the exam score
# if exam_score >= 70:
#     # If the score is 70 or higher, we enter this block
#     print("You passed the exam!")
    
#     # Nested if statement checks participation
#     if participation == "yes":
#         print("You participated actively in class.")
#     else:
#         print("You didn't participate in class.")
# else:
#     # If the score is below 70, we enter this block
#     print("You didn't pass the exam.")

# # Output:
# # You passed the exam!
# # You participated actively in class.

# # '''''''''''''''''''

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# value = 42
# is_even = value % 2 == 0

# if is_prime(value):
#     print("Value is a prime number.")
# elif is_even:
#     print("Value is even.")
# else:
#     print("Value is neither prime nor even.")
    
# if 30 < value < 50:
#     print("Value is between 30 and 50.")
    
# if value > 100 and (value % 7 == 0 or value % 11 == 0):
#     print("Value is greater than 100 and divisible by 7 or 11.")
    
# if value % 3 == 0:
#     print("Value is divisible by 3.")

# # ''''''''''''''''''''''''
# age = 25
# income = 55000
# education_level = "Master's"

# if age < 18:
#     print("You are too young.")
# elif age >= 18 and age <= 30:
#     print("You are in the 18-30 age group.")
#     if income >= 50000:
#         print("You have a good income.")
#     else:
#         print("You need to work on increasing your income.")
#     if education_level == "Ph.D." or education_level == "Master's":
#         print("You have an advanced degree.")
#     else:
#         print("Consider pursuing higher education.")
# elif age > 30 and age <= 50:
#     print("You are in the 31-50 age group.")
#     if income >= 70000:
#         print("You have a high income.")
#     else:
#         print("Work on advancing your career.")
#     if education_level == "Ph.D." or education_level == "Master's":
#         print("You have an advanced degree.")
#     else:
#         print("Consider further education.")
# else:
#     print("You are in the 51+ age group.")
#     if income >= 60000:
#         print("You have a decent income.")
#     else:
#         print("You can explore opportunities for income growth.")
#     if education_level == "Ph.D." or education_level == "Master's":
#         print("You have an advanced degree.")
#     else:
#         print("Education can still be beneficial.")
        
# # '''''''''''''''''''''''
# # Example of an 80-line if statement (for demonstration purposes only)
# x = 10
# y = 5
# z = 15
# a = 20
# b = 25
# c = 30

# if x > 5:
#     print("x is greater than 5.")
#     if y > 2:
#         print("y is also greater than 2.")
#         if z > 10:
#             print("z is greater than 10.")
#             if a > 15:
#                 print("a is greater than 15.")
#                 if b > 20:
#                     print("b is greater than 20.")
#                     if c > 25:
#                         print("c is greater than 25.")
#                     else:
#                         print("c is not greater than 25.")
#                 else:
#                     print("b is not greater than 20.")
#             else:
#                 print("a is not greater than 15.")
#         else:
#             print("z is not greater than 10.")
#     else:
#         print("y is not greater than 2.")
# else:
#     print("x is not greater than 5.")


# print("This is outside of the if statements.")

# # ''''''''''''''
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def classify_number(num):
#     if num % 2 == 0:
#         if num < 0:
#             print("Negative even number")
#         elif num == 0:
#             print("Zero")
#         elif num % 4 == 0:
#             print("Even number divisible by 4")
#         else:
#             print("Even number")
#     else:
#         if is_prime(num):
#             print("Prime number")
#         else:
#             print("Odd number")

# def main():
#     number = int(input("Enter a number: "))
    
#     if number > 100:
#         print("The number is greater than 100.")
#     elif number >= 50:
#         print("The number is between 50 and 100 (inclusive).")
#     elif number >= 0:
#         print("The number is non-negative and less than 50.")
#         classify_number(number)
#     else:
#         print("The number is negative.")
#         if number >= -10:
#             print("The number is greater than or equal to -10.")
#         else:
#             print("The number is less than -10.")
    
#     # More conditions and code can be added here
    
# if __name__ == "__main__":
#     main()

# # ''''''''''''''''''

# # Function to check if a number is even
# def is_even(number):
#     return number % 2 == 0

# # Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
    
#     if number % 2 == 0 or number % 3 == 0:
#         return False
    
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
    
#     return True

# # Main function
# def main():
#     num = 17
    
#     if is_even(num) and is_prime(num):
#         print(f"{num} is both even and prime.")
#     elif is_even(num) and not is_prime(num):
#         print(f"{num} is even but not prime.")
#     elif not is_even(num) and is_prime(num):
#         print(f"{num} is odd and prime.")
#     else:
#         print(f"{num} is neither even nor prime.")

# if __name__ == "__main__":
#     main()

# # ''''''''''''''''''''''Ternary Condition Expression''''''''''''''''
# x = 10
# y = 20

# max_value = x if x > y else y

# print(max_value)  # This will print 20 because y is greater than x

# # ''''''''''''''''''''
# # A simple function that uses a ternary conditional expression
# def get_grade(score):
#     # Using a ternary expression to determine the grade
#     grade = 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'F'))
#     return grade

# # Test the function with different scores
# scores = [95, 85, 75, 60]
# for score in scores:
#     grade = get_grade(score)
#     print(f"Score: {score}, Grade: {grade}")

# # Using ternary expressions in a dictionary
# fruit = 'apple'
# color = 'red' if fruit == 'apple' else ('yellow' if fruit == 'banana' else 'unknown')
# print(f"The color of the fruit is {color}")

# # Ternary expression in list comprehensions
# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 if x % 2 == 0 else x for x in numbers]
# print("Squared numbers:", squared)

# # Ternary expression for a more complex condition
# age = 25
# is_adult = True if age >= 18 and age <= 65 else False
# print("Is the person an adult?", is_adult)

# # '''''''''''''''''''''''''''''
# # Define a list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Use a ternary conditional expression along with a lambda function and map
# # to create a new list containing squared even numbers and cubed odd numbers
# result = [(lambda x: x**2 if x % 2 == 0 else x**3)(num) for num in numbers]

# # Print the result
# print(result)

# # ''''''''''''''''''''''''''
# y = 20
# x = 10

# # Create a generator expression with advanced logic
# result = (i for i in range(x, y) if i % 2 == 0) if x < y else (i for i in range(y, x) if i % 2 != 0)

# # Extract the first value from the generator (you can modify this logic)
# final_result = next(result, None)

# print(final_result)

# # '''''''''''''''''''''''''''Short-circuiting in logical expressions''''''''''''
# '''Short-circuiting with the and operator:'''
# '''when (x > 0) is False, there is no need to evaluate (y / x > 2), so Python short-circuits the evaluation, and the result is False.'''
# x = 5
# y = 10

# # Using 'and' operator
# result = (x > 0) and (y / x > 2)
# print("Result:", result)

# # ''''''''''
# '''Short-circuiting with the or operator:'''
# '''when (a > 0) is True, Python doesn't need to evaluate (1 / b > 0), and it short-circuits the evaluation, resulting in True.'''
# a = 3
# b = 0

# # Using 'or' operator
# result = (a > 0) or (1 / b > 0)
# print("Result:", result)

# # ''''''''''''''''''Conditional Statement with Lists'''''''''''''''''''''''
# # Check if an element is in a list
# my_list = [1, 2, 3, 4, 5]
# if 3 in my_list:
#     print("3 is in the list")

# # Check if a list is empty
# empty_list = []
# if not empty_list:
#     print("The list is empty")

# # Check the length of a list
# if len(my_list) > 3:
#     print("The list has more than 3 elements")

# # Check if an element is present in a list using in keyword:
# my_list = [1, 2, 3, 4, 5]
# element_to_check = 3

# if element_to_check in my_list:
#     print(f"{element_to_check} is present in the list.")
# else:
#     print(f"{element_to_check} is not present in the list.")
    
# # Use a conditional statement to filter elements in a list:
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print("Even numbers:", even_numbers)

# # Initialize a list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Iterate through the list and apply conditional statements
# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")

#     if num > 5:
#         print(f"{num} is greater than 5.")
#     elif num == 5:
#         print(f"{num} is equal to 5.")
#     else:
#         print(f"{num} is less than 5.")

#     if num % 3 == 0 and num % 5 == 0:
#         print(f"{num} is divisible by both 3 and 5.")
#     elif num % 3 == 0:
#         print(f"{num} is divisible by 3 but not 5.")
#     elif num % 5 == 0:
#         print(f"{num} is divisible by 5 but not 3.")
#     else:
#         print(f"{num} is neither divisible by 3 nor 5.")

#     if num in [2, 3, 5, 7]:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")

#     if num == 1 or num == 9:
#         print(f"{num} is at the beginning or end of the list.")
#     elif num in numbers[1:-1]:
#         print(f"{num} is in the middle of the list.")

#     print("-" * 40)  # Separator for better readability

# # Check if all elements in the list are even
# if all(x % 2 == 0 for x in my_list):
#     print("All elements are even")
    

# # Check if any element in the list is odd
# if any(x % 2 != 0 for x in my_list):
#     print("At least one element is odd")

# # Find the maximum and minimum elements in the list
# max_val = max(my_list)
# min_val = min(my_list)
# print(f"Maximum value: {max_val}, Minimum value: {min_val}")

# # Sum all elements in the list
# sum_val = sum(my_list)
# print(f"Sum of all elements: {sum_val}")

# # Create a new list with elements greater than 5
# new_list = [x for x in my_list if x > 5]
# print("Elements greater than 5:", new_list)

# # Create a new list with elements squared
# squared_list = [x ** 2 for x in my_list]
# print("List with elements squared:", squared_list)

# # Add 10 to every element in the list
# updated_list = [x + 10 for x in my_list]
# print("List with 10 added to each element:", updated_list)

# # Remove duplicates from the list
# my_list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5]
# unique_list = list(set(my_list_with_duplicates))
# print("List with duplicates removed:", unique_list)

# # Check if the list is sorted in ascending order
# if my_list == sorted(my_list):
#     print("The list is sorted in ascending order")

# # Sort the list in descending order
# my_list.sort(reverse=True)
# print("List sorted in descending order:", my_list)

# # Reverse the list
# my_list.reverse()
# print("Reversed list:", my_list)

# # Check if the list contains only positive numbers
# if all(x > 0 for x in my_list):
#     print("All elements are positive")

# # Check if the list contains any negative numbers
# if any(x < 0 for x in my_list):
#     print("At least one element is negative")

# # ''''''''''''''''''''
# # Initialize a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Create empty lists for different categories
# even_numbers = []
# odd_numbers = []
# greater_than_5 = []
# squares_gt_50 = []
# multiples_of_3 = []
# not_in_list = []

# # Loop through the list and apply conditional statements
# for num in my_list:
#     # Check if the number is even or odd
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
    
#     # Check if the number is greater than 5
#     if num > 5:
#         greater_than_5.append(num)
    
#     # Calculate the square of the number and check if it's greater than 50
#     squared = num ** 2
#     if squared > 50:
#         squares_gt_50.append((num, squared))
    
#     # Check if the number is a multiple of 3
#     if num % 3 == 0:
#         multiples_of_3.append(num)
    
#     # Check if the number is not in a specific list
#     if num not in [1, 4, 7]:
#         not_in_list.append(num)

# # Print the results
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
# print("Numbers greater than 5:", greater_than_5)
# print("Numbers whose squares are greater than 50:", squares_gt_50)
# print("Multiples of 3:", multiples_of_3)
# print("Numbers not in [1, 4, 7]:", not_in_list)

# # Modify the original list based on conditions
# for num in my_list.copy():  # Create a copy to avoid modifying while iterating
#     if num % 3 == 0:
#         my_list.remove(num)

# # Print the modified list
# print("Modified list after removing multiples of 3:", my_list)

# # ''''''''''''
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Check if an element is in a list:
# if 4 in my_list:
#     print("4 is found in my_list")
# if 15 not in my_list:
#     print("5 is not in my_list")

# # Check if a list is empty:
# empty_list = []
# if not my_list:
#     print("Empty list = []")
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if my_list:
#     print("my_list is not empty")

# # Check if a list contains only unique elements:
# if len(my_list) == len(set(my_list)):
#     print("my_list contains only unique elements")

# # Check if a list contains duplicates:
# if len(my_list) != len(set(my_list)):
#     print("my_list contains dublicates elements")

# # Check if a list is sorted in ascending order:
# if my_list == sorted(my_list):
#     print("my_list is sorted")
    
# # Check if a list is sorted in descending order:
# if my_list == sorted(my_list, reverse=True):
#     print("my_list is sorted in decreasing order")

# # Check if a list contains a sublist:
# sub_list = [4,5,6,7]
# if sub_list in my_list:
#     print("my_list contains a sublist sub_list")

# # '''''''''''''''''''''''''''''
# # Initialize a list
# my_list = [5, 2, 9, 1, 7, 8, 3, 6, 4, 10]

# # Advanced conditional statements and list operations
# even_numbers = [x for x in my_list if x % 2 == 0]
# odd_numbers = [x for x in my_list if x % 2 != 0]
# greater_than_5 = [x for x in my_list if x > 5]
# squares_gt_50 = [x ** 2 for x in my_list if x ** 2 > 50]
# multiples_of_3 = [x for x in my_list if x % 3 == 0]
# not_in_list = [x for x in my_list if x not in [1, 4, 7]]

# # Sorting the list using a lambda function
# my_list.sort(key=lambda x: -x)  # Sort in descending order

# # Print the results
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
# print("Numbers greater than 5:", greater_than_5)
# print("Squares greater than 50:", squares_gt_50)
# print("Multiples of 3:", multiples_of_3)
# print("Numbers not in [1, 4, 7]:", not_in_list)
# print("Sorted list (descending order):", my_list)

# # ''''''''''''''''''''''''''
# # Initialize a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # List comprehensions with conditionals
# even_numbers = [num for num in my_list if num % 2 == 0]
# odd_numbers = [num for num in my_list if num % 2 != 0]
# greater_than_5 = [num for num in my_list if num > 5]

# # Advanced list operations using lambda functions and map
# squared_values = list(map(lambda x: x**2, my_list))
# doubled_values = list(map(lambda x: x * 2, my_list))
# filtered_values = list(filter(lambda x: x % 3 == 0, my_list))

# # List slicing
# first_half = my_list[:len(my_list)//2]
# second_half = my_list[len(my_list)//2:]

# # Conditional statements with all() and any()
# all_positive = all(num > 0 for num in my_list)
# any_below_5 = any(num < 5 for num in my_list)

# # Sort the list using a custom key function
# sorted_list = sorted(my_list, key=lambda x: abs(5 - x))

# # Group elements into dictionaries based on conditions
# grouped_dict = {
#     'even': [num for num in my_list if num % 2 == 0],
#     'odd': [num for num in my_list if num % 2 != 0],
#     'squares_gt_50': [num for num in my_list if num**2 > 50],
# }

# # Flatten a list of lists
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flattened_list = [item for sublist in nested_list for item in sublist]

# # Conditional list comprehension
# conditional_comprehension = [x if x % 2 == 0 else x * 2 for x in my_list]

# # Print the results
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
# print("Numbers greater than 5:", greater_than_5)
# print("Squared values:", squared_values)
# print("Doubled values:", doubled_values)
# print("Filtered values:", filtered_values)
# print("First half of the list:", first_half)
# print("Second half of the list:", second_half)
# print("All positive numbers:", all_positive)
# print("Any number below 5:", any_below_5)
# print("Sorted list:", sorted_list)
# print("Grouped values:", grouped_dict)
# print("Flattened list:", flattened_list)
# print("Conditional comprehension:", conditional_comprehension)

# # '''''''''''''''''''''''''''''''
# # Conditional statements with Lists and Strings

# # List with some numbers and strings
# mixed_list = [1, 'apple', 3, 'banana', 5, 'cherry']

# # Initialize empty lists to store results
# numbers = []
# fruits = []
# other = []

# # Iterate through the mixed list
# for item in mixed_list:
#     if isinstance(item, int):
#         numbers.append(item)
#     elif isinstance(item, str):
#         if item.lower() in ['apple', 'banana', 'cherry']:
#             fruits.append(item)
#         else:
#             other.append(item)

# # Check if a specific fruit is in the list of fruits
# fruit_to_check = 'apple'
# if fruit_to_check in fruits:
#     print(f"{fruit_to_check} is in the list of fruits.")

# # Check if there are any numbers in the list
# if numbers:
#     print("There are numbers in the list.")

# # Check if all fruits contain the letter 'a'
# if all('a' in fruit for fruit in fruits):
#     print("All fruits contain the letter 'a'.")

# # Check if any element in the 'other' list is longer than 5 characters
# if any(len(item) > 5 for item in other):
#     print("There is an element in 'other' longer than 5 characters.")

# # Printing the results
# print("Numbers:", numbers)
# print("Fruits:", fruits)
# print("Other:", other)

# # '''''''''''''''''''''''''''''''''''''Comparison string using conditional statements'''''''''''''''''''''''''''
# # Define three sample strings
# string1 = "Hello, World!"
# string2 = "hello, world!"
# string3 = "Python is awesome!"

# # Using equality operator (case-sensitive)
# if string1 == string2:
#     print("Strings 1 and 2 are equal (case-sensitive)")
# else:
#     print("Strings 1 and 2 are not equal (case-sensitive)")

# # Using equality operator (case-insensitive)
# if string1.lower() == string2.lower():
#     print("Strings 1 and 2 are equal (case-insensitive)")
# else:
#     print("Strings 1 and 2 are not equal (case-insensitive)")

# # Using comparison operators (case-sensitive)
# if string1 < string2:
#     print("String 1 is less than string 2")
# elif string1 > string2:
#     print("String 1 is greater than string 2")
# else:
#     print("Strings 1 and 2 are equal (case-sensitive)")

# # Using str.startswith() and str.endswith() methods
# if string1.startswith("Hello") and string2.endswith("world!"):
#     print("String 1 starts with 'Hello' and String 2 ends with 'world!'")

# # Using regular expressions (import re required)
# import re
# pattern = r"[A-Za-z]+"
# if re.match(pattern, string1) and re.match(pattern, string2):
#     print("Both strings 1 and 2 contain only letters")

# # Using custom function to compare
# def custom_compare(str1, str2):
#     return str1 == str2

# if custom_compare(string1, string2):
#     print("Custom comparison: Strings 1 and 2 are equal")
# else:
#     print("Custom comparison: Strings 1 and 2 are not equal")

# # Comparing string 1 and string 3
# if string1 != string3:
#     print("Strings 1 and 3 are not equal")

# # Using string slicing for comparison
# substring1 = string1[0:5]
# substring2 = string3[-7:]
# if substring1 == substring2:
#     print("Substring comparison: First 5 characters of string 1 and last 7 characters of string 3 are equal")

# # Checking if string 1 contains string 2 as a substring
# if string2 in string1:
#     print("String 1 contains string 2 as a substring")

# # Using difflib for advanced string comparison
# import difflib
# differ = difflib.Differ()
# diff = list(differ.compare(string1, string3))
# print("Differences between string 1 and string 3:")
# for d in diff:
#     if d.startswith('- '):
#         print(f"String 1 has: {d[2:]}")
#     elif d.startswith('+ '):
#         print(f"String 3 has: {d[2:]}")

# # Checking if strings are anagrams
# from collections import Counter
# def are_anagrams(str1, str2):
#     return Counter(str1) == Counter(str2)

# if are_anagrams(string1, string2):
#     print("Strings 1 and 2 are anagrams")
# else:
#     print("Strings 1 and 2 are not anagrams")

# # Levenshtein distance (edit distance) between strings
# def levenshtein_distance(s1, s2):
#     if len(s1) < len(s2):
#         return levenshtein_distance(s2, s1)
#     if len(s2) == 0:
#         return len(s1)
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[j + 1] + 1
#             deletions = current_row[j] + 1
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#     return previous_row[-1]

# distance = levenshtein_distance(string1, string3)
# print(f"Levenshtein distance between string 1 and string 3: {distance}")

# # ''''''''''''''''''''''''''''''Conditional statement with user input'''''''''''''''''''''''''''''''''''''
# # Get user input for age
# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Invalid input. Please enter a valid age as a number.")
#     exit(1)

# # Conditional statements based on user input
# if age < 0:
#     print("Age cannot be negative.")
# elif age < 18:
#     print("You are a minor.")
#     if age < 6:
#         print("You are a preschooler.")
#     elif age < 12:
#         print("You are a child.")
#     else:
#         print("You are a teenager.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# # Ask the user for a preference
# preference = input("Do you prefer pizza or pasta? ").strip().lower()

# # Conditional statements based on user preference
# if preference == "pizza":
#     print("Great choice! Pizza is delicious.")
# elif preference == "pasta":
#     print("Pasta is a classic dish. Enjoy!")
# else:
#     print("I'm not sure what that is, but I'm sure it's tasty!")

# # Ask the user for a yes/no answer
# answer = input("Do you want to continue? (yes/no) ").strip().lower()

# # Conditional statements based on the user's answer
# if answer == "yes":
#     print("Continuing...")
# elif answer == "no":
#     print("Exiting the program.")
# else:
#     print("Invalid input. Please enter 'yes' or 'no'.")

# # Perform a loop based on user input
# while True:
#     choice = input("Do you want to play a game? (yes/no) ").strip().lower()
#     if choice == "yes":
#         print("Let's play!")
#         break
#     elif choice == "no":
#         print("Maybe next time.")
#         break
#     else:
#         print("Invalid input. Please enter 'yes' or 'no'.")

# # Input validation and retry
# while True:
#     user_input = input("Enter a number between 1 and 10: ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         if 1 <= user_number <= 10:
#             print(f"Good choice! You entered {user_number}.")
#             break
#         else:
#             print("The number is not within the specified range.")
#     else:
#         print("Invalid input. Please enter a valid number between 1 and 10.")

# # Handling multiple options with user input
# menu = {
#     '1': "Option 1: Perform task 1",
#     '2': "Option 2: Perform task 2",
#     '3': "Option 3: Perform task 3",
# }

# while True:
#     print("Menu:")
#     for key, value in menu.items():
#         print(f"{key}: {value}")
    
#     user_choice = input("Enter your choice (1/2/3): ")
    
#     if user_choice in menu:
#         print(menu[user_choice])
#         break
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")


# # ''''''''''''''''''''''''''''''''''''
# # Get user input
# user_age = int(input("Enter your age: "))
# user_gender = input("Enter your gender (M/F): ").upper()
# user_income = float(input("Enter your annual income: $"))

# # Complex conditional logic based on user input
# if user_age < 18:
#     print("You are underage.")
# elif 18 <= user_age < 65:
#     print("You are of working age.")
# else:
#     print("You are of retirement age.")

# if user_gender == 'M':
#     print("You are a male.")
# elif user_gender == 'F':
#     print("You are a female.")
# else:
#     print("You did not specify a valid gender.")

# if user_income < 5000:
#     print("Your income is low.")
# elif 5000 <= user_income < 30000:
#     print("Your income is moderate.")
# elif 30000 <= user_income < 100000:
#     print("Your income is high.")
# else:
#     print("Your income is very high.")

# # Complex conditional logic combining conditions
# if user_age < 18:
#     if user_income < 10000:
#         print("You are a young person with low income.")
#     else:
#         print("You are a young person with a decent income.")
# elif 18 <= user_age < 65:
#     if user_gender == 'M':
#         if user_income < 30000:
#             print("You are a working-age man with a moderate income.")
#         else:
#             print("You are a working-age man with a high income.")
#     elif user_gender == 'F':
#         if user_income < 30000:
#             print("You are a working-age woman with a moderate income.")
#         else:
#             print("You are a working-age woman with a high income.")
# else:
#     print("You are of retirement age.")

# # ''''''''''''''''''''''''''''''''''''''''''Conditional Statements with dictionaries''''''''''''''''''''''''''''''''''
# # Create a dictionary of students and their scores
# student_scores = {
#     "Alice": 95,
#     "Bob": 88,
#     "Charlie": 72,
#     "David": 64,
#     "Eva": 98,
#     "Frank": 81,
#     "Grace": 90,
# }

# # Conditional statements with dictionaries
# for student, score in student_scores.items():
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
    
#     print(f"{student}: Score = {score}, Grade = {grade}")

# # Conditional statements using dictionary values
# search_name = "Eva"
# if search_name in student_scores:
#     score = student_scores[search_name]
#     if score >= 90:
#         print(f"{search_name} has an excellent score.")
#     elif 80 <= score < 90:
#         print(f"{search_name} has a very good score.")
#     elif 70 <= score < 80:
#         print(f"{search_name} has a good score.")
#     elif 60 <= score < 70:
#         print(f"{search_name} has a satisfactory score.")
#     else:
#         print(f"{search_name} needs improvement.")
# else:
#     print(f"{search_name} is not in the list of students.")
    
# # Create a dictionary of fruits and their quantities
# fruits_inventory = {
#     "Apple": 50,
#     "Banana": 30,
#     "Cherry": 45,
#     "Date": 15,
#     "Elderberry": 20,
#     "Fig": 10,
#     "Grape": 35,
# }

# # Define a function to check if a fruit is in stock
# def is_in_stock(fruit, quantity):
#     return fruit in fruits_inventory and fruits_inventory[fruit] >= quantity

# # Conditional statements with dictionaries and functions
# order = [("Apple", 10), ("Cherry", 50), ("Grape", 40), ("Kiwi", 5)]

# for fruit, quantity in order:
#     if is_in_stock(fruit, quantity):
#         print(f"We have enough {fruit} in stock to fulfill your order of {quantity}.")
#     else:
#         print(f"We don't have enough {fruit} in stock to fulfill your order of {quantity}.")

# # Conditional statements with dictionary comprehensions
# excellent_students = {name: score for name, score in student_scores.items() if score >= 90}
# print("Excellent Students:", excellent_students)

# # Perform operations with dictionaries
# total_score = sum(student_scores.values())
# average_score = total_score / len(student_scores)
# print(f"Total Score: {total_score}, Average Score: {average_score}")

# # Find students with the highest and lowest scores
# highest_scorer = max(student_scores, key=student_scores.get)
# lowest_scorer = min(student_scores, key=student_scores.get)
# print(f"Highest Scorer: {highest_scorer}, Lowest Scorer: {lowest_scorer}")

# # Modify scores for specific students
# student_scores["Eva"] += 5
# student_scores["David"] -= 3

# # Check if a student's score improved
# if student_scores["Eva"] > 88:
#     print("Eva's score improved.")
# else:
#     print("Eva's score did not improve.")

# # Remove a student from the dictionary
# removed_student = student_scores.pop("Charlie", None)
# if removed_student is not None:
#     print(f"{removed_student}'s record removed.")
# else:
#     print("Charlie was not found in the list of students.")

# # ''''''''''''''''''''''''''''''''''''
# # Conditional statements with dictionary comprehensions
# excellent_students = {name: score for name, score in student_scores.items() if score >= 90}
# print("Excellent Students:", excellent_students)

# # Calculate the average score of all students
# total_scores = sum(student_scores.values())
# average_score = total_scores / len(student_scores)
# print(f"Average Score: {average_score:.2f}")

# # Create a dictionary of subjects and corresponding scores
# subject_scores = {
#     "Math": {"Alice": 90, "Bob": 85, "Charlie": 92},
#     "Science": {"Alice": 88, "David": 92, "Eva": 78},
#     "History": {"Bob": 85, "Charlie": 88, "David": 95, "Eva": 88},
# }

# # Find the subject with the highest average score
# best_subject = None
# best_average = 0

# for subject, scores in subject_scores.items():
#     subject_average = sum(scores.values()) / len(scores)
#     if subject_average > best_average:
#         best_subject = subject
#         best_average = subject_average

# print(f"The subject with the highest average score is {best_subject}.")

# # '''''''''''''''''''''''''''''''''''''''''''''
# # Define a dictionary of student records with advanced data structure
# students = {
#     "Alice": {
#         "scores": {"Math": 90, "Science": 88, "History": 85},
#         "attendance": {"January": True, "February": False, "March": True},
#     },
#     "Bob": {
#         "scores": {"Math": 85, "Science": 92, "History": 88},
#         "attendance": {"January": False, "February": True, "March": True},
#     },
#     "Charlie": {
#         "scores": {"Math": 92, "Science": 78, "History": 88},
#         "attendance": {"January": True, "February": True, "March": True},
#     },
# }

# # Define a function to calculate the GPA of a student
# def calculate_gpa(scores):
#     total_score = sum(scores.values())
#     return total_score / len(scores)

# # Calculate the GPA for each student and store it in a new dictionary
# student_gpa = {name: calculate_gpa(record["scores"]) for name, record in students.items()}

# # Find the student with the highest GPA
# best_student = max(student_gpa, key=student_gpa.get)
# best_gpa = student_gpa[best_student]

# print(f"The student with the highest GPA is {best_student} with a GPA of {best_gpa:.2f}.")

# # Check attendance for a specific month
# search_month = "February"
# absent_students = [name for name, record in students.items() if not record["attendance"].get(search_month, False)]

# if absent_students:
#     print(f"The following students were absent in {search_month}: {', '.join(absent_students)}")
# else:
#     print(f"All students were present in {search_month}.")

# # Conditional statements with advanced dictionary comprehension
# high_scorers = {name: record["scores"] for name, record in students.items() if calculate_gpa(record["scores"]) >= 90}

# print("High Scorers:")
# for name, scores in high_scorers.items():
#     print(f"{name}: {', '.join([f'{subject}: {score}' for subject, score in scores.items()])}")

# # '''''''''''''''''''''''''''''''''
# # Create a dictionary of students and their exam scores
# student_scores = {
#     "Alice": {"Math": 85, "Science": 92, "History": 78},
#     "Bob": {"Math": 92, "Science": 88, "History": 95},
#     "Charlie": {"Math": 78, "Science": 85, "History": 90},
#     "David": {"Math": 95, "Science": 90, "History": 88},
#     "Eva": {"Math": 88, "Science": 92, "History": 85},
# }

# # Define a function to classify students based on their scores
# def classify_students(scores):
#     classifications = {}
#     for name, subject_scores in scores.items():
#         total_score = sum(subject_scores.values())
#         if total_score >= 270:
#             classifications[name] = "Excellent"
#         elif 240 <= total_score < 270:
#             classifications[name] = "Very Good"
#         elif 210 <= total_score < 240:
#             classifications[name] = "Good"
#         else:
#             classifications[name] = "Needs Improvement"
#     return classifications

# # Get the classifications of students
# student_classifications = classify_students(student_scores)

# # Display the classifications
# for name, classification in student_classifications.items():
#     print(f"{name}: {classification}")

# # Find the best subject for each student
# best_subjects = {}
# for name, subject_scores in student_scores.items():
#     best_subject = max(subject_scores, key=subject_scores.get)
#     best_subjects[name] = best_subject

# print("Best Subjects:")
# for name, subject in best_subjects.items():
#     print(f"{name}: {subject}")

# # Create a dictionary of subjects and their difficulty levels
# subject_difficulty = {
#     "Math": "Hard",
#     "Science": "Moderate",
#     "History": "Easy",
# }

# # Filter students based on their best subject's difficulty level
# difficult_subject_students = {
#     name: best_subjects[name]
#     for name in best_subjects
#     if subject_difficulty[best_subjects[name]] == "Hard"
# }

# print("Students with a Difficult Best Subject:")
# for name, subject in difficult_subject_students.items():
#     print(f"{name}: {subject}")

# # Calculate the average score for each subject
# subject_averages = {}
# for subject in subject_scores.values():
#     total_score = sum(subject.values())
#     subject_averages[subject] = total_score / len(subject)

# print("Subject Averages:")
# for subject, average in subject_averages.items():
#     print(f"{subject}: {average:.2f}")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Create a dictionary of products with their prices and quantities
# products = {
#     "apple": {"price": 0.5, "quantity": 100},
#     "banana": {"price": 0.25, "quantity": 150},
#     "cherry": {"price": 1.0, "quantity": 50},
#     "date": {"price": 0.75, "quantity": 75},
#     "elderberry": {"price": 1.5, "quantity": 25},
#     "fig": {"price": 1.2, "quantity": 60},
#     "grape": {"price": 0.8, "quantity": 120},
# }

# # Define a function to calculate the total value of products
# def calculate_total(products_dict):
#     total = sum(product["price"] * product["quantity"] for product in products_dict.values())
#     return total

# # Calculate and print the total value of products
# total_value = calculate_total(products)
# print(f"Total value of products: ${total_value:.2f}")

# # Define a function to find the most expensive product
# def find_most_expensive(products_dict):
#     most_expensive = max(products_dict, key=lambda x: products_dict[x]["price"])
#     return most_expensive, products_dict[most_expensive]["price"]

# # Find and print the most expensive product
# most_expensive_product, price = find_most_expensive(products)
# print(f"The most expensive product is {most_expensive_product} priced at ${price:.2f}")

# # Define a function to filter products with low quantities
# def filter_low_quantity(products_dict, threshold):
#     return {product: data for product, data in products_dict.items() if data["quantity"] < threshold}

# # Filter and print products with low quantities (less than 50)
# low_quantity_products = filter_low_quantity(products, 50)
# print("Products with low quantities:", low_quantity_products)

# # Define a function to sort products by price in descending order
# def sort_products_by_price(products_dict):
#     return dict(sorted(products_dict.items(), key=lambda x: x[1]["price"], reverse=True))

# # Sort and print products by price
# sorted_products = sort_products_by_price(products)
# print("Products sorted by price:", sorted_products)

# ''''''''''''''''''''''''''''''''''''''''''''''Conditional statements with sets'''''''''''''''''''''''''''''''

