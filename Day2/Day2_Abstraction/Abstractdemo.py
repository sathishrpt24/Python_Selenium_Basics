from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def area(side):
        pass;
    @abstractmethod
    def circumference(side):
        pass;

class B(A):
    def __init__(self,side):
        self.side = side;
        print("constructor: Initializing the side values: ",self.side);
    def area(self):
        return self.side*self.side
    def circumference(self):
        return self.side*4

b = B(5);
Area = b.area()
Circum = b.circumference()
print("Area: ",Area)
print("Circum: ",Circum)