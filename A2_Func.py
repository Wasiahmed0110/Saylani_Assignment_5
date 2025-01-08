# Task 1
def divisible_by_7_not_5():
    return ",".join(str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0)

# Task 2
import math

def calculate_p(values):
    A, B = 50, 30
    result = [str(int(math.sqrt((2 * A * B) / int(c)))) for c in values.split(",")]
    return ",".join(result)

# Task 3
def sort_words(sequence):
    return ",".join(sorted(sequence.split(",")))

# Task 4
def capitalize_lines(lines):
    return "\n".join(line.upper() for line in lines.split("\n"))

# Task 5
def count_vowels(sentence):
    vowels = "aeiou"
    result = {vowel: sentence.lower().count(vowel) for vowel in vowels}
    return "\n".join(f"{v} appeared {result[v]} times" for v in vowels)

# Task 6
def even_digit_numbers():
    return [i for i in range(1000, 3001) if all(int(d) % 2 == 0 for d in str(i))]

# Task 7
def binary_divisible_by_5(binary_numbers):
    return ",".join(b for b in binary_numbers.split(",") if int(b, 2) % 5 == 0)

# Task 8
def count_letters_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return f"LETTERS {letters}\nDIGITS {digits}"
