# import copy
# class MobilePhone:
#     def __init__(self,cpu):
#         self.cpu = cpu
# class CPU:
#     pass
# c = CPU()
# m = MobilePhone(c)
# print('浅拷贝')

# m2 = copy.copy(m)
# print(id(m))
# print(id(m2))
# print(id(m.cpu))
# print(id(m2.cpu))
# m3 = copy.deepcopy()    