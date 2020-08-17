"""
author: Bhoj Bahadur Karki
Date: 2020-August-12th
Description: Factory design pattern
The factory pattern comes under the creational patterns list category.
It provides one of the best ways to create an object.
In factory pattern, objects are created without exposing the logic to
client and referring to the newly created object using a common interface.

Factory patterns are implemented in Python using factory method. When a
user calls a method such that we pass in a string and the return value as a
new object is implemented through factory method. The type of o
"""


class Button(object):
    html = "<button></button>"

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Card(Button):
    html = "<obj></obj>"


class ButtonFactory:

    def create_button(self, typ):
        # Note we need to capitalize() because we are passing values in lower case
        # print("gob=", globals())
        # print("gob type=", type(globals()[typ.capitalize()]))
        return globals()[typ.capitalize()]()


btn = ButtonFactory()
input_list = ['image', 'input', 'card']
for b in input_list:
    t = btn.create_button(b).get_html()
    print(t)
