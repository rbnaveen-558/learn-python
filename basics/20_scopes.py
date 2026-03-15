# Sample: Python Scopes Explained

# 1. Global Scope
global_var = "I am a global variable"

def demonstrate_scopes():
    # 2. Enclosing Scope
    enclosing_var = "I am an enclosing variable"

    def inner_function():
        # 3. Local Scope
        local_var = "I am a local variable"
        print("--- Inside inner_function ---")
        print(local_var)       # Accessing local variable
        print(enclosing_var)   # Accessing enclosing variable
        print(global_var)      # Accessing global variable

    print("--- Calling inner_function ---")
    inner_function()
    
    # print(local_var)  # This would cause a NameError because local_var is not in this scope

# 4. Built-in Scope
# Functions like print(), len(), str() are in the built-in scope
print("--- Built-in Scope ---")
print("This is the print() function from the built-in scope.")
print("Length of 'hello':", len("hello"))


print("--- Global Scope ---")
print(global_var)
# print(enclosing_var) # This would cause a NameError
# print(local_var)     # This would cause a NameError

demonstrate_scopes()


# Using 'global' and 'nonlocal' keywords

x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        # To modify the enclosing scope's x, use 'nonlocal'
        # nonlocal x 
        
        # To modify the global scope's x, use 'global'
        # global x
        
        x = "local"
        print("inner:", x)

    inner()
    print("outer:", x)

print("--- 'global' and 'nonlocal' keywords demo ---")
outer()
print("global:", x)

# Example with 'nonlocal'
def outer_nonlocal():
    count = 0
    def inner_increment():
        nonlocal count
        count += 1
        return count
    return inner_increment

incrementer = outer_nonlocal()
print("--- 'nonlocal' example ---")
print(incrementer())
print(incrementer())

# Example with 'global'
global_count = 0
def increment_global():
    global global_count
    global_count += 1
    
print("--- 'global' example ---")
increment_global()
print(global_count)
increment_global()
print(global_count)


# g = 1
# def outer1():
#     g = 2
#     def inner1():
#         global g
#         g = 3
#     inner1()
#     print(g)

# print("outer1", g)  # Output: 1 (global scope)
# outer1()  # Output: 2 (enclosing scope)