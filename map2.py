# Map class written for day 3 (abandonded)


class Map2:

    def __init__(self):
        print("map created")
        self.m = {}

    def add(self, key, value):
        if key in self.m:
            self.m[key].append(value)
        else:
            self.m[key] = [value]

    def get(self):
        return self.m

    def __str__(self):
        return str(self.m)

    def __repr__(self):
        return "\n" + str(self.m)
