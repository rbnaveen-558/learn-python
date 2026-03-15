# d:\work\python\basics\utils	ools.py

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        return a / b

