phone_dict = {
    '华为':{'型号':'pura','价格':'4999'},
    '小米':{'型号':'xiaomi 14 pro','价格':'4699'}
}
def show_memu():
    print("*"*30)
    print("*** 手机数据存储系统 ***")
    print("1.添加手机信息")
    print("2.保存手机信息")
    print("3.显示所有数据")
    print("*"*30)
def get_select():
    while True:
        try:
            select_num = int(input("请输入选择的序号"))
            return select_num
        except:
            print("输入无效，请输入数字序号")
def add_phone_data():
    brand = input("添加数据，请输入要添加的数据,品牌:")
    model = input("要添加的手机型号")
    price = input("价格:")
    phone_dict['brand'] = {'型号':model,'价格':price}
    print("数据添加成功")
def show_phone_data():
    print("当前的手机数据又:")
    if not phone_dict:
        print("当前没有数据")
    for brand,info in phone_dict:
        print(f"品牌:{brand},型号:{info.get('型号'),'价格':{info.get('价格')}}")
def save_to_file(filename = "backup.data"):
    try:
        with open(filename,"w",encoding='utf-8') as f:
            f.write(str(phone_dict))
        print("数据已经成功保存")
    except:
        print("保存文件时出现错误")

if __name__ == "__main__":
    while True:
        show_memu()
        num = get_select()
        if num == 1:
            add_phone_data()
        elif num == 2:
            save_to_file()
        elif num == 3:
            show_phone_data()
        else:
            print("无效的序号，请重新输入")



