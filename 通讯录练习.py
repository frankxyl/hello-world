contacts = {}

while True:
    print("\n1.添加  2.查找  3.删除  4.全部  5.退出")
    op = input("请选择操作：")

    if op == "1":
        name = input("姓名：")
        tel = input("电话：")
        contacts[name] = tel
        print("添加成功")

    elif op == "2":
        name = input("查找姓名：")
        print(contacts.get(name, "未找到该联系人"))

    elif op == "3":
        name = input("删除姓名：")
        if name in contacts:
            del contacts[name]
            print("删除成功")
        else:
            print("不存在该联系人")

    elif op == "4":
        if not contacts:
            print("通讯录为空")
        else:
            for n, t in contacts.items():
                print(f"{n} : {t}")

    elif op == "5":
        print("退出程序")
        break
    else:
        print("输入有误，请重新选择")