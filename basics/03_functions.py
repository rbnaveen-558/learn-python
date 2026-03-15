# Sample: Python Functions

def greet(name):
    return f"Hello, {name}!"

# Lambda function
add = lambda x, y: x + y

# Built-in functions
numbers = [1, 2, 3, 4]
print("Sum:", sum(numbers))

# Scope example
def outer():
    x = "outer"
    def inner():
        print("Inner x:", x)
    inner()

print(greet("Alice"))
print("Add lambda:", add(2, 3))
outer()
