class Employee:
    __count = 0

    def __init__(self):
        Employee.__count = Employee.__count+1

    def display(self):
        print('No of employees:', Employee.__count)


em = Employee()


try:
    print(em.__count)

finally:
    em.display()
