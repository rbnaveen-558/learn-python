# Sample: Python Error Handling

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs.")

# Custom exception
class MyError(Exception):
    pass

def risky():
    raise MyError("Something went wrong!")

try:
    risky()
except MyError as e:
    print("Caught custom error:", e)
