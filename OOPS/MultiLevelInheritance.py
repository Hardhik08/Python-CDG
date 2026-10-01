# This is a multi-level inheritance example in Python.
#  It demonstrates how a class can inherit from another class, and that class can then inherit from another class.

class Grandparent:
    def __init__(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        
        print("This is Parent class")
class Child(Parent):
    def __init__(self):
        super().__init__()
        
        print("This is child class")

c = Child()    