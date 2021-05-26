class Parent:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def getName(self):
        return self.name

    def getName(self):
        return self.height


class Child(Parent):
    def __init__(self, name, height, weight):
        super().__init__(name, height)
        self.weight = weight

    def getWeight(self):
        return self.weight


child = Child('Kabita', '5', '54')
print("Name=", child.name, "\t", "Height=",
      child.height, "\t", "Weight=", child.weight)
