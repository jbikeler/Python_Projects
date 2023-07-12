
#make class with general info about vehicles
class vehicle:
    year = 0
    make = ""

#Make a car class that inherits vehicle and contains speed in mph and tire type
class car(vehicle):
    tireType = ""
    mphSpeed = 0

#Make a plane class that inherits vehicle and contains speed in knots and cargo type
class plane(vehicle):
    cargoType = ""
    knots = 0
