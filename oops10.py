class Vehicle:
    fuelcap=90
class newvehicle(Vehicle):
    fuelcap=80
    def display(self):
        print("fuel cap from the vehicle class",super().fuelcap)
        print("fuel cap from the car class",self.fuelcap)
obj1= newvehicle()
obj1.display()
#calling the parent class methods
class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
#using with initializer
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
