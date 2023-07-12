#make class with general info about vehicles
class vehicle:
    year = 0
    make = ""

    #print default warning in console
    def getTopSpeed(self):
        print("Default value. Needs override")

#Make a car class that inherits vehicle and contains speed in mph and tire type
class car(vehicle):
    tireType = ""
    mphSpeed = 100

    #print speed in console but format it for a car
    def getTopSpeed(self):
        print("This car has a speed of " + str(self.mphSpeed) + " mph")

#Make a plane class that inherits vehicle and contains speed in knots and cargo type
class plane(vehicle):
    cargoType = ""
    knots = 400

    #print speed in console but format it for a plane
    def getTopSpeed(self):
        print("This plane has a speed of " + str(self.knots) + " knots")

myPlane = plane()
myCar = car()

myPlane.getTopSpeed()
myCar.getTopSpeed()
