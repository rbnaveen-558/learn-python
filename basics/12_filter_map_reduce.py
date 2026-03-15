# Sample: Python filter, map, and reduce Examples

# filter example: get even numbers
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers (filter):", even)

# map example: square each number
squares = list(map(lambda x: x ** 2, nums))
print("Squares (map):", squares)

# reduce example: sum all numbers
from functools import reduce
sum_nums = reduce(lambda x, y: x + y, nums)
print("Sum (reduce):", sum_nums)

# More examples
# filter: remove empty strings
words = ["apple", "", "banana", "", "cherry"]
non_empty = list(filter(None, words))
print("Non-empty words (filter):", non_empty)

# map: uppercase words
upper_words = list(map(str.capitalize, words))
print("Uppercase words (map):", upper_words)

# reduce: concatenate words
concat = reduce(lambda x, y: x + y, non_empty)
print("Concatenated words (reduce):", concat)

# Fibonacci sequence example
def fibonacci(n):
	seq = []
	a, b = 0, 1
	for _ in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq

print("First 10 Fibonacci numbers:", fibonacci(10))

square = list(map(lambda x: x**2, range(10)))
print("Squares of first 10 numbers:", square)