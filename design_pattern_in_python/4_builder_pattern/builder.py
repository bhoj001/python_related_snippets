"""
author: Bhoj Bahadur Karki
Date: 2020-August-12th
Description: Builder design pattern
Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.

Advantages of Builder Pattern
It provides clear separation and a unique layer between construction and representation of a specified object created by class.

It provides better control over construction process of the pattern created.

It gives the perfect scenario to change the internal representation of objects.

"""


class Builder:
    """
    This is like an abstract class
    """

    def get_wheel(self): pass

    def get_body(self): pass

    def get_engine(self): pass


class JeepBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 34
        return wheel

    def get_engine(self):
        eng = Engine()
        eng.horsepower = 770
        return eng

    def get_body(self):
        body = Body()
        body.shape = "Range Rover"
        return body


class Director:
    __builder = None

    def __init__(self, b):
        self.__builder = b

    def get_car(self):
        car = Car()

        car.set_body(self.__builder.get_body())
        # car.set_wheel(self.__builder.get_wheel())
        car.set_engine(self.__builder.get_engine())

        # set wheel
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.set_wheel(wheel)
            i += 1

        return car


# This one is our main product
class Car:
    _body = None
    _engine = None
    _wheels = list()

    def set_body(self, body):
        self._body = body

    def set_engine(self, eng):
        self._engine = eng

    def set_wheel(self, wh):
        self._wheels.append(wh)

    def get_specification(self):
        print(f"body shape = {self._body.shape}")
        print(f"engine horsepower= {self._engine.horsepower}")
        print(f"wheel size = {self._wheels[0].size}")


class Wheel:
    size = None


class Body:
    shape = None  # e.g SUV


class Engine:
    horsepower = None


if __name__ == "__main__":
    print("jeep")
    builder = JeepBuilder()
    director = Director(builder)

    jeep = director.get_car()  # return an instance
    jeep.get_specification()
    print("thanks")
