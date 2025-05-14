from math import sqrt

for i in range(2, 51):  # 从2开始循环，排除1
    flag = 0
    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
