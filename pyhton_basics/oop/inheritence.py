class Parent:
    firstname = "Kabita"
    age = 21


class Child(Parent):
    height = 6


child = Child()
print('Kabita is', child.height)
