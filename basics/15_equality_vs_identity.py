# Sample: Python == vs is Examples

# == checks for value equality
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x), id(y))  # Different memory addresses
print("x == y:", x == y)  # True, values are equal
print("x is y:", x is y)  # False, different objects

# is checks for identity (same object)
z = x
print("x is z:", x is z)  # True, same object

# == with numbers
num1 = 1000
num2 = 1000
print("num1 == num2:", num1 == num2)  # True
print("num1 is num2:", num1 is num2)  # May be False (different objects)

# == with strings
s1 = "hello"
s2 = "hello"
print(id(s1), id(s2))
print("s1 == s2:", s1 == s2)  # True
print("s1 is s2:", s1 is s2)  # True (string interning), but not guaranteed for all cases

# Explanation:
# == compares values, is compares object identity (memory address).
