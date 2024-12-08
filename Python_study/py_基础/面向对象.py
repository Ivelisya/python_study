# self是由当前对象自动传参

class name(object):
    name = 'smzy'
    age = 1
    def get_age(self):
        self.age
        print(self.name)
        
n = name()
n.sex = 'man'
print(name.name)
    