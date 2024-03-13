# 1. Power of a Number
def power(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        y //= 2
        x *= x
    return result

# 2. Minimum and Maximum
def min_and_max(lst):
    minimum = maximum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return (minimum, maximum)

# 3. Check Leap Year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 4. Calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# 5. Rotating Digits
def rotate_digits(n):
    if n < 10:
        return n
    last_digit = n % 10
    rest_of_digits = n // 10
    multiplier = 10 ** (len(str(rest_of_digits)))
    return last_digit * multiplier + rest_of_digits

# 6. Minimum and Maximum but with Loops
# For loop
def min_with_for_loop(lst):
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def max_with_for_loop(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

# While loop
def min_with_while_loop(lst):
    minimum = lst[0]
    index = 1
    while index < len(lst):
        if lst[index] < minimum:
            minimum = lst[index]
        index += 1
    return minimum

def max_with_while_loop(lst):
    maximum = lst[0]
    index = 1
    while index < len(lst):
        if lst[index] > maximum:
            maximum = lst[index]
        index += 1
    return maximum

# 7. Vowels
def vowel_count(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# 8. Digital Root
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n