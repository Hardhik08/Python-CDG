# Multiple inheritance in Python is a feature where a class can inherit from more than one parent class. 
# This allows a class to inherit the properties and methods of multiple classes. 
# In Python, multiple inheritance is achieved using the `class` keyword followed by the class name and a colon,
#  and then a comma-separated list of parent classes. Here's an example of multiple inheritance in Python:

class Animal:
    def speak(self):
        print("Animal speak")
class Dog(Animal):
    def bark(self):
        print('Dog bark')
class Cat(Animal):
    def meow(self):
        print('Cat meow')
    
d = Dog()
d.speak()
d.bark()
c = Cat()
c.speak()
c.meow()
print(Cat())