# This is a single inheritance example in Python. It demonstrates how a class can inherit from another class.
#  In this example, the `Car` class inherits from the `Vehicle` class.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
class Car(Vehicle):
    def __init__(self,model,make,year):
        print("Car constructor called")
        print("Maker",make)
        print("Year",year)
        print("Model",model)

v = Car("Nano","Tata",2018)
# print(v)


        