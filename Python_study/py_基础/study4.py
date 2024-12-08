class Student():
    count = 0
    def __init__(self, name, score):
        self.name = name#新增name属性
        self.score = score#新增score属性

    @classmethod
    def a(cls):
        cls.count += 1
        print(cls.count)
    @staticmethod
    def b(c,d):
        print(f'{c} + {d} = {c + d}')
    def say_score(self):
        # print(f"分数是{self.name},姓名是{self.score}")
        #__init__初始化方法 系统默认提供无参的构造方法
        self.age = 18
    def __del__(self):
        print(f'销毁对象{self}')
e = Student(1,2)
f = Student(1,2)
# print(e.name,e.score,e.height)
print('程序结束')
del e