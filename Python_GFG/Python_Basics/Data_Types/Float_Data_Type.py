# '''In Python, the float data type represents floating-point numbers, which are numbers that have a decimal point or use exponential notation. Floats are used to represent real numbers and can be positive, negative, or zero'''

# # '''''''''''''''''''''''''''''''''Syntax for Declaring a float-data type variable'''''''''''''''''''''''''''''''''''''''''''''''
# '''
# Syntax for float data types;
#     variable_name = float_value
# '''
# # Direct Assignment
# x = 3.14
# y = -0.5
# z = 2.0e3

# # Using 'float()' Constructor
# x = float(3) # explicity conversion
# y = float("3.14") # explicity conversion

# # Using Arithmetic Operation
# x = 5
# y = 2
# result = x / y  # results in a float value

# # # Reading from User Input
# # float_value = float(input("Enter a float value: "))
# # print(f'Float value: {float_value}')

# # Using Variable in Expression
# radius = 2.5
# area = 3.14 * radius ** 2

# # Iterating over Floating-Point Numbers:
# for i in range(1, 10):
#     print(i * 0.5, end=" ")

# # using math module
# import math
# pi_value = math.pi 
# print(f'Value of pi: {pi_value}')               # Output: 3.141592653589793
# e_value = math.e
# print(f"Value of Euler's number: {e_value}")    # Output: 2.718281828459045

# # # Using Constant from other modules or libraries
# # import numpy as np

# # nan_value = np.nan   # NaN (Not a Number) from NumPy
# # inf_value = float('inf')  # Infinity

# # Using Unpacking
# x, y, z = 1.5, -2.5, 3.5

# # Using Scientific Notation
# y = 2.0e3 # Equivalent to 2.0 * 10^3

# # Assigning result of calculation to a float variable
# a = 5
# b = 2
# result = float(a) / b

# # Using parentheses for clarity in expression
# pi_approximation = (22 / 7.0)
# print(f'pi approximation value: {pi_approximation}') 

# # Combining multiple floating-point values into a single variable:
# coordinate = 3.5, 2.5 # Tuple containing two float values
# print(f'coordinate point p1: {coordinate}')

# # Initializing multiple float variable in a single line
# lenght, width, height  = 5.5, 3.5, 4.5

# # Representing special float values:
# infinity = float('infinity')
# infinity = float('inf')
# print(f'infinity: {infinity}')

# negative_infinity = float('-infinity')
# negative_infinity = float('-inf')
# print(f'negative_infinity: {negative_infinity}')

# nan_value = float('nan')
# print(f'nan_value: {nan_value}')

# # '''''''''''''''''''''''''''''''''''''''''''''''''''Arithmetic Operations''''''''''''''''''''''''''''''''''''
# import math

# # Declare float variables
# x = 3.14
# y = 2.71

# # Addition
# sum_result = x + y
# print("Addition:", sum_result)

# # Subtraction
# difference_result = x - y
# print("Subtraction:", difference_result)

# # Multiplication
# product_result = x * y
# print("Multiplication:", product_result)

# # Division
# quotient_result = x / y
# print("Division:", quotient_result)

# # Exponentiation
# x_squared = x ** 2
# print("Exponentiation:", x_squared)

# # Square root using exponentiation
# y_sqrt = y ** 0.5
# print("Square root (exponentiation):", y_sqrt)

# # Square root using math.sqrt
# y_sqrt_math = math.sqrt(y)
# print("Square root (math.sqrt):", y_sqrt_math)

# # Absolute value
# abs_result = abs(-5.6)
# print("Absolute value:", abs_result)

# # Rounding
# rounded_value = round(3.1415926535, 2)
# print("Rounding:", rounded_value)

# # Increment and decrement
# increment_result = x + 1
# decrement_result = y - 1
# print("Increment:", increment_result, "Decrement:", decrement_result)

# # Modulus
# modulus_result = x % y
# print("Modulus:", modulus_result)

# # Floor division
# floor_division_result = x // y
# print("Floor division:", floor_division_result)

# # Compound assignment operators
# x += 1
# y -= 1
# print("Compound addition:", x, "Compound subtraction:", y)

# # Multiple operations in one line
# result = (x + y) * (x - y) / 2
# print("Multiple operations:", result)

# # ''''''''''''''''''''''''''''''''''''Comparsion operator''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Declare float variables
# x = 3.14
# y = 2.71

# # Greater than
# greater_than_result = x > y
# print("Greater than:", greater_than_result)

# # Greater than or equal to
# greater_than_or_equal_result = x >= y
# print("Greater than or equal to:", greater_than_or_equal_result)

# # Less than
# less_than_result = x < y
# print("Less than:", less_than_result)

# # Less than or equal to
# less_than_or_equal_result = x <= y
# print("Less than or equal to:", less_than_or_equal_result)

# # Equal to
# equal_to_result = x == y
# print("Equal to:", equal_to_result)

# # Not equal to
# not_equal_to_result = x != y
# print("Not equal to:", not_equal_to_result)

# # Comparing with tolerance
# tolerance = 0.001
# close_enough_result = abs(x - y) < tolerance
# print(f'Close enough(with tolerance: {close_enough_result}')

# # Chaninig Comparison Operators
# chained_comparison_result = 1.0 < x <= 3.14 < y
# print(f'Chained comparison: {chained_comparison_result}')

# # Floating-Point Comparison Using math.isclose()
# import math
# isclose_result = math.isclose(x, y, rel_tol=1e-9, abs_tol=0.0)
# print(f'isclose result: {isclose_result}')

# # Using round() constructor for Comparison
# x = 1123.45678
# y = 1123.7890
# rounded_x = round(x, 2)
# rounded_y = round(y, 2)
# print('Rounded Value for Comparison:\n')
# print(f'rounded_x: {rounded_x}')
# print(f'rounded_y: {rounded_y}')
# equal_after_rounding = rounded_x == rounded_y
# print(f'equal_after_rounding: {equal_after_rounding}')

# # Check for NaN (Not a Number)
# import math
# z = math.nan
# is_nan_result = math.isnan(z)
# print("Is NaN:", is_nan_result)

# # Check for infinity
# infinity_pos = float('inf')
# infinity_neg = float('-inf')
# is_infinity_pos_result = math.isinf(infinity_pos)
# is_infinity_neg_result = math.isinf(infinity_neg)
# print("Is positive infinity:", is_infinity_pos_result)
# print("Is negative infinity:", is_infinity_neg_result)

# # ''''''''''''''''''''''''''''''''''''''''''Logical Operators''''''''''''''''''''''''''''''''''''''''
# # Declare float variables
# x = 3.14
# y = 2.71
# z = 4.2

# # Logical AND
# result_and = (x > y) and (y < z)
# print("Logical AND:", result_and)  # Output: True

# # Logical OR
# result_or = (x < y) or (y > z)
# print("Logical OR:", result_or)  # Output: True

# # Logical NOT
# result_not = not (x == y)
# print("Logical NOT:", result_not)  # Output: True

# # '''''''''''''''''''''''''''''''''''Bitwise Operators''''''''''''''''''''''''''''''''''''
# x = 3.14
# y = 2.71

# # result_and = x & y
# # print(f'result_and: {result_and}') # TypeError: unsupported operand type(s) for &: 'float' and 'float

# # Declare float variables
# x = 3.14
# y = 2.71

# # Convert floats to integers
# x_int = int(x)
# y_int = int(y)

# # Bitwise AND
# result_and = x_int & y_int
# print("Bitwise AND:", result_and)

# # Bitwise OR
# result_or = x_int | y_int
# print("Bitwise OR:", result_or)

# # Bitwise XOR
# result_xor = x_int ^ y_int
# print("Bitwise XOR:", result_xor)

# # Bitwise NOT
# result_not_x = ~x_int
# print("Bitwise NOT (x):", result_not_x)
# result_not_y = ~y_int
# print("Bitwise NOT (y):", result_not_y)

# # Bitwise left shift
# result_left_shift_x = x_int << 1
# print("Bitwise left shift (x):", result_left_shift_x)
# result_left_shift_y = y_int << 1
# print("Bitwise left shift (y):", result_left_shift_y)

# # Bitwise right shift
# result_right_shift_x = x_int >> 1
# print("Bitwise right shift (x):", result_right_shift_x)
# result_right_shift_y = y_int >> 1
# print("Bitwise right shift (y):", result_right_shift_y)

# # ''''''''''''''''''''''''''''''''''''''''''Assignment Operators''''''''''''''''''''''''''''''''''''''''''''
# # Declare float variables
# x = 3.14
# y = 2.71

# # Basic assignment
# z = x + y
# print("Basic assignment:", z)  # Output: 5.85

# # Compound assignment operators
# z += x  # Equivalent to z = z + x
# print("Compound addition:", z)  # Output: 8.99

# z -= y  # Equivalent to z = z - y
# print("Compound subtraction:", z)  # Output: 6.28

# z *= x  # Equivalent to z = z * x
# print("Compound multiplication:", z)  # Output: 19.7072

# z /= y  # Equivalent to z = z / y
# print("Compound division:", z)  # Output: 7.266793313069908

# z //= x  # Equivalent to z = z // x
# print("Compound floor division:", z)  # Output: 2.0

# z %= y  # Equivalent to z = z % y
# print("Compound modulus:", z)  # Output: 1.5667933130699077

# z **= x  # Equivalent to z = z ** x
# print("Compound exponentiation:", z)  # Output: 74.29304231500186

# # '''''''''''''''''''''''''''''Membership Operators''''''''''''''''''''''''''''''''''''''''
# # List containing float elements
# float_list = [3.14, 2.71, 1.618]

# # Membership operators with float values
# print(3.14 in float_list)   # Output: True
# print(2.5 in float_list)    # Output: False

# # Membership operators with non-float values
# print(1 in float_list)      # Output: False
# print(1.618 not in float_list)  # Output: False

# # '''''''''''''''''''''''''''''''''''''''''''''Exponential Notation''''''''''''''''''''''''''''''''''''''''''''''''''''''
# large_number = 2.5e8  # 2.5 * 10^2
# small_number = 2.5e-8 # 2.5 * 10^-8
# print(f'large_number: {large_number} and small_number: {small_number}')

# # Using Uppercase E for Exponential Notation
# Large_number_2 = 2.5E8 # 2.5 * 10^8
# print(f'Large_number_2 :{Large_number_2}')

# # Performing arithmetic operations with exponential notation
# result = 2.5e2 + 3.5e1  # Equivalent to 250 + 35
# print(result)            # Output: 285.0

# # Exponential notation with arithmetic operations
# result_2 = 1.5e3 * 2.5e-2  # Equivalent to (1.5 * 10^3) * (2.5 * 10^-2)
# print(result_2)            # Output: 37.5

# # Exponential notation with division
# result_3 = 3.0e5 / 2.0e4  # Equivalent to (3.0 * 10^5) / (2.0 * 10^4)
# print(result_3)            # Output: 15.0

# # Reading input values with exponential notation 
# n = int(input("Enter number of the test cases: "))
# for _ in range(n):
#     x, y = map(float, input().split()) # Read two float values
#     # Performs the calculation with x and y 
# print(f'x = {x}, y = {y}')

# # Outputing the result in exponential notation
# result = 1.23e12 # Some calculated result
# print("{:.6e}".format(result)) # # Output result in exponential notation with 6 decimal places -> Output: 1.230000e+12

# # '''''''''''''''''''''''''''''''''recision and Limitations of floating-point numbers''''''''''''''''''''''
# # Rounding errors
# result = 0.1 + 0.2
# print(result)  # Output: 0.30000000000000004

# # Precision loss
# large_number = 12345678901234567890.0
# print(large_number)  # Output: 1.2345678901234568e+19

# # Accuracy in arithmetic operations
# result = 1.0 / 3.0
# print(result)  # Output: 0.3333333333333333

# Rounding errors
result = 0.1 + 0.2
print(result)  # Output: 0.30000000000000004

# Precision loss
large_number = 12345678901234567890.0
print(large_number)  # Output: 1.2345678901234568e+19

# Accuracy in arithmetic operations
result = 1.0 / 3.0
print(result)  # Output: 0.3333333333333333
