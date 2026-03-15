# Sample: Python Dictionary Operations and Methods

# Dictionary creation
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Original dictionary:", person)

# Access value
print("Name:", person["name"])

# Add/update key-value
person["email"] = "alice@example.com"
person["age"] = 31
print("After add/update:", person)

# Remove key
removed = person.pop("city")
print("After pop 'city':", person, "Removed value:", removed)

# Get value with default
print("Country:", person.get("country", "Unknown"))

# Keys, values, items
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Iterate over items
for key, value in person.items():
    print(f"{key}: {value}")

# Check existence
print("Has 'email'?", "email" in person)

# Copy dictionary
person_copy = person.copy()
print("Copy:", person_copy)

# Clear dictionary
person.clear()
print("After clear:", person)

# Merge dictionaries
info = {"country": "USA", "gender": "F"}
merged = {**person_copy, **info}
print("Merged dictionary:", merged)

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
print("Squared dict:", squared)

# Count each character in a string
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Character counts:")
for char, count in char_count.items():
    print(f"{char}: {count}")

