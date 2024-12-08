class benz:pass
class bmw:pass
class CarFactory:
    __obj = None
    __init_flag = True
    
    def __new__(cls,*args, **kwargs):
        if cls.__obj == None:
            cls.__obj = super().__new__(cls)
        return cls.__obj
    
    def __init__(self,name):
        if self.__init_flag:
            self.name = name 
            self.__init_flag = False
    def CarCreater(self,name):
        if name == '宝马':
            return bmw()
        if name == '奔驰':
            return benz()
a = CarFactory()
c1 = a.CarCreater('宝马')
print(c1)