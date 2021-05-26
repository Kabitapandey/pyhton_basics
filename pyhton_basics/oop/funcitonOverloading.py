class Calculator:
    def add(self, a=5, b=0, c=0, d=0):
        return a+b+c+d


calc = Calculator()
print(calc.add())
print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))
