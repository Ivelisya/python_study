import math

def calculate_states(a, b, c):
    """
    目标：针对输入的三个数字，求三个数字的均值、方差、标准差

    Args:
        a: 第一个数字。
        b: 第二个数字。
        c: 第三个数字。

    Returns:
        返回均值、方差、标准差
    """
    mean = (a + b + c) / 3
    variance = ((a - mean)**2 + (b - mean)**2 + (c - mean)**2) / 3
    standard_deviation = math.sqrt(variance)
    return mean, variance, standard_deviation

if __name__ == "__main__":
    # 获取输入的三个数字
    while True:
        try:
            a = float(input("请输入第一个数字："))
            b = float(input("请输入第二个数字："))
            c = float(input("请输入第三个数字："))
            break  # 输入正确，跳出循环
        except ValueError:
            print("输入的数字有误，请重新输入")

    mean, variance, standard_deviation = calculate_states(a, b, c)

    # 打印结果,保留两位小数
    print(f"均值为: {mean:.2f}")
    print(f"方差为: {variance:.2f}")
    print(f"标准差为: {standard_deviation:.2f}")