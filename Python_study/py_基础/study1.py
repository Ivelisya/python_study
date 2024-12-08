class Employee():
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    @classmethod
    def b(cls):
        cls.count += 1
        print(cls.count)
    @staticmethod
    def c(d,e):
        print(f'{d} + {e} = {d+e}')    
    @property
    def salary(self):
        print(f"薪资是{self.__salary}")
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if 1 < salary <100000:
            self.__salary = salary
        else:
            print('错误')
a = Employee(1,1)
a.salary = 10000
Employee.b()
a.c(1,2)