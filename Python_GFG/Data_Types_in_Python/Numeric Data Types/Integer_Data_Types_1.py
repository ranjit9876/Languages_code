# # ''''''''''''''''''''''''''''''''''''''''''''''''Integer Conversion'''''''''''''''''''''''''''''''''''''''''''''
# # Integer to Binary
# def int_to_binary(num):
#     return bin(num)

# # Integer to Octal
# def int_to_octal(num):
#     return oct(num)

# # Integer to Hexadecimal
# def int_to_hexadecimal(num):
#     return hex(num)

# # Binary to Integer
# def binary_to_int(binary_str):
#     return int(binary_str, 2)

# # Octal to Integer
# def octal_to_int(octal_str):
#     return int(octal_str, 8)

# # Hexadecimal to Integer
# def hexadecimal_to_int(hexadecimal_str):
#     return int(hexadecimal_str, 16)

# # Integer to String
# def int_to_string(num):
#     return str(num)

# # String to Integer
# def string_to_int(string_num):
#     return int(string_num)

# # Example usage
# if __name__ == "__main__":
#     num = 42

#     # Integer to Binary
#     binary_num = int_to_binary(num)
#     print(f"Integer {num} to Binary: {binary_num}")

#     # Integer to Octal
#     octal_num = int_to_octal(num)
#     print(f"Integer {num} to Octal: {octal_num}")

#     # Integer to Hexadecimal
#     hex_num = int_to_hexadecimal(num)
#     print(f"Integer {num} to Hexadecimal: {hex_num}")

#     # Binary to Integer
#     binary_str = "101010"
#     int_from_binary = binary_to_int(binary_str)
#     print(f"Binary {binary_str} to Integer: {int_from_binary}")

#     # Octal to Integer
#     octal_str = "52"
#     int_from_octal = octal_to_int(octal_str)
#     print(f"Octal {octal_str} to Integer: {int_from_octal}")

#     # Hexadecimal to Integer
#     hex_str = "2a"
#     int_from_hex = hexadecimal_to_int(hex_str)
#     print(f"Hexadecimal {hex_str} to Integer: {int_from_hex}")

#     # Integer to String
#     num_str = int_to_string(num)
#     print(f"Integer {num} to String: {num_str}")

#     # String to Integer
#     str_num = "123"
#     int_from_str = string_to_int(str_num)
#     print(f"String {str_num} to Integer: {int_from_str}")

# # Error Handling
# try:
#     invalid_num = int("invalid")  # Trying to convert an invalid string to int
# except ValueError as e:
#     print(f"Error: {e}")

# # Integer conversions for advanced topics
# float_num = 3.14159
# int_from_float_truncate = int(float_num)  # Truncates the decimal part
# print(f"Integer from Float (Truncate): {int_from_float_truncate}")

# complex_num = 2 + 3j
# int_from_complex = int(complex_num.real)  # Takes the real part
# print(f"Integer from Complex: {int_from_complex}")
# ''''''''''''''''''''''
# # Conversion to and from Roman numerals
# roman_numeral = 'XLII'
# int_from_roman = 0

# roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# for i in range(len(roman_numeral)):
#     if (i > 0 and roman_values[roman_numeral[i]] > roman_values[roman_numeral[i - 1]]):
#         int_from_roman += roman_values[roman_numeral[i]] - 2 * roman_values[roman_numeral[i - 1]]
#     else:
#         int_from_roman += roman_values[roman_numeral[i]]
# print(f'Integer from Roman Numeral: {int_from_roman}')        
# '''''''''''''''''''''''''
# # Integer to Roman Numeral
# def int_to_roman(n):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#         ]
#     syms = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#         ]
#     roman_numeral = ''
#     i = 0
#     while n > 0:
#         for _ in range(n // val[i]):
#             roman_numeral += syms[i]
#             n -= val[i]
#         i += 1
#     return roman_numeral

# num = 42
# roman_numeral_from_int = int_to_roman(num)
# print(f"Roman Numeral from Integer: {roman_numeral_from_int}")

# # '''''''''''''''''''''''''''''''''''
# # Other base to decimal conversion without built-in functions
# def base_to_decimal(num_str, base):
#     decimal_num = 0
#     power = 0
#     for digit in reversed(num_str):
#         decimal_num += int(digit) * (base ** power)
#         power += 1
#     return decimal_num

# # Decimal to other base conversion without built-in functions
# def decimal_to_base(num, base):
#     result = ""
#     while num > 0:
#         digit = num % base
#         result = str(digit) + result
#         num //= base
#     return result

# '''''''''''''''''
# # Integer to ASCII character and vice versa
# ascii_num = 65
# char_from_int = chr(ascii_num)
# int_from_char = ord(char_from_int)
# print(f"Character from Integer: {char_from_int}")
# print(f"Integer from Character: {int_from_char}")

# # ''''''''''''''''''
# # Typecasting from list of digits to int
# digits = [1, 2, 3, 4, 5]
# int_from_digits = int(''.join((map(str, digits))))
# print(f"Typecasting from List of Digits to Integer: {int_from_digits}")

# ''''''''''''''''''''''
# # Typecasting from int to list of digits
# num = 9876
# int_to_digits = list((map(int, str(num))))
# print(f"Typecasting from Integer to List of Digits: {int_to_digits}")

# # '''''''''''''''''''''''''''
# # Advanced Integer Conversions in Python

# # Function to convert a decimal integer to any base
# def decimal_to_base(num, base):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # For bases up to 36
#     if num == 0:
#         return "0"
#     result = ""
#     while num > 0:
#         remainder = num % base
#         result = digits[remainder] + result
#         num //= base
#     return result

# # Function to convert an integer from any base to decimal
# def base_to_decimal(num_str, base):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # For bases up to 36
#     result = 0
#     power = 0
#     for digit in reversed(num_str):
#         if digit in digits:
#             value = digits.index(digit)
#             result += value * (base ** power)
#         else:
#             raise ValueError("Invalid digit in input string")
#         power += 1
#     return result

# # Convert a decimal integer to binary, octal, and hexadecimal
# num = 255
# binary_num = decimal_to_base(num, 2)
# octal_num = decimal_to_base(num, 8)
# hexadecimal_num = decimal_to_base(num, 16)

# print(f"Decimal: {num}")
# print(f"Binary: {binary_num}")
# print(f"Octal: {octal_num}")
# print(f"Hexadecimal: {hexadecimal_num}")

# # Convert binary, octal, and hexadecimal to decimal
# decimal_from_binary = base_to_decimal(binary_num, 2)
# decimal_from_octal = base_to_decimal(octal_num, 8)
# decimal_from_hexadecimal = base_to_decimal(hexadecimal_num, 16)

# print(f"Decimal from Binary: {decimal_from_binary}")
# print(f"Decimal from Octal: {decimal_from_octal}")
# print(f"Decimal from Hexadecimal: {decimal_from_hexadecimal}")

# # Advanced Typecasting: Floating-point to Integer
# float_num = 3.14
# int_from_float = int(float_num)  # This truncates the decimal part

# print(f"Typecasting from Float to Integer: {int_from_float}")

# # Advanced Typecasting: String to Integer with Error Handling
# str_num = "123abc"
# try:
#     int_from_str = int(str_num)
#     print(f"String to Integer: {int_from_str}")
# except ValueError as e:
#     print(f"Error: {e}")

# # Advanced Typecasting: Boolean to Integer
# bool_val = True
# int_from_bool = int(bool_val)

# print(f"Typecasting from Boolean to Integer: {int_from_bool}")

# # '''''''''''''''''''''''''''''
# # Integer Typecasting in Python

# # 1. Integer to Float
# int_to_float = float(42)

# # 2. Integer to String
# int_to_str = str(42)

# # 3. Float to Integer (Truncates decimal part)
# float_to_int = int(3.14)

# # 4. Float to String
# float_to_str = str(3.14)

# # 5. String to Integer
# str_to_int = int("42")

# # 6. String to Float
# str_to_float = float("3.14")

# # 7. Boolean to Integer (True becomes 1, False becomes 0)
# bool_to_int_true = int(True)
# bool_to_int_false = int(False)

# # 8. List to Integer (Invalid)
# list_to_int = None
# try:
#     list_to_int = int([1, 2, 3])
# except TypeError as e:
#     print(f"Error: {e}")

# # 9. Tuple to Integer (Invalid)
# tuple_to_int = None
# try:
#     tuple_to_int = int((1, 2, 3))
# except TypeError as e:
#     print(f"Error: {e}")

# # 10. Set to Integer (Invalid)
# set_to_int = None
# try:
#     set_to_int = int({1, 2, 3})
# except TypeError as e:
#     print(f"Error: {e}")

# # 11. Dictionary to Integer (Invalid)
# dict_to_int = None
# try:
#     dict_to_int = int({"a": 1, "b": 2})
# except TypeError as e:
#     print(f"Error: {e}")

# # 12. Character to Integer (Invalid)
# char_to_int = None
# try:
#     char_to_int = int("A")
# except ValueError as e:
#     print(f"Error: {e}")

# # 13. String with Commas to Integer (Invalid)
# comma_str_to_int = None
# try:
#     comma_str_to_int = int("1,000")
# except ValueError as e:
#     print(f"Error: {e}")

# # 14. Binary to Integer
# binary_str = "1010"
# binary_to_int = int(binary_str, 2)

# # 15. Octal to Integer
# octal_str = "52"
# octal_to_int = int(octal_str, 8)

# # 16. Hexadecimal to Integer
# hexadecimal_str = "1A"
# hexadecimal_to_int = int(hexadecimal_str, 16)

# # 17. String with Leading Zeros to Integer (Invalid)
# leading_zeros_str_to_int = None
# try:
#     leading_zeros_str_to_int = int("00123")
# except ValueError as e:
#     print(f"Error: {e}")

# # 18. Negative String to Integer
# negative_str_to_int = int("-42")

# # 19. String with Plus Sign to Integer (Invalid)
# plus_sign_str_to_int = None
# try:
#     plus_sign_str_to_int = int("+42")
# except ValueError as e:
#     print(f"Error: {e}")

# # 20. String with Non-numeric Characters to Integer (Invalid)
# invalid_str_to_int = None
# try:
#     invalid_str_to_int = int("42a")
# except ValueError as e:
#     print(f"Error: {e}")

# # 21. Empty String to Integer (Invalid)
# empty_str_to_int = None
# try:
#     empty_str_to_int = int("")
# except ValueError as e:
#     print(f"Error: {e}")

# # 22. String to Integer with Base (Binary)
# binary_str_base_to_int = int("1010", 2)

# # 23. String to Integer with Base (Octal)
# octal_str_base_to_int = int("52", 8)

# # 24. String to Integer with Base (Hexadecimal)
# hexadecimal_str_base_to_int = int("1A", 16)

# # 25. Binary to Integer with Prefix
# binary_str_prefix_to_int = int("0b1010", 0)

# # 26. Octal to Integer with Prefix
# octal_str_prefix_to_int = int("0o52", 0)

# # 27. Hexadecimal to Integer with Prefix
# hexadecimal_str_prefix_to_int = int("0x1A", 0)

# # 28. String with Underscores to Integer (Python 3.6+)
# underscore_str_to_int = int("1_000_000")

# # 29. String with Non-breaking Space to Integer (Invalid)
# non_breaking_space_str_to_int = None
# try:
#     non_breaking_space_str_to_int = int("1 000")  # Note: This contains a non-breaking space character
# except ValueError as e:
#     print(f"Error: {e}")

# # 30. Complex to Integer (Loses Imaginary Part)
# complex_num = 3 + 4j
# complex_to_int = int(complex_num)

# # 31. Integer to Complex (Imaginary Part Set to 0)
# int_to_complex = complex(42)

# # 32. Typecasting with Explicit Conversion (Unsafe)
# unsafe_int = int("42")

# # 33. Typecasting with Explicit Conversion (Safe with Validation)
# validated_safe_int = None
# try:
#     validated_safe_int = int("42")
# except ValueError as e:
#     print(f"Error: {e}")

# # 34. Typecasting with Multiple Input Values
# input_values = input("Enter two numbers separated by space: ").split()
# if len(input_values) == 2:
#     num1 = int(input_values[0])
#     num2 = int(input_values[1])
#     print(f"Sum: {num1 + num2}")
# else:
#     print("Invalid input format. Please enter two numbers separated by space.")

# # 35. Typecasting with Unit Conversion
# def feet_to_meters(feet):
#     return feet * 0.3048

# feet_distance = 10
# meters_distance = feet_to_meters(feet_distance)

# # 36. Typecasting with Exception Handling for Conversion
# def safe_float_conversion(val):
#     try:
#         return float(val)
#     except (ValueError, TypeError):
#         raise ValueError(f"Invalid float value: {val}")

# try:
#     float_value = safe_float_conversion("3.14")
#     print(f"Parsed Float: {float_value}")
# except ValueError as e:
#     print(f"Error: {e}")

# # 37. Typecasting with Input Validation (Non-Negative Integer)
# def validate_non_negative_int(val, default):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if int_val >= 0:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# non_negative_int1 = validate_non_negative_int("42", 0)
# non_negative_int2 = validate_non_negative_int("-5", 0)
# non_negative_int3 = validate_non_negative_int(None, 0)

# # 38. Typecasting with Input Validation (Positive Integer)
# def validate_positive_int(val, default):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if int_val > 0:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# positive_int1 = validate_positive_int("42", 0)
# positive_int2 = validate_positive_int("0", 0)
# positive_int3 = validate_positive_int("-5", 0)
# positive_int4 = validate_positive_int(None, 0)

# # 39. Typecasting with Input Validation (Custom Range)
# def validate_int_in_range(val, default, min_val, max_val):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if min_val <= int_val <= max_val:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# range_int1 = validate_int_in_range("42", 0, 0, 100)
# range_int2 = validate_int_in_range("200", 0, 0, 100)
# range_int3 = validate_int_in_range("-5", 0, 0, 100)
# range_int4 = validate_int_in_range(None, 0, 0, 100)

# # 40. Typecasting with Customized Output for Validation
# def validate_int_with_output(val, default):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if int_val >= 0:
#             return int_val
#         else:
#             print("Value must be non-negative. Using default.")
#             return default
#     except (ValueError, TypeError):
#         print("Invalid input format. Using default.")
#         return default

# output_int1 = validate_int_with_output("42", 0)
# output_int2 = validate_int_with_output("-5", 0)
# output_int3 = validate_int_with_output(None, 0)

# # 41. Typecasting with Function Composition
# def str_to_positive_int(val, default):
#     return validate_positive_int(val, default)

# def str_to_positive_int_with_output(val, default):
#     return validate_int_with_output(val, default)

# composed_int1 = str_to_positive_int("42", 0)
# composed_int2 = str_to_positive_int_with_output("-5", 0)
# composed_int3 = str_to_positive_int(None, 0)

# # 42. Typecasting with Built-in Functions
# str_to_int1 = int("42")
# str_to_int2 = int("-5")
# str_to_float1 = float("3.14")
# str_to_bool1 = bool("True")
# str_to_bool2 = bool("False")
# str_to_bool3 = bool("Invalid")

# # 43. Typecasting with Floating-Point Precision
# float_to_str_precision = format(3.141592653589793, ".2f")
# float_precision = round(3.141592653589793, 2)

# # 44. Typecasting with Different Bases (Binary, Octal, Hexadecimal)
# binary_str = "1010"
# octal_str = "52"
# hexadecimal_str = "1A"
# binary_to_int = int(binary_str, 2)
# octal_to_int = int(octal_str, 8)
# hexadecimal_to_int = int(hexadecimal_str, 16)

# # 45. Typecasting with Multiple Assignment
# a = b = 42

# # 46. Typecasting with Namedtuples
# from collections import namedtuple
# Point = namedtuple("Point", ["x", "y"])
# point = Point(x=1, y=2)
# point_dict = point._asdict()
# point_tuple = Point(**point_dict)

# # 47. Typecasting with List Comprehension
# string_numbers = ["1", "2", "3"]
# int_numbers = [int(x) for x in string_numbers]

# # 48. Typecasting with a Map Function
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))

# # 49. Typecasting with Lambda Functions
# double = lambda x: x * 2
# result3 = double(5)

# # 50. Typecasting with Conditional Ternary Operator
# x = 42
# y = 30
# max_value = x if x > y else y

# # 51. Typecasting with Complex to Integer (Loses Imaginary Part)
# complex_num = 3 + 4j
# complex_to_int = int(complex_num)

# # 52. Typecasting with Integer to Complex (Imaginary Part Set to 0)
# int_to_complex = complex(42)

# # 53. Typecasting with Type Hints (Python 3.5+)
# def multiply_numbers(x: int, y: int) -> int:
#     return x * y

# result4 = multiply_numbers(5, 6)

# # 54. Typecasting with Zip Function
# list1 = [1, 2, 3]
# list2 = ["a", "b", "c"]
# zipped = list(zip(list1, list2))

# # 55. Typecasting with List Slicing
# str_slice = "Hello, World!"[7:12]

# # 56. Typecasting with List Unpacking
# numbers_list = [1, 2, 3]
# a, b, c = numbers_list

# # 57. Typecasting with Input and Validation (Non-Negative Integer)
# def validate_non_negative_int(val, default):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if int_val >= 0:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# # 58. Typecasting with Input and Validation (Positive Integer)
# def validate_positive_int(val, default):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if int_val > 0:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# # 59. Typecasting with Input and Validation (Custom Range)
# def validate_int_in_range(val, default, min_val, max_val):
#     if val is None:
#         return default
#     try:
#         int_val = int(val)
#         if min_val <= int_val <= max_val:
#             return int_val
#         else:
#             return default
#     except (ValueError, TypeError):
#         return default

# # 60. Typecasting with Input and Validation (Custom Function)
# def validate_input(val, validation_function, default):
#     if val is None:
#         return default
#     try:
#         return validation_function(val, default)
#     except Exception as e:
#         print(f"Validation Error: {e}")
#         return default

# # 61. Typecasting with Input and Validation (Using Custom Functions)
# user_input = input("Enter a positive integer: ")
# validated_int = validate_input(user_input, validate_positive_int, 0)

# # 62. Typecasting with Input and Validation (Using Different Custom Functions)
# user_input2 = input("Enter a number between 10 and 50: ")
# validated_int2 = validate_input(user_input2, validate_int_in_range, 0, 10, 50)

# # 63. Typecasting with Input and Validation (Using a Different Custom Function)
# user_input3 = input("Enter a non-negative integer: ")
# validated_int3 = validate_input(user_input3, validate_non_negative_int, 0)

# # ''''''''''''''''''''''''''''''''''''
# # Numeric Operations in Python
# import math 
# import random
# # Arithmetic Operations
# num1 = 10
# num2 = 5

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# floor_division = num1 // num2
# modulus = num1 % num2
# exponentiation = num1 ** num2

# # Comparison Operations
# greater_than = num1 > num2
# less_than = num1 < num2
# equal_to = num1 == num2
# not_equal_to = num1 != num2
# greater_than_or_equal = num1 >= num2
# less_than_or_equal = num1 <= num2

# # Rounding
# number = 3.14159
# rounded = round(number, 2)
# ceiling = math.ceil(number)
# floor = math.floor(number)

# # Absolute Value
# negative_number = -42
# absolute_value = abs(negative_number)

# # Trigonometric Functions
# angle_degrees = 30
# angle_radians = math.radians(angle_degrees)
# sine = math.sin(angle_radians)
# cosine = math.cos(angle_radians)
# tangent = math.tan(angle_radians)

# # Square Root
# number_to_sqrt = 25
# square_root = math.sqrt(number_to_sqrt)

# # Logarithmic Functions
# logarithm_base_10 = math.log10(100)
# natural_logarithm = math.log(2.71828)  # Approximation of e

# # Constants
# pi = math.pi
# euler_number = math.e

# # Integer Division
# integer_result = 10 // 3

# # Modulus (Remainder)
# remainder = 10 % 3

# # Bitwise Operations
# bitwise_and = 0b1100 & 0b1010
# bitwise_or = 0b1100 | 0b1010
# bitwise_xor = 0b1100 ^ 0b1010
# bitwise_not = ~0b1100
# left_shift = 0b0010 << 2
# right_shift = 0b1100 >> 2

# # Absolute Value of Complex Number
# complex_num = complex(-3, 4)
# abs_complex = abs(complex_num)

# # Complex Number Operations
# complex1 = complex(2, 3)
# complex2 = complex(1, 2)

# complex_addition = complex1 + complex2
# complex_subtraction = complex1 - complex2
# complex_multiplication = complex1 * complex2
# complex_division = complex1 / complex2

# # Random Number Generation
# random_number = random.random()
# random_integer = random.randint(1, 10)
# random_choice = random.choice(['apple', 'banana', 'cherry'])

# # Numeric Operations with Fractions
# import fractions

# fraction1 = fractions.Fraction(1, 3)
# fraction2 = fractions.Fraction(2, 5)

# fraction_addition = fraction1 + fraction2
# fraction_subtraction = fraction1 - fraction2
# fraction_multiplication = fraction1 * fraction2
# fraction_division = fraction1 / fraction2

# # Numeric Operations with Decimals
# from decimal import Decimal

# decimal1 = Decimal('0.1')
# decimal2 = Decimal('0.2')

# decimal_addition = decimal1 + decimal2
# decimal_subtraction = decimal1 - decimal2
# decimal_multiplication = decimal1 * decimal2
# decimal_division = decimal1 / decimal2

# # Numeric Operations with Complex Numbers
# complex_num1 = 2 + 3j
# complex_num2 = 1 - 1j

# complex_addition = complex_num1 + complex_num2
# complex_subtraction = complex_num1 - complex_num2
# complex_multiplication = complex_num1 * complex_num2
# complex_division = complex_num1 / complex_num2

# # Convert to Integer
# float_to_int = int(3.14)
# string_to_int = int("42")

# # Convert to Float
# int_to_float = float(42)
# string_to_float = float("3.14")

# # Convert to String
# int_to_str = str(42)
# float_to_str = str(3.14)

# # Convert to Boolean
# int_to_bool = bool(0)
# float_to_bool = bool(0.0)
# string_to_bool = bool("True")

# # Additional Numeric Operations...

# # Print Results
# print("Arithmetic Operations:")
# print(f"Addition: {addition}")
# print(f"Subtraction: {subtraction}")
# print(f"Multiplication: {multiplication}")
# print(f"Division: {division}")
# print(f"Floor Division: {floor_division}")
# print(f"Modulus: {modulus}")
# print(f"Exponentiation: {exponentiation}\n")

# print("Comparison Operations:")
# print(f"Greater Than: {greater_than}")
# print(f"Less Than: {less_than}")
# print(f"Equal To: {equal_to}")
# print(f"Not Equal To: {not_equal_to}")
# print(f"Greater Than or Equal: {greater_than_or_equal}")
# print(f"Less Than or Equal: {less_than_or_equal}\n")

# print("Rounding:")
# print(f"Rounded: {rounded}")
# print(f"Ceiling: {ceiling}")
# print(f"Floor: {floor}\n")

# print("Absolute Value:")
# print(f"Absolute Value: {absolute_value}\n")

# print("Trigonometric Functions:")
# print(f"Sine: {sine}")
# print(f"Cosine: {cosine}")
# print(f"Tangent: {tangent}\n")

# print("Square Root:")
# print(f"Square Root: {square_root}\n")

# print("Logarithmic Functions:")
# print(f"Logarithm (Base 10): {logarithm_base_10}")
# print(f"Natural Logarithm (Base e): {natural_logarithm}\n")

# print("Constants:")
# print(f"Pi: {pi}")
# print(f"Euler's Number (e): {euler_number}\n")

# print("Integer Division and Modulus:")
# print(f"Integer Result (10 // 3): {integer_result}")
# print(f"Modulus (10 % 3): {remainder}\n")

# print("Bitwise Operations:")
# print(f"Bitwise AND: {bitwise_and}")
# print(f"Bitwise OR: {bitwise_or}")
# print(f"Bitwise XOR: {bitwise_xor}")
# print(f"Bitwise NOT: {bitwise_not}")
# print(f"Left Shift: {left_shift}")
# print(f"Right Shift: {right_shift}\n")

# print("Absolute Value of Complex Number:")
# print(f"Absolute Value: {abs_complex}\n")

# print("Complex Number Operations:")
# print(f"Complex Addition: {complex_addition}")
# print(f"Complex Subtraction: {complex_subtraction}")
# print(f"Complex Multiplication: {complex_multiplication}")
# print(f"Complex Division: {complex_division}\n")

# print("Random Number Generation:")
# print(f"Random Number: {random_number}")
# print(f"Random Integer: {random_integer}")
# print(f"Random Choice: {random_choice}\n")

# print("Numeric Operations with Fractions:")
# print(f"Fraction Addition: {fraction_addition}")
# print(f"Fraction Subtraction: {fraction_subtraction}")
# print(f"Fraction Multiplication: {fraction_multiplication}")
# print(f"Fraction Division: {fraction_division}\n")

# print("Numeric Operations with Decimals:")
# print(f"Decimal Addition: {decimal_addition}")
# print(f"Decimal Subtraction: {decimal_subtraction}")
# print(f"Decimal Multiplication: {decimal_multiplication}")
# print(f"Decimal Division: {decimal_division}\n")

# print("Numeric Operations with Complex Numbers:")
# print(f"Complex Addition: {complex_addition}")
# print(f"Complex Subtraction: {complex_subtraction}")
# print(f"Complex Multiplication: {complex_multiplication}")
# print(f"Complex Division: {complex_division}\n")

# print("Type Conversions:")
# print(f"Float to Integer: {float_to_int}")
# print(f"String to Integer: {string_to_int}")
# print(f"Integer to Float: {int_to_float}")
# print(f"String to Float: {string_to_float}")
# print(f"Integer to String: {int_to_str}")
# print(f"Float to String: {float_to_str}")
# print(f"Integer to Boolean: {int_to_bool}")
# print(f"Float to Boolean: {float_to_bool}")
# print(f"String to Boolean: {string_to_bool}")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''Additional Numeric Operations''''''''''''''''''''''''''''''''''''
# import math
# import random
# import fractions
# from decimal import Decimal

# # 1. Absolute Value of Complex Number
# complex_num = complex(-3, 4)
# abs_complex = abs(complex_num)

# # 2. Complex Number Operations
# complex1 = complex(2, 3)
# complex2 = complex(1, 2)

# complex_addition = complex1 + complex2
# complex_subtraction = complex1 - complex2
# complex_multiplication = complex1 * complex2
# complex_division = complex1 / complex2

# # 3. Random Number Generation
# random_number = random.random()
# random_integer = random.randint(1, 10)
# random_choice = random.choice(['apple', 'banana', 'cherry'])

# # 4. Numeric Operations with Fractions
# fraction1 = fractions.Fraction(1, 3)
# fraction2 = fractions.Fraction(2, 5)

# fraction_addition = fraction1 + fraction2
# fraction_subtraction = fraction1 - fraction2
# fraction_multiplication = fraction1 * fraction2
# fraction_division = fraction1 / fraction2

# # 5. Numeric Operations with Decimals
# decimal1 = Decimal('0.1')
# decimal2 = Decimal('0.2')

# decimal_addition = decimal1 + decimal2
# decimal_subtraction = decimal1 - decimal2
# decimal_multiplication = decimal1 * decimal2
# decimal_division = decimal1 / decimal2

# # 6. Numeric Operations with Complex Numbers
# complex_num1 = 2 + 3j
# complex_num2 = 1 - 1j

# complex_addition = complex_num1 + complex_num2
# complex_subtraction = complex_num1 - complex_num2
# complex_multiplication = complex_num1 * complex_num2
# complex_division = complex_num1 / complex_num2

# # 7. Convert to Integer
# float_to_int = int(3.14)
# string_to_int = int("42")

# # 8. Convert to Float
# int_to_float = float(42)
# string_to_float = float("3.14")

# # 9. Convert to String
# int_to_str = str(42)
# float_to_str = str(3.14)

# # 10. Convert to Boolean
# int_to_bool = bool(0)
# float_to_bool = bool(0.0)
# string_to_bool = bool("True")

# # Print Additional Results
# print("Additional Numeric Operations:")
# print(f"Absolute Value of Complex Number: {abs_complex}\n")
# print("Complex Number Operations:")
# print(f"Complex Addition: {complex_addition}")
# print(f"Complex Subtraction: {complex_subtraction}")
# print(f"Complex Multiplication: {complex_multiplication}")
# print(f"Complex Division: {complex_division}\n")
# print("Random Number Generation:")
# print(f"Random Number: {random_number}")
# print(f"Random Integer: {random_integer}")
# print(f"Random Choice: {random_choice}\n")
# print("Numeric Operations with Fractions:")
# print(f"Fraction Addition: {fraction_addition}")
# print(f"Fraction Subtraction: {fraction_subtraction}")
# print(f"Fraction Multiplication: {fraction_multiplication}")
# print(f"Fraction Division: {fraction_division}\n")
# print("Numeric Operations with Decimals:")
# print(f"Decimal Addition: {decimal_addition}")
# print(f"Decimal Subtraction: {decimal_subtraction}")
# print(f"Decimal Multiplication: {decimal_multiplication}")
# print(f"Decimal Division: {decimal_division}\n")
# print("Numeric Operations with Complex Numbers:")
# print(f"Complex Addition: {complex_addition}")
# print(f"Complex Subtraction: {complex_subtraction}")
# print(f"Complex Multiplication: {complex_multiplication}")
# print(f"Complex Division: {complex_division}\n")
# print("Type Conversions:")
# print(f"Float to Integer: {float_to_int}")
# print(f"String to Integer: {string_to_int}")
# print(f"Integer to Float: {int_to_float}")
# print(f"String to Float: {string_to_float}")
# print(f"Integer to String: {int_to_str}")
# print(f"Float to String: {float_to_str}")
# print(f"Integer to Boolean: {int_to_bool}")
# print(f"Float to Boolean: {float_to_bool}")
# print(f"String to Boolean: {string_to_bool}")

# # '''''''''''''''''''''''''''Integer Operations''''''''''''''''''''''''''''''''''''''
# import math
# # Basic Arithmetic Operations
# num1 = 10
# num2 = 5

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# floor_division = num1 // num2
# modulus = num1 % num2
# exponentiation = num1 ** num2

# # Comparison Operations
# greater_than = num1 > num2
# less_than = num1 < num2
# equal_to = num1 == num2
# not_equal_to = num1 != num2
# greater_than_or_equal = num1 >= num2
# less_than_or_equal = num1 <= num2

# # Rounding
# number = 3.14159
# rounded = round(number, 2)
# ceiling = math.ceil(number)
# floor = math.floor(number)

# # Absolute Value
# negative_number = -42
# absolute_value = abs(negative_number)

# # Bitwise Operations
# bitwise_and = 0b1100 & 0b1010
# bitwise_or = 0b1100 | 0b1010
# bitwise_xor = 0b1100 ^ 0b1010
# bitwise_not = ~0b1100
# left_shift = 0b0010 << 2
# right_shift = 0b1100 >> 2

# # GCD and LCM
# gcd = math.gcd(30, 45)
# lcm = math.lcm(12, 18)

# # Factorial
# factorial = math.factorial(5)

# # Integer Square Root
# integer_square_root = math.isqrt(16)

# # Trigonometric Functions
# angle_degrees = 30
# angle_radians = math.radians(angle_degrees)
# sine = math.sin(angle_radians)
# cosine = math.cos(angle_radians)
# tangent = math.tan(angle_radians)

# # Square Root
# number_to_sqrt = 25
# square_root = math.sqrt(number_to_sqrt)

# # Logarithmic Functions
# logarithm_base_10 = math.log10(100)
# natural_logarithm = math.log(2.71828)  # Approximation of e

# # Constants
# pi = math.pi
# euler_number = math.e

# # Integer Division
# integer_result = 10 // 3

# # Modulus (Remainder)
# remainder = 10 % 3

# # Convert to Integer
# float_to_int = int(3.14)
# string_to_int = int("42")

# # Convert to Boolean
# int_to_bool = bool(0)
# float_to_bool = bool(0.0)
# string_to_bool = bool("True")

# # Print Results
# print("Arithmetic Operations:")
# print(f"Addition: {addition}")
# print(f"Subtraction: {subtraction}")
# print(f"Multiplication: {multiplication}")
# print(f"Division: {division}")
# print(f"Floor Division: {floor_division}")
# print(f"Modulus: {modulus}")
# print(f"Exponentiation: {exponentiation}\n")

# print("Comparison Operations:")
# print(f"Greater Than: {greater_than}")
# print(f"Less Than: {less_than}")
# print(f"Equal To: {equal_to}")
# print(f"Not Equal To: {not_equal_to}")
# print(f"Greater Than or Equal To: {greater_than_or_equal}")
# print(f"Less Than or Equal To: {less_than_or_equal}\n")

# print("Rounding:")
# print(f"Rounded Value: {rounded}")
# print(f"Ceiling: {ceiling}")
# print(f"Floor: {floor}\n")

# print("Absolute Value:")
# print(f"Absolute Value: {absolute_value}\n")

# print("Bitwise Operations:")
# print(f"Bitwise AND: {bitwise_and}")
# print(f"Bitwise OR: {bitwise_or}")
# print(f"Bitwise XOR: {bitwise_xor}")
# print(f"Bitwise NOT: {bitwise_not}")
# print(f"Left Shift: {left_shift}")
# print(f"Right Shift: {right_shift}\n")

# print("GCD and LCM:")
# print(f"GCD: {gcd}")
# print(f"LCM: {lcm}\n")

# print("Factorial:")
# print(f"Factorial: {factorial}\n")

# print("Integer Square Root:")
# print(f"Integer Square Root: {integer_square_root}\n")

# print("Trigonometric Functions:")
# print(f"Sine: {sine}")
# print(f"Cosine: {cosine}")
# print(f"Tangent: {tangent}\n")

# print("Square Root:")
# print(f"Square Root: {square_root}\n")

# print("Logarithmic Functions:")
# print(f"Logarithm (Base 10): {logarithm_base_10}")
# print(f"Natural Logarithm (Base e): {natural_logarithm}\n")

# print("Constants:")
# print(f"Pi: {pi}")
# print(f"Euler's Number (e): {euler_number}\n")

# print("Integer Division and Modulus:")
# print(f"Integer Result (10 // 3): {integer_result}")
# print(f"Modulus (10 % 3): {remainder}\n")

# print("Type Conversions:")
# print(f"Float to Integer: {float_to_int}")
# print(f"String to Integer: {string_to_int}")
# print(f"Integer to Boolean: {int_to_bool}")
# print(f"Float to Boolean: {float_to_bool}")
# print(f"String to Boolean: {string_to_bool}")

# # ''''''''''''''''''''''''Integer Overflow and Underflow'''''''''''''''''''''''''''
# '''nteger overflow and underflow are not typically issues in Python because 
# Python integers can dynamically adjust in size to accommodate very large or very small numbers'''
# import sys

# # Define maximum and minimum values for demonstration
# max_int = sys.maxsize
# min_int = -sys.maxsize - 1

# # Overflow Example
# overflowed_value = max_int + 1
# print(f"Overflowed Value: {overflowed_value}")

# # Underflow Example
# underflowed_value = min_int - 1
# print(f"Underflowed Value: {underflowed_value}")

# # Overflow Prevention
# try:
#     safe_addition = max_int + 100  # This will not cause overflow
# except OverflowError as e:
#     print("OverflowError:", e)

# # Underflow Prevention
# try:
#     safe_subtraction = min_int - 100  # This will not cause underflow
# except OverflowError as e:
#     print("OverflowError:", e)

# # '''''''''''''''''''''''''''Integer Constants'''''''''''''''''''''''
# # Integer Constants in Python

# # Binary Constants
# binary_0b1010 = 0b1010  # Binary representation of 10
# binary_0b1100 = 0b1100  # Binary representation of 12

# # Octal Constants
# octal_0o12 = 0o12  # Octal representation of 10
# octal_0o14 = 0o14  # Octal representation of 12

# # Hexadecimal Constants
# hexadecimal_0x1A = 0x1A  # Hexadecimal representation of 26
# hexadecimal_0xFF = 0xFF  # Hexadecimal representation of 255

# # Large Integers
# large_integer = 1234567890123456789012345678901234567890

# # Negative Integers
# negative_integer = -42

# # Constants for Mathematical Operations
# pi = 3.14159265358979323846
# euler_number = 2.71828182845904523536
# golden_ratio = 1.618033988749895

# # Constants for Bits
# bit_mask = 0b11110000  # Bit mask with first 4 bits set to 1
# all_bits_set = 0xFFFFFFFF  # All 32 bits set to 1

# # Special Constants
# infinity = float('inf')  # Positive infinity
# negative_infinity = float('-inf')  # Negative infinity
# not_a_number = float('nan')  # Not-a-Number (NaN)

# # 9. Minimum and Maximum Integer Values
# max_int = 2**63 - 1  # Maximum signed 64-bit integer (Python 3)
# min_int = -2**63     # Minimum signed 64-bit integer (Python 3)

# # 13. Minimum Positive Subnormal Float (PEP 754)
# min_positive_subnormal = 2.0**-1074

# # Print Integer Constants

# print("Binary Constants:")
# print(f"Binary 0b1010: {binary_0b1010}")
# print(f"Binary 0b1100: {binary_0b1100}\n")

# print("Octal Constants:")
# print(f"Octal 0o12: {octal_0o12}")
# print(f"Octal 0o14: {octal_0o14}\n")

# print("Hexadecimal Constants:")
# print(f"Hexadecimal 0x1A: {hexadecimal_0x1A}")
# print(f"Hexadecimal 0xFF: {hexadecimal_0xFF}\n")

# print("Large Integers:")
# print(f"Large Integer: {large_integer}\n")

# print("Negative Integers:")
# print(f"Negative Integer: {negative_integer}\n")

# print("Constants for Mathematical Operations:")
# print(f"Pi: {pi}")
# print(f"Euler's Number: {euler_number}")
# print(f"Golden Ratio: {golden_ratio}\n")

# print("Constants for Bits:")
# print(f"Bit Mask: {bit_mask}")
# print(f"All Bits Set: {all_bits_set}\n")

# print("Special Constants:")
# print(f"Infinity: {infinity}")
# print(f"Negative Infinity: {negative_infinity}")
# print(f"Not-a-Number (NaN): {not_a_number}")

# print(f'max_int: {max_int}')
# print(f'min_int: {min_int}')

# print(f'min_positive_subnormal: {min_positive_subnormal}')

# from decimal import Decimal
# # Decimal to Integer (conversion)
# decimal_to_integer = int(Decimal("42"))
# print(f'decimal_to_integer: {decimal_to_integer}')
# print(int("123456789012345678901234567890"))
# print(float("123456789012345678901234567890"))

# # # Complex Number to Float (conversion)
# # complex_to_float = float(4 + 5j) # get error: float() argument must be a string or a real number, not 'complex'
# # print(f'complex_to_float: {complex_to_float}')

# # Decimal to Float (conversion)
# decimal_to_float = float(Decimal("3.14"))
# print(f'decimal_to_float: {decimal_to_float}')

# # NaN to Float (conversion)
# nan_to_float = float(float('nan'))
# print(f'nan_to_float: {nan_to_float}')

# # Infinity to Float (conversion)
# positive_inf_to_float = float(float('inf'))
# negative_inf_to_float = float(float('-inf'))

# print(f'positive_inf_to_float: {positive_inf_to_float}')
# print(f'negative_inf_to_float: {negative_inf_to_float}')

# # '''''''''''''''''''''''''''''''Integer Formatting'''''''''''''''''''''''''''''''''
# # Integer Formatting in Python

# # Integer values
# num1 = 12345
# num2 = -6789

# # Basic Integer Formatting
# formatted_num1 = f"Number 1: {num1}"
# formatted_num2 = f"Number 2: {num2}"

# # Integer with Leading Zeros (5 digits)
# formatted_with_zeros = f"Formatted with leading zeros: {num1:05}"

# # Integer as Currency
# formatted_currency = f"Formatted as currency: ${num2:,.2f}"

# # Integer with Plus Sign for Positive Numbers
# formatted_plus_sign = f"Formatted with plus sign: {num1:+}"

# # Integer as Percentage
# formatted_percentage = f"Formatted as percentage: {num2:.2%}"

# # Integer in Exponential Notation
# formatted_exponential = f"Formatted in exponential notation: {num1:.2e}"

# # Integer with Thousands Separator
# formatted_thousands_separator = f"Formatted with thousands separator: {num1:,}"

# # Integer with Custom Separator
# formatted_custom_separator = f"Formatted with custom separator: {num2:_}"

# # Integer with Left Alignment
# formatted_left_alignment = f"Left-aligned with width 10: {num1:<10}"

# # Integer with Center Alignment
# formatted_center_alignment = f"Center-aligned with width 15: {num2:^15}"

# # Integer with Right Alignment
# formatted_right_alignment = f"Right-aligned with width 12: {num1:>12}"

# # Hexadecimal Representation
# formatted_hexadecimal = f"Hexadecimal representation: {num1:X}"

# # Binary Representation
# formatted_binary = f"Binary representation: {num2:b}"

# # Octal Representation
# formatted_octal = f"Octal representation: {num1:o}"

# # Integer with Alternate Form
# formatted_alternate_form = f"Formatted with alternate form: {num2:#X}"

# # Integer with Sign Prefix
# formatted_sign_prefix = f"Formatted with sign prefix: {num1:+}"

# # Zero-Padded Binary Representation
# formatted_zero_padded_binary = f"Zero-padded binary representation: {num2:08b}"

# # Integer with Comma Separators and Width
# formatted_comma_and_width = f"Formatted with comma separators and width: {num1:0>12,}"

# # Custom Numeric Formatting
# def custom_format(x):
#     return f"Custom formatted: {x * 2}"

# formatted_custom_numeric = custom_format(num2)

# # Output
# print(formatted_num1)
# print(formatted_num2)
# print(formatted_with_zeros)
# print(formatted_currency)
# print(formatted_plus_sign)
# print(formatted_percentage)
# print(formatted_exponential)
# print(formatted_thousands_separator)
# print(formatted_custom_separator)
# print(formatted_left_alignment)
# print(formatted_center_alignment)
# print(formatted_right_alignment)
# print(formatted_hexadecimal)
# print(formatted_binary)
# print(formatted_octal)
# print(formatted_alternate_form)
# print(formatted_sign_prefix)
# print(formatted_zero_padded_binary)
# print(formatted_comma_and_width)
# print(formatted_custom_numeric)
