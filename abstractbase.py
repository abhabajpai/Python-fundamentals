from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square=Square(4)
print(square.area())
# this code will not compile since Shape has abstract methods without
# method definitions in it
