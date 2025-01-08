# Assignment 1
def max_of_three(a, b, c):
    return max(a, b, c)

# Assignment 2
def sum_of_list(numbers):
    return sum(numbers)

# Assignment 3
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Assignment 4
def reverse_string(s):
    return s[::-1]

# Assignment 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Assignment 6
def is_in_range(number, start, end):
    return start <= number <= end

# Assignment 7
def count_case(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case

# Assignment 8
def unique_list(lst):
    return list(set(lst))

# Assignment 9
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Assignment 10
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Assignment 11
def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

# Assignment 12
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
