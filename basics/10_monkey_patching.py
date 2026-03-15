# Sample: Python Monkey Patching Example

class Greet:
    def say_hello(self):
        print("Hello!")

g = Greet()
g.say_hello()  # Output: Hello!

# Monkey patching: change say_hello at runtime
def new_hello(self):
    print("Hi, this is monkey patched!")


Greet.say_hello = new_hello
g.var = "This is a new variable added via monkey patching."

g.say_hello()  # Output: Hi, this is monkey patched!
print(g.var)  # Output: This is a new variable added via monkey patching!
print(Greet.var)  # Output: This is a new variable added via monkey patching!


# Explanation:
# Monkey patching is the practice of modifying or extending code at runtime,
# such as replacing methods or attributes of classes or modules.
# It is often used for testing, debugging, or adding features dynamically.
