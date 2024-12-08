class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('创造Person')
    def say_age(self):
        print(f"{self.name}的年龄是{self.age}")
class Student(Person):
    def __init__(self,name,age):
        super(Student,self).__init__(name,age)
        
obj = object()  
s1 = Student('mzy',19)
s1.say_age()
print(s1.say_age)