class Parent:
    def name(self):
        print("Kabita Panday")

class Derived(Parent):
    def name(self):
        super().name()
        print("Bijay Panday")

d=Derived()
d.name()
