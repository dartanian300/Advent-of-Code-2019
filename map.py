# Map class written for day 3


class Map:
    m = {}

    def __init__(self):
        print("map created")

    def add(self, key, value):
        if key in self.m:
            self.m[key].add(value)
        else:
            self.m[key] = {value}

    def __str__(self):
        return str(self.m)
