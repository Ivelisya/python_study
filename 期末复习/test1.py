import math
# 寻找10 到 100 之间的所有素数
for i in range(10,101):
    flag = 0
    for j in range(2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)