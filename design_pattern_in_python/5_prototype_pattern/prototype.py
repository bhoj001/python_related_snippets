"""
author: Bhoj Bahadur Karki
Date: 2020-August-12th
Description: Prototype design pattern
Prototype design pattern helps to hide the complexity of the instances created by the class.
The concept of the existing object will differ with that of the new object,
which is created from scratch.

The newly copied object may have some changes in the properties if required.
This approach saves time and resources that go in for the development of a product.

"""

import copy


class Prototype:
    _type = None
    _value = None

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value

    def clone(self):
        pass


class Type1(Prototype):
    def __init__(self, value):
        self._type = "type1"
        self._value = value

    def clone(self):
        return copy.copy(self)


class Type2(Prototype):
    def __init__(self, value):
        self._type = "type2"
        self._value = value

    def clone(self):
        return copy.copy(self)


class ObjectFactory:
    __type1value1 = None
    __type1value2 = None
    __type2value1 = None
    __type2value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1value1 = Type1(1)
        ObjectFactory.__type1value2 = Type1(2)
        ObjectFactory.__type2value1 = Type2(1)
        ObjectFactory.__type2value2 = Type2(2)

    @staticmethod
    def get_type1_value1():
        return ObjectFactory.__type1value1.clone()

    @staticmethod
    def get_type1_value2():
        return ObjectFactory.__type1value2.clone()

    @staticmethod
    def get_type2_value1():
        return ObjectFactory.__type2value1.clone()

    @staticmethod
    def get_type2_value2():
        return ObjectFactory.__type2value2.clone()


def main():
    print("starting main")

    # initialize and call method
    ObjectFactory.initialize()

    obj = ObjectFactory.get_type1_value1()
    print(f"type= {obj.get_type()}, value = {obj.get_value()}")

    obj = ObjectFactory.get_type1_value2()
    print(f"type= {obj.get_type()}, value = {obj.get_value()}")

    obj = ObjectFactory.get_type2_value1()
    print(f"type= {obj.get_type()}, value = {obj.get_value()}")

    obj = ObjectFactory.get_type2_value2()
    print(f"type= {obj.get_type()}, value = {obj.get_value()}")

    print("thanks")


if __name__ == "__main__":
    main()
