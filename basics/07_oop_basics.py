# Sample: Python OOP Basics

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Encapsulation
class Person:
    def __init__(self, name):
        self._name = name  # _name is 'protected'
    def get_name(self):
        return self._name

animal = Animal("Generic Animal")
dog = Dog("Rex")
person = Person("Alice")

animal.speak()
dog.speak()
print("Person's name:", person.get_name())
