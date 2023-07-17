from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("This should now go!")

myObj = Car()
myObj.go()
