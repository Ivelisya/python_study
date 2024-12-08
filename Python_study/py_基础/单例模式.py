class Singleton():
    __obj = None
    __init_flag = True
    
    def __new__(cls,*args, **kwargs):
        if cls.__obj == None:
            cls.__obj = super().__new__(cls)
        return cls.__obj
    
    def __init__(self,name):
        if Singleton.__init_flag:
            Singleton.name = name 
            Singleton.__init_flag = False
a = Singleton('aa')
print(a.name)
b = Singleton('bb')
print(b.name)
object