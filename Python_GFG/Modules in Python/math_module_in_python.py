'''Constants:

math.pi: π (pi)
math.e: e
Basic Arithmetic Functions:

math.sqrt(x): Square root of x
math.pow(x, y): x raised to the power of y
math.exp(x): e raised to the power of x
math.log(x, base): Logarithm of x with the specified base
math.log10(x): Base-10 logarithm of x
math.log2(x): Base-2 logarithm of x
math.ceil(x): Smallest integer greater than or equal to x
math.floor(x): Largest integer less than or equal to x
math.fabs(x): Absolute value of x
math.factorial(x): Factorial of x
math.isfinite(x): Checks if x is a finite number
math.isinf(x): Checks if x is positive or negative infinity
math.isnan(x): Checks if x is a NaN (Not-a-Number)
math.gcd(x, y): Greatest common divisor of x and y
Trigonometric Functions:

math.sin(x): Sine of x (in radians)
math.cos(x): Cosine of x (in radians)
math.tan(x): Tangent of x (in radians)
math.asin(x): Inverse sine of x (result in radians)
math.acos(x): Inverse cosine of x (result in radians)
math.atan(x): Inverse tangent of x (result in radians)
math.atan2(y, x): Inverse tangent of y/x (result in radians)
Hyperbolic Functions:

math.sinh(x): Hyperbolic sine of x
math.cosh(x): Hyperbolic cosine of x
math.tanh(x): Hyperbolic tangent of x
Angular Conversion Functions:

math.radians(degrees): Converts degrees to radians
math.degrees(radians): Converts radians to degrees
Exponentiation and Logarithmic Functions:

math.exp(x): e raised to the power of x
math.log(x, base): Logarithm of x with the specified base
math.log10(x): Base-10 logarithm of x
math.log2(x): Base-2 logarithm of x
Rounding and Absolute Value Functions:

math.ceil(x): Smallest integer greater than or equal to x
math.floor(x): Largest integer less than or equal to x
math.fabs(x): Absolute value of x
Statistical Functions:

math.factorial(x): Factorial of x
Trigonometric Functions:

math.sin(x): Sine of x (in radians)
math.cos(x): Cosine of x (in radians)
math.tan(x): Tangent of x (in radians)
Inverse Trigonometric Functions:

math.asin(x): Inverse sine of x (result in radians)
math.acos(x): Inverse cosine of x (result in radians)
math.atan(x): Inverse tangent of x (result in radians)
math.atan2(y, x): Inverse tangent of y/x (result in radians)
Hyperbolic Functions:

math.sinh(x): Hyperbolic sine of x
math.cosh(x): Hyperbolic cosine of x
math.tanh(x): Hyperbolic tangent of x
Angular Conversion Functions:

math.radians(degrees): Converts degrees to radians
math.degrees(radians): Converts radians to degrees
Other Mathematical Functions:

math.isfinite(x): Checks if x is a finite number
math.isinf(x): Checks if x is positive or negative infinity
math.isnan(x): Checks if x is a NaN (Not-a-Number)
math.gcd(x, y): Greatest common divisor of x and y
math.erf(x): Error function of x
math.erfc(x): Complementary error function of x
math.gamma(x): Gamma function of x
math.lgamma(x): Natural logarithm of the absolute value of the gamma function of x
math.modf(x): Returns the fractional and integer parts of x as a tuple
math.frexp(x): Returns the mantissa and exponent of x as a tuple
math.trunc(x): Truncates x to the nearest integer toward 0
math.copysign(x, y): Returns x with the sign of y
math.hypot(x, y): Returns the Euclidean norm, sqrt(xx + yy)'''

import math

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''Math Constants''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
pi = math.pi
print("Pi:", pi)

e = math.e
print("Euler's Number:", e)

# '''''''''''''''''''''''''''''''''''''''''''''''''''Basic Arithmetic Functions''''''''''''''''''''''''''''''''''''''''''''
# '''''1.Absolute Value
num = -5
absolute_value = math.fabs(num)
print(f"Absolute Value: {absolute_value}")

# '''''''''2.Rounding Functions
# round up to the nearest integer
num1 = 4.6
ceil_value = math.ceil(num1)
print(f'Ceil Value of {num1} is {ceil_value}')

# Round down to the nearest integer
num2 = 4.7
floor_value = math.floor(num2)
print(f'floor value of {num2} is {floor_value}') 

# Round to the nearest integer
num3 = 4.7
num4 = 4.3
rounded_value_1 = round(num3)
rounded_value_2 = round(num4)
print(f"rounded_value_1: {rounded_value_1}")
print(f"rounded_value_2: {rounded_value_2}")

# '''''''''''''3.Exponents and Power
# Calculate the e raised to the power of 2
x = 2
exp_value = math.exp(x) # e^2
print(f"e^{x} is {exp_value}")

# Calculate the x raised to the power of y
base = 2
exponent = 3
power_value = math.pow(base, exponent) # 2^3
print(f"{base} raised to the power of {exponent} is {power_value}")

# '''''''''''''''''''''''''''''''''''''Turncates Decimal Parts''''''''''''''''''''''''''
num = 7.9
turncate_value = math.trunc(num)
print(f'Turncate value of {num} is {turncate_value}')

# ''''''''''''''''''''''''''Maximum and Minimum'''''''''''''''
# Find the maximum of the two numbers
max_value = max(10, 7)
print(f'max_value: {max_value}')

# Find the minimum of the two numbers
min_value = min(10, 7)
print(f'min_value: {min_value}')

# ''''''''''''''''''''''''''''''''''''''''''