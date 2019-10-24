#car has states and behaviours
#class holds behaviour and states


class Car:
    '''this is a car class'''

    # __init__ is special function, that creates objects states
    # self represent this object(car)

    def __init__(self, color, height, cost, wheels, speed, name):
        self.wheels = wheels # save wheels to self
        self.color = color
        self.height = height
        self.cost = cost
        self.speed = speed
        self.name = name

    # behaviours/ function
    def move(self):
        print("the car is moving slowly")
        print("the car has", self.wheels, "wheels")
        print("the color is", self.color)
        print("the car will cost", self.cost, "kes")

    def carry(self):
        print("the car is carrying some passengers")

    def hooting(self):
        print("the car is not hooting")

    def racing(self):
        print("the car is speeding at", self.speed, "km/hr")

    def brand(self):
        print("the car type is", self.name)

carobject = Car("silver", 5.5, 40000, 4, 80, "rolce royce")
carobject.move()
carobject.carry()
carobject.hooting()
carobject.racing()
carobject.brand()