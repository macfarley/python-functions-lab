# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base: int, height: int) -> float:  # type hinting notation
    return (base * height) / 2


print('Exercise 1:', calculate_area_triangle(10, 5)) #expected 25.0
# print('Exercise 1:', calculate_area_triangle(7, 3)) #expected 10.5

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal: float, rate: float, time: int) -> float:
    return (principal * rate * time) / 100


print('Exercise 2:', simple_interest(1000, 5, 2)) #expect 100
# print('Exercise 2:', simple_interest(1500, 3.5, 5)) #expect 262.5
# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price: float, discount: int) -> float:
    savings = (price * discount/100)
    return price-savings

print('Exercise 3:', apply_discount(100, 25))
# print(apply_discount(80, 10)) #expect 72

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature(temperature: float, unit: str) -> float:
    unit = unit.upper()
    if unit not in ('C', 'F'):
        raise ValueError('Converter does not support that unit, use F for Fahrenheit or C for Celsius')
    elif unit == 'C':
        return (temperature * 9/5) + 32
    else: #default, only F remains
        return (temperature - 32) * 5/9


print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
# print(convert_temperature(35, "C")) #expect 95
# print(convert_temperature(273, 'K')) #expect Error
# print(convert_temperature(104, 'f')) #expect 40

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
def sum_to(n: int) -> int:
    # return (n/2)*(n+1) #this is known (to google) mathmatical formula, easier to run it than loops
    i = n-1
    total = n #starts with itself
    while i >= 1:
        total += i #add the next smallest
        i -= 1 #shrink the increment
    return total #after the loop breaks


print('Exercise 5:', sum_to(6)) #expect 21
# print(sum_to(10)) #expect 55
# print(sum_to(99)) #expect 4950


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.

def largest(a: float, b: float, c:float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: #if neither a or b is largest it must be
        return c

print('Exercise 6:', largest(1, 2, 3))
# print(largest(-100, 42, 3.14 )) #expect 42

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
def calculate_tip(subtotal:float , tip: int) ->float:
    return subtotal * (tip/100)


print('Exercise 7:', calculate_tip(50, 20)) #expect 10
print(calculate_tip(456, 18))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
def product(*args: int)->int:
    total = 1 #even if there's only 1 arg it will be equal to itself
    for num in args:
        total = total*num
    return total


print('Exercise 8:', product(2, 5, 5)) #expect 50
# print(product(4,4,4)) #expect 64
# print(product(10, 10, 10, 10, 10, 25)) #2,500,000 but all together


# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.
def basic_calculator(a: int, b: int, operator: str)-> int:
    if operator not in ('subtract', 'add', 'multiply', 'divide'):
        raise ValueError ("this calculator can't do that don't break me")
    elif operator == 'add':
        return a+b
    elif operator == 'subtract':
        return a-b
    elif operator == 'multiply':
        return a*b
    else: #last possible
        return a/b


print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
print(basic_calculator(144, 12, 'divide')) #expect 12
print(basic_calculator(100, 2, 'root')) #expect error
