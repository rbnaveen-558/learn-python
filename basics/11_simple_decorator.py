# Sample: Python Simple Decorator Example

def my_decorator(func):
    def any():
        print("Before function call any")
        func()
        print("After function call any")
    return any

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator for functions with parameters
def my_param_decorator(funct):
    def wrapper(*arg, **kwargs):
        print("Before function call (with params) changed")
        result = funct(*arg, **kwargs)
        print("After function call (with params)")
        return result
    return wrapper

@my_param_decorator
def greet(name: str):
    print(f"Hello, {name}!")

greet("Alice")
 
# Decorator defined inside a class
class Logger:
    @staticmethod
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            print("[LOG] Before method call")
            func(*args, **kwargs)
            print("[LOG] After method call")
        return wrapper

class Person:
    @Logger.log_decorator
    def say_name(self, name):
        print(f"My name is {name}.")

p = Person()
p.say_name("Bob")

# Explanation:
# The @my_decorator syntax applies the decorator to the say_hello function.
# When say_hello() is called, it runs the wrapper, which adds behavior before and after the original function.
