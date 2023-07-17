from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    def getText(self):
        return ("I am a vehicle.")
    
class Car(Vehicle):
    
    def go(self):
        print("This should now go!")

myObj = Car()
print(myObj.getText())
myObj.go()
