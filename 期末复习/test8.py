month = int(input("请输入月份"))
if month == 5:
    print("这个月有年会")
    day = int(input("请输入日期"))
    if day == 20:
        print("年会将于今天进行")
    elif day > 20:
        print("年会已经结束")
    elif day < 20:
        remain_day = 20 - day
        print(f"年会还有 {remain_day}天进行")
