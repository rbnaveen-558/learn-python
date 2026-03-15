# Sample: Python List Operations and Methods

# List creation
nums = [1, 2, 3, 4, 5]
print("Original list:", nums)

# Append
nums.append(6)
print("After append:", nums)

# Extend
nums.extend([7, 8])
print("After extend:", nums)

# Insert
nums.insert(0, 0)
print("After insert:", nums)

# Remove
nums.remove(3)
print("After remove 3:", nums)

# Pop
last = nums.pop()
print("After pop:", nums, "Popped value:", last)

# Index
idx = nums.index(4)
print("Index of 4:", idx)

# Count
count_2 = nums.count(2)
print("Count of 2:", count_2)

# Sort
nums.sort()
print("After sort:", nums)

# Reverse
nums.reverse()
print("After reverse:", nums)

# Copy
nums_copy = nums.copy()
print("Copy of list:", nums_copy)

# Clear
nums.clear()
print("After clear:", nums)

print(nums_copy)

# List slicing
letters = ['a', 'b', 'c', 'd', 'e']
print("Slice [1:4]:", letters[1:4])
print("Slice [-3:]:", letters[-3:])

# List comprehension
squared = [x**2 for x in range(5)]
print("Squared numbers:", squared)

