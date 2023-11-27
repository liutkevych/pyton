import random


class Hat:

    houses = ['Lviv', 'Krakow', 'New York', 'London']

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Alex")