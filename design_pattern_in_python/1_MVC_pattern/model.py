import json


class Person(object):
    """Note this object has nothing to do with this program it symbolizes that we
    are inheriting some behaviour in this class. Like we do in django

    """
    def __init__(self, first_name=None, last_name=None):
        self._first_name = first_name
        self._last_name = last_name

    def name(self):
        # return "{} {}".format(self._first_name, self._last_name)
        return f"{self._first_name} {self._last_name}"

    @staticmethod
    def get_all():
        """Return all data in db.txt as a person object"""
        # database = open('db.txt', 'r')
        # dt  = database.read()
        print("some data=", type(dt))
        json_list =[
            {
                "first_name":"ram",
                "last_name":"sharma"
            },
            {
                "first_name": "ram1",
                "last_name": "sharma1"
            }
        ]
        #json.loads(dt)
        result = []
        for item in json_list:
            data = Person(item['first_name'], item['last_name'])
            result.append(data)

        return result







