class Calculation1:
    def add(self,a,b):
        return a+b


class Calculation2:
    def multiply(self,a,b):
        return a*b

class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b

d=Derived()
print(d.add(10,20))
print(d.multiply(5,10))
print(d.divide(4,2))