# # '''''''''''''''''''''''''''''''''''''''''''Integer Operation''''''''''''''''''''''''''''''''''''''''''''''
# # 1.Arithmatic Operation
# # Declaration and Assignment
# a = 10
# b = 3

# # Addition
# sum_result = a + b  # 13

# # Subtraction
# diff_result = a - b  # 7

# # Multiplication
# prod_result = a * b  # 30

# # Division
# div_result = a / b   # 3.333...

# # Modulus
# mod_result = a % b   # 1

# # Floor Division
# div_floor_result = a // b  # 3

# # Exponentiation
# exponent_result = a ** 2  # 100

# # Displaying Results
# print("Addition:", sum_result)
# print("Subtraction:", diff_result)
# print("Multiplication:", prod_result)
# print("Division:", div_result)
# print("Modulus:", mod_result)
# print("Floor Division:", div_floor_result)
# print("Exponentiation:", exponent_result)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Floor Division (//) with Positive Numbers
# a = 10
# b = 3
# div_floor_result = a // b  # 3
# print("Floor Division (//) with Positive Numbers:", div_floor_result)

# # Floor Division (//) with Negative Numbers
# c = -10
# d = 3
# div_floor_negative_result = c // d  # -4
# print("Floor Division (//) with Negative Numbers:", div_floor_negative_result)

# # Floor Division (//) with Mixed Signs
# e = 10
# f = -3
# div_floor_mixed_result = e // f  # -4
# print("Floor Division (//) with Mixed Signs:", div_floor_mixed_result)

# # Floor Division (//) with Zero as Denominator
# g = 10
# h = 0
# try:
#     div_floor_zero_result = g // h  # Raises ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot perform floor division when the denominator is zero.")

# # ''''''''''''''''''''''''''''''''''''Exponentiation(**)''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Exponentiation (**) with Positive Numbers
# a = 2
# b = 3
# exponent_result = a ** b  # 2^3 = 8
# print("Exponentiation (**) with Positive Numbers:", exponent_result)

# # Exponentiation (**) with Negative Numbers
# c = -2
# d = 3
# exponent_negative_result = c ** d  # (-2)^3 = -8
# print("Exponentiation (**) with Negative Numbers:", exponent_negative_result)

# # Exponentiation (**) with Zero as Exponent
# e = 2
# f = 0
# exponent_zero_result = e ** f  # 2^0 = 1
# print("Exponentiation (**) with Zero as Exponent:", exponent_zero_result)

# # Exponentiation (**) with Negative Base and Even Exponent
# g = -2
# h = 2
# exponent_negative_base_even_result = g ** h  # (-2)^2 = 4
# print("Exponentiation (**) with Negative Base and Even Exponent:", exponent_negative_base_even_result)

# # Exponentiation (**) with Negative Base and Odd Exponent
# i = -2
# j = 3
# exponent_negative_base_odd_result = i ** j  # (-2)^3 = -8
# print("Exponentiation (**) with Negative Base and Odd Exponent:", exponent_negative_base_odd_result)

# # ''''''''''''''''''''''''''''''''''Comparision Operations'''''''''''''''''''''''''''''''''
# # Declaration and Assignment
# a = 10
# b = 3

# # Equality (==)
# equal_result = a == b  # False
# print("Equality (==):", equal_result)

# # Inequality (!=)
# not_equal_result = a != b  # True
# print("Inequality (!=):", not_equal_result)

# # Greater than (>)
# greater_than_result = a > b  # True
# print("Greater than (>):", greater_than_result)

# # Greater than or equal to (>=)
# greater_than_or_equal_result = a >= b  # True
# print("Greater than or equal to (>=):", greater_than_or_equal_result)

# # Less than (<)
# less_than_result = a < b  # False
# print("Less than (<):", less_than_result)

# # Less than or equal to (<=)
# less_than_or_equal_result = a <= b  # False
# print("Less than or equal to (<=):", less_than_or_equal_result)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''Bitwise Operation''''''''''''''''''''''''''''''''''''''''''''
# # Bitwise AND (&)
# x = 10  # Binary: 1010
# y = 6   # Binary: 0110

# bitwise_and_result = x & y  # Result: 2 (Binary: 0010)
# print("Bitwise AND (&):", bitwise_and_result)

# # Bitwise OR (|)
# bitwise_or_result = x | y   # Result: 14 (Binary: 1110)
# print("Bitwise OR (|):", bitwise_or_result)

# # Bitwise XOR (^)
# bitwise_xor_result = x ^ y  # Result: 12 (Binary: 1100)
# print("Bitwise XOR (^):", bitwise_xor_result)

# # Bitwise NOT (~)
# bitwise_not_x_result = ~x   # Result: -11 (Binary: -1011 in 2's complement)
# print("Bitwise NOT (~x):", bitwise_not_x_result)

# # Left Shift (<<)
# left_shift_result = x << 1  # Result: 20 (Binary: 10100)
# print("Left Shift (<<):", left_shift_result)

# # Right Shift (>>)
# right_shift_result = x >> 1 # Result: 5 (Binary: 0101)
# print("Right Shift (>>):", right_shift_result)

# # '''''''''''''''''''''''''''''''''''''''''''''Logical Operations''''''''''''''''''''''''''''''''
# # Logical AND (and)
# x = 10
# y = 0
# logical_and_result = x and y  # Result: 0 (False)
# print("Logical AND (and):", logical_and_result)

# # Logical OR (or)
# logical_or_result = x or y   # Result: 10 (True)
# print("Logical OR (or):", logical_or_result)

# # Logical NOT (not)
# logical_not_x_result = not x  # Result: False
# logical_not_y_result = not y  # Result: True
# print("Logical NOT (not) for x:", logical_not_x_result)
# print("Logical NOT (not) for y:", logical_not_y_result)

# # ''''''''''''''''''''''''''''''''Type Conversion'''''''''''''''''''''''''''''''''''''''''''''''
# # Integer to Float
# integer_number = 10
# float_number = float(integer_number)  # Result: 10.0
# print("Integer to Float:", float_number)

# # Integer to String
# integer_number = 10
# string_number = str(integer_number)  # Result: '10'
# print("Integer to String:", string_number)

# # Integer to Boolean
# integer_number = 10
# boolean_value = bool(integer_number)  # Result: True
# print("Integer to Boolean:", boolean_value)

# # Float to Integer
# float_number = 3.14
# integer_number = int(float_number)  # Result: 3 (truncated towards zero)
# print("Float to Integer:", integer_number)

# # String to Integer
# string_number = "10"
# integer_number = int(string_number)  # Result: 10
# print("String to Integer:", integer_number)

# # Boolean to Integer
# boolean_value = True
# integer_number = int(boolean_value)  # Result: 1
# print("Boolean to Integer:", integer_number)

# # '''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# a = 42

# # Built-in Methods
# print("Value:", a)
# print("Bit Length:", a.bit_length())
# print("Conjugate:", a.conjugate())
# print("Denominator:", a.denominator)
# print("From Bytes:", int.from_bytes(a.to_bytes(2, 'big')))
# print("Numerator:", a.numerator)
# print("Real:", a.real)
# print("To Bytes:", a.to_bytes(2, 'big'))

# # Mathematical Operations
# print("Add 10:", a.__add__(10))
# print("Subtract 5:", a.__sub__(5))
# print("Multiply by 2:", a.__mul__(2))
# print("True Divide by 3:", a.__truediv__(3))
# print("Floor Divide by 4:", a.__floordiv__(4))
# print("Modulo 7:", a.__mod__(7))
# print("Power of 3:", a.__pow__(3))
# print("Negative:", a.__neg__())
# print("Positive:", a.__pos__())
# print("Absolute Value:", a.__abs__())

# # Comparison Operations
# print("Equal to 42?", a.__eq__(42))
# print("Not Equal to 50?", a.__ne__(50))
# print("Less than 60?", a.__lt__(60))
# print("Less than or Equal to 30?", a.__le__(30))
# print("Greater than 20?", a.__gt__(20))
# print("Greater than or Equal to 50?", a.__ge__(50))

# # String Representations
# print("String:", a.__str__())
# print("Representation:", a.__repr__())
# print("Hash Value:", a.__hash__())
# print("Boolean Value:", a.__bool__())
 
# ***********************************************************Properties****************************************************************
# # ''''''''''''''''''''''''''''1. int.bit_length()'''''''''''''''''''''''''''
# num = 10 # 1010
# bit_length = num.bit_length()
# print(bit_length)  # Output: 4

# negative_num = -5 
# bit_length_negative = negative_num.bit_length()
# print(bit_length_negative)  # Output: 3

# # ''''''''''''''''''''''''''''''2. int.conjugate()''''''''''''''''''''''''''''''
# real_num = 5
# conjugate_real = real_num.conjugate()
# print(conjugate_real)  # Output: 5

# complex_num = 3 + 2j
# conjugate_complex = complex_num.conjugate()
# print(conjugate_complex)  # Output: 3 - 2j

# # ''''''''''''''''''''''''''''3. int.denominator '''''''''''''''''''''''''''''''''
# import fractions
# num = 10
# print(num.denominator)  # Output: 1

# fraction_num = fractions.Fraction(3, 5)
# print(fraction_num.denominator)  # Output: 5

# # ''''''''''''''''''''''''''''''4. int.real''''''''''''''''''''''''''''''''''
# num = 5
# print(num.real)  # Output: 5.0

# complex_num = 3 + 4j
# print(complex_num.real)  # Output: 3.0

# # ''''''''''''''''''''''''''''5. int.img'''''''''''''''''''''''''''''''''
# num = 10  # Integer
# print(num.imag)
# complex_num = complex(num)  # Convert to complex number


# print(complex_num.imag)  # Output: 0

# complex_num = complex(3, 4)  # Complex number with real and imaginary parts
# print(complex_num.imag)  # Output: 4

# # ''''''''''''''''''''''int.bit_count()'''''''''''''''''''''''''
# num=10
# bit_count_1=num.bit_count()
# print(bit_count_1)
# bit_count_2=num.bit_count
# print(bit_count_2())
# # '''''''''''''''''''''''''''int.from_bytes()'''''''''''''''''''''
# # Example 1: Converting bytes to an integer
# bytes_seq = b'\x00\x00\x00\x0A'
# integer = int.from_bytes(bytes_seq, byteorder='big')
# print(integer)  # Output: 10

# # Example 2: Converting bytes to a signed integer
# bytes_seq = b'\xFF\xFF\xFF\xFF'
# integer = int.from_bytes(bytes_seq, byteorder='big', signed=True)
# print(integer)  # Output: -1

# bytes_array = b'\xFF\x00\x00\x0F'  # 4 bytes representing the value -16776982
# integer = int.from_bytes(bytes_array, byteorder='little', signed=True)
# print(integer)  # Output: -16776982

# # '''''''''''''''''''''''int.to_bytes()''''''''''''''''''''''''''''''''''
# integer = 15
# bytes_array = integer.to_bytes(length=4, byteorder='big')
# print(bytes_array)  # Output: b'\x00\x00\x00\x0f
# bytes_array2 = integer.to_bytes(length=4, byteorder='little')
# print(bytes_array2) # Output: b'\x0f\x00\x00\x00'


# integer = -16776982
# bytes_array = integer.to_bytes(length=4, byteorder='big', signed=True)
# print(bytes_array)  # Output: b'\xff\x00\x00\xea'

# ''''''''''''''''''''''''''''''int.__abs()__
# num = -10
# # abs_value = num.__abs__ # return object refrence
# abs_value = num.__abs__()
# print(abs_value)  # Output: 10

# # Alternatively, you can use the abs() function directly:
# abs_value = abs(num)
# print(abs_value)  # Output: 10

# # ''''''''''''''''''''''''''''''
# from functools import total_ordering

# @total_ordering
# class MyInt(int):
#     def __new__(cls, value):
#         return super().__new__(cls, value)

#     def __abs__(self):
#         if self < 0:
#             return -self
#         return self

# # Example usage:
# num1 = MyInt(-10)
# num2 = MyInt(20)

# abs_num1 = abs(num1)
# print(abs_num1)  # Output: 10

# abs_num2 = abs(num2)
# print(abs_num2)  # Output: 20

# print(abs_num1 < abs_num2)  # Output: True

# # ''''''''''''''''''''''''''''''''''''''
# # Example 1: Compute the absolute difference between two integers
# a = 5
# b = -8

# abs_diff = abs(a - b)
# print(abs_diff)  # Output: 13

# # Example 2: Find the maximum absolute difference in a list of integers
# nums = [1, -3, 6, -9, 4, -2]

# max_abs_diff = max(abs(num1 - num2) for num1 in nums for num2 in nums)
# print(max_abs_diff)  # Output: 15
# # '''''''''''''''''''''''''''''''''''''''''''''''
# def absolute_value(num):
#     mask = num >> (num.bit_length() - 1)  # Create a mask to get the sign bit (0 for positive, -1 for negative)
#     return (num + mask) ^ mask  # XOR the number with the mask to flip the sign bit for negative numbers

# # Example usage:
# num = -110
# abs_value = absolute_value(num)
# print(abs_value)  # Output: 10

# # ''''''''''''''''''''''''''''''''''''''''''''''
# # Given an array of integers, find the sum of absolute differences between adjacent elements.
# # For example, for the array [2, -5, 8, 0], the result would be |2-(-5)| + |(-5)-8| + |8-0| = 17.

# def sum_of_absolute_differences(arr):
#     total_sum = 0
#     for i in range(1, len(arr)):
#         difference = abs(arr[i] - arr[i-1])  # Use abs() to get the absolute difference
#         total_sum += difference
#     return total_sum

# # Example usage:
# array = [2, -5, 8, 0]
# result = sum_of_absolute_differences(array)
# print(result)  # Output: 17

# # '''''''''''''''''''''''''''''''''''''''''''''''custom abs'''''''''''''''''''
# # Custom implementation of int.__abs__() method
# def custom_abs(num):
#     return num if num >= 0 else num.__neg__()

# # Example usage in competitive programming
# num1 = -10
# num2 = 15

# # Using built-in abs() function
# abs_value_1 = abs(num1)
# abs_value_2 = abs(num2)

# # Using custom_abs() method
# abs_value_1_custom = custom_abs(num1)
# abs_value_2_custom = custom_abs(num2)

# print(abs_value_1)  # Output: 10
# print(abs_value_2)  # Output: 15
# print(abs_value_1_custom)  # Output: 10
# print(abs_value_2_custom)  # Output: 15
# # ''''''''''''''''''''''''''''''''2.int.__add__(other)''''''''''''''''''''''''''
# num1 = 10
# num2 = 20

# # Using the '+' operator to add two integers
# result = num1 + num2
# print(result)  # Output: 30

# # Equivalent to the above code using the __add__() method directly
# result_method = num1.__add__(num2)
# print(result_method)  # Output: 30
# # ''''''''''''''''''''''''''''''''''''''
# class MyInt:
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         if isinstance(other, MyInt):
#             return MyInt(self.value + other.value)
#         elif isinstance(other, int):
#             return MyInt(self.value + other)
#         else:
#             raise TypeError("Unsupported operand type: {}".format(type(other)))

# # Example usage:
# a = MyInt(5)
# b = MyInt(10)
# c = a + b
# print(c.value)  # Output: 15

# d = a + 7
# print(d.value)  # Output: 12
# # '''''''''''''''''''''''''''''''''''''''''''''
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         else:
#             raise ValueError("Unsupported operand type for +")

# # Example usage:
# point1 = Point(1, 2)
# point2 = Point(3, 4)

# # Adding two Point objects using the '+' operator
# result = point1 + point2
# print(result.x, result.y)  # Output: 4 6

# # '''''''''''''''''''''''''''''''''''''''''''''''Integer Built-in-Function''''''''''''''''''''''''
# '''abs(x): Returns the absolute value of x.
# divmod(a, b): Returns a tuple containing the quotient and remainder of the division of a by b.
# pow(x, y, z=None): Returns x to the power of y, modulo z (if provided).
# round(number[, ndigits]): Rounds a number to the nearest integer or to the specified number of decimal places (ndigits).
# bin(x): Converts an integer x to a binary string prefixed with '0b'.
# hex(x): Converts an integer x to a lowercase hexadecimal string prefixed with '0x'.
# oct(x): Converts an integer x to an octal string prefixed with '0o'.
# int(x): Converts x to an integer. If x is not specified, it returns 0.'''

# num = -10

# # Absolute value
# abs_value = abs(num)
# print(abs_value)  # Output: 10

# # Divmod
# quotient, remainder = divmod(num, 3)
# print(quotient, remainder)  # Output: (-4, 2)

# # Power
# result = pow(2, 3)
# print(result)  # Output: 8

# # Rounding
# rounded = round(3.14159, 2)
# print(rounded)  # Output: 3.14

# # Conversion to binary, hexadecimal, and octal strings
# binary_str = bin(num)
# hex_str = hex(num)
# octal_str = oct(num)
# print(binary_str, hex_str, octal_str)  # Output: '-0b1010' '-0xa' '-0o12'

# # Integer conversion
# # int_num = int('1010',2)
# int_num = int('14563',8)
# print(int_num)  # Output: 3

# # ''''''''''''''''''''''''''''''''''int.__and__(other)'''''''''''''''''
# num=9
# bitwise_and=num.__and__(6)
# bitwise_and_2=num & 6
# print(bitwise_and," ",bitwise_and_2)

# num=1
# # print(num.__bool__(True))
# print(num.__sub__(8))

# # ''''''''''''''''''''''''''''''''''''''''''''
# num=10
# print(num.__getstate__())
# print(num.__float__())

# l1=[1,2,3,4]

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''''1.Integer Declaration and Assignment'''''''''''''
# # Direct Assignment
# x = 10

# #  Assigning the Value of Another Variable:
# a = 10
# b = a

# # Using assignment in loop
# # sum = 0 # Don't assign to builtin variable `sum
# sum_1 = 0
# for i in range(1, 10):
#     sum_1+=i
    
# # Using Tuple Unpacking
# x, y = 10, 20
# print(x, y)

# value = (1, 2, 3)
# a, b, c = value
# print(f'a = {a}, b = {b}, c = {c}')
# value = [10, 20, 30]
# a, b, c = value
# print(f'a = {a}, b = {b}, c = {c}')

# # Multiple Assignment in a single line
# x = y = z  = 10
# print(x, y, z)

# # Using Assignment with Augmented Operators
# # Before
# other_value = 33
# number = 42
# number += other_value
 
# #  After
# other_value = 33
# number = 42 + other_value

# # Assigning a negative integer
# negative_num = -10

# # #  Assigning Integer from user input
# # user_input = int(input("Enter a number:\n"))
# # print(user_input)

# # Using Binary, Octal and Hexadecimal Notations
# binary_num = 0b1010 # Binary literal (10 in decimal)
# octal_num = 0o17    # Octal literal (15 in decimal)
# hex_num = 0xA       # Hexadecimal literal (10 in decimal)
# print(f"Binary number: {binary_num}, octal number {octal_num}, hexadecimal number: {hex_num}")

# # Assignment with function return
# def fun():
#     return "Hello, world!"
# string = fun()
# print(f"string: {string}")

# # Assignment with Conditional Operators
# value = 50
# x = value if value > 0 else 0
# x = max(value, 0)
# print(f'x = {x}')

# # # Assignment with file reading 
# # with open('data.txt', 'r') as file:
# #     first_int = int(file.readline())
# # print(f'first_int = {first_int}')
    
# # Assignment with Generator Expression
# squares = [x**2 for x in range(10)]
# print(f'squares = {squares}')

# # Assignment with Dictionary Access
# my_dict = {'name': 'Ranjit', 'age': 22}
# name = my_dict.get('name','0')
# age = my_dict.get('age','1')
# print(f'name = {name}')
# print(f'age = {age}')

# student_scores = {"Alice": 85, "Bob": 90, "Charlie": 75}
# bob_score = student_scores["Bob"]
# print(f'bob_score = {bob_score}')

# # Assignment with Type Casting
# x = int('10')
# print(f'x = {x}')

# # Assignment with Bitwise Operations
# x = 0b1010 # Bitwise Literal(10 Decimal number)
# y = x << 2 # Left shift operation
# print(f'x = {x}') # 10 
# print(f'y = {y}') # 40

# #  Assignment using Unary Operators
# a = ~10
# print(f'a = {a}')

# # ''''''''''''''''''''''''''''''''''''''''''''''Arithmetic Operations''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Addition
# result_addition = 5 + 3
# print("Addition:", result_addition)  # Output: 8

# # Subtraction
# result_subtraction = 10 - 4
# print("Subtraction:", result_subtraction)  # Output: 6

# # Multiplication
# result_multiplication = 7 * 2
# print("Multiplication:", result_multiplication)  # Output: 14

# # Division
# result_division = 15 / 3
# print("Division:", result_division)  # Output: 5.0

# # Integer Division (Quotient)
# result_integer_division = 15 // 4 
# print("Integer Division (Quotient):", result_integer_division)  # Output: 3
# result_integer_division, result_modulus = divmod(15, 4)
# print(f'Integer Division (Quotient) = {result_division}, Remainder = {result_modulus}')  # Output: 3
# l1 = [(10, 6), (12, 7), (12, 8), (13, 9)]
# for t in l1:
#     q, r = divmod(*t)
#     print(f'q = {q}, r = {r}\n')
    
# # Before
# result = int(42 / 10)
# print(f'result = {result}') # Output: 4
# # After 
# result = 42 // 10
# print(f'result = {result}') # Output: 4

# # Before
# result = 42 // 10
# remainder = 42 % 10
# print(f'result = {result}, remainder = {remainder}') # Output: result = 4, remainder = 2

# # After
# result, remainder = divmod(42, 10)
# print(f'result = {result}, remainder = {remainder}')

# # Modulus (Remainder)
# result_modulus = 15 % 4
# print("Modulus (Remainder):", result_modulus)  # Output: 3

# # Exponentiation
# result_exponentiation = 2 ** 4
# print("Exponentiation:", result_exponentiation)  # Output: 16

# # Floor Division (Quotient as Integer)
# result_floor_division = 15 // 4
# print("Floor Division (Quotient as Integer):", result_floor_division)  # Output: 3

# # Absolute Value
# result_absolute = abs(-7)
# print("Absolute Value:", result_absolute)  # Output: 7

# # Negation
# result_negation = -7
# print("Negation:", result_negation)  # Output: -7

# # Increment
# x = 5
# x += 1
# print("Increment:", x)  # Output: 6

# # Decrement
# y = 10
# y -= 1
# print("Decrement:", y)  # Output: 9

# # sum of integers
# integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_of_integers = sum(integer_list)
# print(f'sum of integers = {sum_of_integers}')

# # # Products of integers
# # import numpy as np
# # product_of_integers = np.prod(integer_list)
# # print(f'sum of products = {product_of_integers}') # Output: 

# # Minimum and Maximum of integers list
# min_integer = min(integer_list) # Output: 1
# max_integer = max(integer_list) # Output: 10
# print(f'minimum integer = {min_integer}, max_integer = {max_integer}')

# # '''''''''''''''''''''''''''''''''''''''''''''''Comparision Operation with integers''''''''''''''''''''''''''''''''''''''''
# # Define two integers
# x = 5
# y = 10

# # Equality
# result_equal = x == y
# print("Equality:", result_equal)  # Output: False

# # Inequality
# result_inequality = x != y
# print("Inequality:", result_inequality)  # Output: True

# # Greater Than
# result_greater_than = x > y
# print("Greater Than:", result_greater_than)  # Output: False

# # Less Than
# result_less_than = x < y
# print("Less Than:", result_less_than)  # Output: True

# # Greater Than or Equal To
# result_greater_equal = x >= y
# print("Greater Than or Equal To:", result_greater_equal)  # Output: False

# # Less Than or Equal To
# result_less_equal = x <= y
# print("Less Than or Equal To:", result_less_equal)  # Output: True

# # Chained omparision
# x, y, z = 5, 10, 5
# result_chained = x = z < y
# print(f'Chained Comparision: {result_chained}') # Output: True

# # Membership Test
# integer_list = [1, 2, 3, 4, 5]
# result_membership = 3 in integer_list
# print(f'Membership Test: {result_membership}') # Output: True

# # Non-membership Test
# result_non_membership = 0 not in integer_list
# print(f'Non-Membership Test: {result_non_membership}') # Output: True

# # '''''''''''''''''''''''''''''''''''''''''''Logical Operators'''''''''''''''''''''''''''''''''''''''''''''
# # Declaring integers
# x = 5
# y = 10

# # AND
# result_and = (x < 10) and (y > 5)
# print("AND:", result_and)  # Output: True

# # OR
# result_or = (x < 10) or (y < 5)
# print("OR:", result_or)  # Output: True

# # NOT
# result_not_x = not (x < 10)
# print("NOT x:", result_not_x)  # Output: False

# result_not_y = not (y < 5)
# print("NOT y:", result_not_y)  # Output: True

# # Before
# p = True
# if not not p:
#     a = 1
# if not a is p:
#     a  = 1
# if not (a == 1 and p == 2):
#     a = 1
# # After
# if p:
#     a == 1
# if a is not p:
#     a == 1
# if (a != 1 or p != 2):
#     a == 1

# # '''''''''''''''''''''''''''''''''''''''''''''Bitwise operator''''''''''''''''''''''''''''''''''''
# # Bitwise AND
# x = 5
# y = 3
# result_and = x & y
# print("Bitwise AND:", result_and)  # Output: 1

# # Bitwise OR
# result_or = x | y
# print("Bitwise OR:", result_or)  # Output: 7

# # Bitwise XOR
# result_xor = x ^ y
# print("Bitwise XOR:", result_xor)  # Output: 6

# # Bitwise NOT
# result_not_x = ~x
# print("Bitwise NOT x:", result_not_x)  # Output: -6

# result_not_y = ~y
# print("Bitwise NOT y:", result_not_y)  # Output: -4

# # Bitwise Left Shift
# result_left_shift = x << 1
# print("Bitwise Left Shift:", result_left_shift)  # Output: 10

# # Bitwise Right Shift
# result_right_shift = x >> 1
# print("Bitwise Right Shift:", result_right_shift)  # Output: 2

# # '''''''''''''''''''''''''''''''''''''''Identity Operator'''''''''''''''''''''''''
# # Declaring Integer
# a, b, c = 5, 5, 10
# x, y, z = '5', '5', '10'

# # Checking identity with 'is'
# result_identity_1 = a is b
# print(f'Identity test (a is b); {result_identity_1}')

# result_identity_2 = a is c
# print(f'identity test (a is c); {result_identity_2}')

# print(f'(a is x): {a is x} and (a == x): {a == x}')

# # Checking non-identity with 'is not'
# result_non_identity_1 = (a is not b)
# print("Non-Identity Test (a is not b):", result_non_identity_1)  # Output: False

# result_non_identity_2 = (a is not c)
# print("Non-Identity Test (a is not c):", result_non_identity_2)  # Output: True

# # ''''''''''''''''''''''''''''''''''Exponentiation with Integers''''''''''''''''''''''
# # Declaring integers
# x = 2
# y = 3

# # Exponentiation
# result_exponentiation = x ** y
# print("Exponentiation:", result_exponentiation)  # Output: 8

# # Another example
# base = 4
# exponent = 2
# result = base ** exponent
# print("Result:", result)  # Output: 16

# # Exponentiation with negative exponent
# negative_exponent = -2
# result_negative_exponent = base ** negative_exponent
# print("Exponentiation with negative exponent:", result_negative_exponent)  # Output: 0.0625 (1/16)

# # Using the pow() function
# result_pow_fun = pow(2, 4)
# print(f'Exponentiation with pow(): {result_pow_fun}')

# # Using the math.pow() function
# import math
# result_pow_fun_2 = math.pow(2, 4)
# print(f'Exponentiation with math.pow(): {result_pow_fun_2}')

# # '''''''Modular Exponentiation'''''''''''''
# # Define base, exponent, and modulus
# base = 2
# exponent = 10
# modulus = 1000

# # Modular Exponentiation using iterative method
# def mod_exp_iterative(base, exponent, modulus):
#     result = 1
#     base %= modulus
#     while exponent > 0:
#         if exponent % 2 == 1:
#             result = (result * base) % modulus
#         exponent //= 2
#         base = (base * base) % modulus
#     return result

# result_mod_exp_iterative = mod_exp_iterative(base, exponent, modulus)
# print("Modular Exponentiation (Iterative):", result_mod_exp_iterative)  # Output: 24

# # Modular Exponentiation using built-in pow() function
# result_mod_exp_builtin = pow(base, exponent, modulus)
# print("Modular Exponentiation (Built-in pow()):", result_mod_exp_builtin)  # Output: 24
 
# #  '''''''''''''''''''''''''''''''''Integer Overflow and Underflow''''''''''''''''''''''''''''''''''
# ''''''''''''''Integer Overflow 
# import sys
# max_int = sys.maxsize
# print(f'Maximum integer value: {max_int}') # Output: 9223372036854775807
# # Incrementing max_int(Overflow)
# Overflow_value = max_int + 1
# print(f'Overflow value: {Overflow_value}') # Output: 9223372036854775808

# # ''''''''''''''''Integer Underflow
# import sys
# # Minimum integer value
# min_int = -sys.maxsize - 1
# print(f'Minimum integer value: {min_int}') # Output: -9223372036854775808
# Underflow_value = min_int - 1
# print(f'Underflow value: {Underflow_value}') # Output: -9223372036854775809

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # '''''''''''''''''''''''''''''''''''''''''''Integer Type Conversion'''''''''''''''''''''''''''''''''''''''
# # ''''''''Integer to Float Conversion''''''''''
# integer_value = 10
# float_value = float(integer_value) # Integer to Float Conversion using float() constructor
# print(f'Integer to Float Conversion: {float_value} and type of float_value: {type(float_value)}') # Output: 10.0 , <class 'float'>

# # Integer to  String Conversion
# integer_value = 123
# string_value = str(integer_value) # Integer to String Conversion using str() constructor
# print(f'Integer to String Conversion: {string_value} and type of string_value: {type(string_value)}') # Output: 123, <class 'string_value>

# # Float to integer conversion
# float_value = 3.14
# int_value = int(float_value) # Float to integer Conversion using int() constructor
# print(f'Float to Integer Conversion: {int_value} and type of int_value: {type(int_value)}') # Output: 3, <class 'int'>

# # String to Integer Value
# string_value = '123' # String to Integer Conversion using int() constructor
# int_value = int(string_value)
# print(f'String to Integer Value: {string_value} and type of int_value: {type(int_value)}') # Output: 123, <class 'int'>

# # Rounding Float to Nearest Integer
# float_value = 3.14
# rounded_integer = round(float_value) # Rounding Float to Nearest Integer using round() constructor
# print(f'Rounding Float to Nearest Integer: {rounded_integer} and type of rounded_integer: {type(rounded_integer)}') # Output: 3, <class 'int'>

# # Binary to Integer Conversion
# binary_value = '1010'
# int_value = int(binary_value, 2) # Binary to Integer using int() constructor with base 2
# print(f'Binary to Integer Conversion: {int_value} and type of int_value: {type(int_value)}') # Output: 10, <class 'int'>

# # Octal to Integer Conversion# Octal string
# octal_string = '17'

# # Using int() function with base 8
# integer_from_octal = int(octal_string, 8)
# print("Converted Integer from Octal:", integer_from_octal)  # Output: 15

# # Hexadecimal to Intgere Conversion
# hex_value = '1A'
# int_value = int(hex_value, 16) # Hexadecimal to Integer using int() constructor with base 16
# print(f'Hexadecimal to Intgere Conversion: {int_value} and type of int_value: {type(int_value)}') # Output 26, <class 'int'> 

# # Boolean to Integer Conversion
# bool_value = True
# int_value = int(bool_value) # Boolean to Integer Conversion using int() constructor
# print(f'Boolean to Integer Conversion: {int_value} and type of int_value: {type(int_value)}') # Output 1, <class 'int'>  

# # From Other Numeeric Type to Integer Conversion
# # Using int() with other numeric types
# long_num = 12345678901234567890
# # long_to_int = int(long_num)
# long_to_int = long_num
# print("Converted Integer from Long:", long_to_int)  # Output: 12345678901234567890

# # Handling Errors
# invalid_conversion = '123.45'
# try:
#     invalid_int_value = int(invalid_conversion) 
# except ValueError:
#     print('Invalid conversion from string to integer')
# # '''''''''''''''''''''''''''''''' 
# # Implicit Integer Type Conversion: 
# int_value = 4
# float_value = 2.5 + int_value # Implicit Conversion: integer to float
# print(f'Implicit Integer Type Conversion: {float_value} and type of float_value: {type(float_value)}') # Output: 6.5, <class 'float'>

 
# result = 10 / 2 # Implicit Conversion: float to integer
# print(f'Explict Conversion: {result} and type of result: {type(result)}') # Output: 5.0, <class 'float'>

# # Explict Integer Type Conversion:
# # Explicit conversion from string to integer
# string_value = "123"
# integer_value = int(string_value)
# print("Explicit Conversion from String to Integer:", integer_value)  # Output: 123

# # Explicit conversion from float to integer
# float_value = 3.7
# integer_value = int(float_value)
# print("Explicit Conversion from Float to Integer:", integer_value)  # Output: 3

# # Explicit conversion from integer to string
# integer_value = 456
# string_value = str(integer_value)
# print("Explicit Conversion from Integer to String:", string_value)  # Output: "456"

# '''''''''''''''''''Integer Type Conversion in Data Processing and Analysis
"""Read an integer from File"""
# # 1.Data Input From a File
# with open('data.txt', 'r') as file:
#     lines = file.readlines()
#     integers = [int(line.strip()) for line in lines]
# print(f'Integers from file: {integers}')
"""Read an integer from CSV file"""
# # 2. Data Input From CSV File
# import csv
# integers = []
# with open('data.csv', 'r') as file:
#     readers = csv.reader(file)
#     for row in file:
#         integers.append(row[0])
# print(f'Integers from CSV File: {integers}')

"""Read an Integer from User Input."""
# # 3.Data Input from User Input
# integer_input = input("Enter an integer: ")
# integer_value  = int(integer_input)
# print(f'Integer value from User Input: {integer_value}') 

# Data Conversion in Data Processing
# string_data = ['1', '2', '3', '4', '5']
# integer_data = [int(x) for x in string_data]
# print(f'integer data from Data Processing: {integer_data}')

"""Write data to a file"""
# # Data Output to a File
# integers = [1, 2, 3, 4, 5]
# with open('data.txt', 'w') as file:
#     for integer in integers:
#         file.write(str(integer) + '\n')

# '''''''''''''''''''''''''''''Error Handling and Exception Management in Integer Type Conversion
# 1.Handling Value Error











