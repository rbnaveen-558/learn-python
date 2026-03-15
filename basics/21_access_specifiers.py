# Sample: Python Access Specifiers (Emulated)

class MyClass:
    def __init__(self):
        # 1. Public attribute
        self.public_attribute = "I am public"
        
        # 2. Protected attribute (by convention, single underscore)
        self._protected_attribute = "I am protected"
        
        # 3. Private attribute (name mangling, double underscore)
        self.__private_attribute = "I am private"

    def public_method(self):
        print("This is a public method.")
        print("It can access all attributes:")
        print(f"  - public: {self.public_attribute}")
        print(f"  - protected: {self._protected_attribute}")
        print(f"  - private: {self.__private_attribute}")
        self.__private_method()

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")


# Subclass to demonstrate access from derived classes
class MySubclass(MyClass):
    def access_attributes_from_subclass(self):
        print("--- Accessing from Subclass ---")
        print(f"Can access public attribute: {self.public_attribute}")
        print(f"Can access protected attribute: {self._protected_attribute}")
        
        # Accessing private attribute will raise an AttributeError
        try:
            print(self.__private_attribute)
        except AttributeError as e:
            print(f"Cannot directly access private attribute: {e}")
            
        # Calling methods
        self.public_method()
        self._protected_method()
        # self.__private_method() # Would also cause an AttributeError


# --- Object Instantiation and Access ---

obj = MyClass()

print("--- Accessing from outside the class (via object) ---")

# 1. Public access
print(f"Public attribute: {obj.public_attribute}")
obj.public_method()

# 2. Protected access (possible, but not recommended by convention)
print(f"Protected attribute (not recommended): {obj._protected_attribute}")
obj._protected_method()

# 3. Private access (will fail due to name mangling)
try:
    print(obj.__private_attribute)
except AttributeError as e:
    print(f"Cannot access private attribute directly: {e}")

# We can still access the "mangled" name, but this is strongly discouraged.
# The name is changed to _ClassName__attributeName
print(f"Accessing mangled private attribute: {obj._MyClass__private_attribute}")


sub_obj = MySubclass()
sub_obj.access_attributes_from_subclass()
