def fun(num):
    n_min = 500 #最大值
    n_max = 0
    if num > 0:
        try:
            for i in range(0,num):
                n = int(input())
                if n > 500:
                    raise ValueError("输入的数字超出范围 (<= 500)")
                if n > n_max:
                    n_max = n
                if n < n_min:
                    n_min = n
        except ValueError as e:
            print(f"输入错误：{e}")
        dict1 = {}
        dict1["NUM_max"] = n_max
        dict1['NUM_min'] = n_min
        print(dict1)
num_count = int(input("NUM="))
fun(num_count)

