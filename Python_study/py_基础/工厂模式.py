class benz:pass
class bmw:pass
class CarFactory:
    def CarCreater(self,name):
        if name == '宝马':
            return bmw()
        if name == '奔驰':
            return benz()
a = CarFactory()
c1 = a.CarCreater('宝马')
print(c1)