"""
author: Bhoj Bahadur Karki
Date: 2020-August-15th
Description: Adapter design pattern
Adapter pattern works as a bridge between two incompatible interfaces.
This type of design pattern comes under structural pattern as this pattern combines the
capability of two independent interfaces.

This pattern involves a single class, which is responsible to join functionalities of independent
or incompatible interfaces. A real life example could be the case of a card reader, which acts as
an adapter between memory card and a laptop. You plug in the memory card into the card reader and
the card reader into the laptop so that memory card can be read via the laptop.

The adapter design pattern helps to work classes together. It converts the interface of a class
into another interface based on requirement. The pattern includes a speciation a polymorphism which
names one name and multiple forms. Say for a shape class which can use as per the requirements gathered.

There are two types of adapter pattern −

Object Adapter Pattern
This design pattern relies on object implementation. Hence, it is called the Object Adapter Pattern.

Class Adapter Pattern
This is an alternative way to implement the adapter design pattern. The pattern can be implemented
using multiple inheritances.
"""


class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# adaptee

class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

class USASocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

# this is the adaptor pattern

class Adaptor(USASocketInterface):
    def __init__(self, interface):
        self.__interface = interface

    def voltage(self):
        return 110

    def live(self):
        return self.__interface.live()

    def neutral(self):
        return self.__interface.neutral()

# client
class ClientElectricKettle:
    def __init__(self, obj):
        self.__power = obj

    def boil(self):
        if self.__power.voltage() > 110:
            print("Too hot")
        elif self.__power.live() == 1 and self.__power.neutral() == -1:
            print("Coffee time")
        else:
            print("No power")


if __name__ == "__main__":

    socket = Socket()
    adaptor = Adaptor(socket)

    client = ClientElectricKettle(adaptor)
    client.boil()

    print("end")
