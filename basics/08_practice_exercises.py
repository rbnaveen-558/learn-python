# Sample: Python Practice Exercises

# 1. Simple calculator
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Invalid operator"

print("Calculator 2+3:", calculator(2, 3, '+'))

# 2. File parser
def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

# Create and count lines in a file
with open("test.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
print("Line count in test.txt:", count_lines("test.txt"))

# 3. List filtering
nums = [1, 2, 3, 4, 5]
even = [n for n in nums if n % 2 == 0]
print("Even numbers:", even)
# More list comprehension examples
# Squares of numbers
squares = [n**2 for n in nums]
print("Squares:", squares)

# Uppercase strings
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print("Uppercase words:", upper_words)

# Pairs (i, j) where i != j
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print("Pairs where i != j:", pairs)

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened list:", flat)


def main():
    st = "hello world"
    st = st.upper()
    print(st)

    l = [1, 2, 3]
    l.append(4)
    print(l)

    s = {1,3,2,2}
    s.add(4)
    print(s)

def ispolyndorm():
    st = "madam"
    return st == st[::-1]

if __name__ == "__main__":
    print(ispolyndorm())


# 4. Anagram checker
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

are_anagrams("listen", "silent")