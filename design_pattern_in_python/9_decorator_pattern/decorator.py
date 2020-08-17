"""
author: Bhoj Bahadur Karki
Date: 2020-August-15th
Description: Decorator design pattern

Decorator pattern allows a user to add new functionality to an existing object
without altering its structure. This type of design pattern comes under structural
pattern as this pattern acts as a wrapper to existing class.

This pattern creates a decorator class, which wraps the original class and provides additional
functionality keeping the class methods signature intact.

The motive of a decorator pattern is to attach additional responsibilities of an object dynamically.

How to implement decorator design pattern
The code mentioned below is a simple demonstration of how to implement decorator design pattern in Python.
The illustration involves demonstration of a coffee shop in the format of class. The coffee
class created is an abstract, which means that it cannot be instantiated

"""

import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class AbstractCoffee:
    def get_ingridents(self):
        pass

    def get_price(self):
        pass

    def get_taxes(self):
        return 0.1 * self.get_price()


class ConcreteCoffee(AbstractCoffee):
    def get_ingridents(self):
        return 'coffee'

    def get_price(self):
        return 100


@six.add_metaclass(ABCMeta)
class AbstractCoffeeDecorator(AbstractCoffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_ingridents(self):
        return self.decorated_coffee.get_ingridents()

    def get_price(self):
        return self.decorated_coffee.get_price()


class Suger(AbstractCoffeeDecorator):
    def get_ingridents(self):
        return self.decorated_coffee.get_ingridents() + " ,suger"

    def get_price(self):
        return self.decorated_coffee.get_price() + 25


class Milk(AbstractCoffeeDecorator):
    def get_ingridents(self):
        return self.decorated_coffee.get_ingridents() + " ,milk"

    def get_price(self):
        return self.decorated_coffee.get_price() + 75


class Vanilla(AbstractCoffeeDecorator):
    def get_ingridents(self):
        return self.decorated_coffee.get_ingridents() + " ,vanilla"

    def get_price(self):
        return self.decorated_coffee.get_price() + 200


