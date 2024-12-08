class A():
    def __init__(self):
        print('a的构造方法')
    def say(self):
        print('say AAA')
class B(A):
    def __init__(self):
        super(B,self).__init__()
        print('这是b的构造方法')
    def say(self):
        super(B,self).say()
        print('say BBB')
a = B()
a.say()