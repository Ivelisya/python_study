import re
trs  =[1,2,3,4,5]
for index, tr in enumerate(trs):
    print(index)
# enumerate 中加迭代器
print(re.findall('[a-z]','AaBb',flags= re.I))