"""
author: Bhoj Bahadur Karki
Date: 2020-August-12th
Purpose: singleton design pattern: This pattern restricts the instantiation of
a class to one object. It is a type of
creational pattern and involves only one class to create methods and specified objects.

"""


class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        print(self)
        print("type = ", type(self))
        if Singleton.__instance is not None:
            # exit(0)
            raise Exception("Singleton class !Can't create multiple objects!")

        else:

            Singleton.__instance=self


s = Singleton()
print(s)

s = Singleton.get_instance()
print(s)

s = Singleton.get_instance()
print(s)

s = Singleton.get_instance()
print(s)

# This creation will throw error.
# s = Singleton()
# print(s)