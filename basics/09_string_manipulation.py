# Sample: Python String Manipulation Examples

# Concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print("Concatenation:", result)

# String formatting
name = "Alice"
age = 30
formatted = f"Name: {name}, Age: {age}"
print("Formatted string:", formatted)

# Changing case
text = "Python"
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

# Stripping whitespace
raw = "  hello  "
print("Stripped:", raw.strip())

# Splitting and joining
sentence = "one,two,three"
words = sentence.split(",")
print("Split:", words)
joined = "-".join(words)
print("Joined:", joined)

# Replacing substrings
msg = "I like apples"
print("Replace:", msg.replace("apples", "bananas"))
print(msg)

# Finding substrings
print("Find 'like':", msg.find("like"))

# Slicing
sample = "abcdef"
print("Slice [1:4]:", sample[1:4])

# Checking start/end
print("Starts with 'a':", sample.startswith("a"))
print("Ends with 'f':", sample.endswith("f"))
