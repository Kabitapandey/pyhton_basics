class Calculation1:
    def add(self,a,b):
        return a+b


class Calculation2:
    def multiply(self,a,b):
        return a*b

class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
# issubclass
print(issubclass(Derived,Calculation1))
print(issubclass(Calculation1,Calculation2))
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Derived))

# is instance
c=Calculation1()
d=Derived()
print(isinstance(c,Derived))
print(isinstance(d,Calculation1))
print(isinstance(d,Calculation1))
print(isinstance(d,Derived))