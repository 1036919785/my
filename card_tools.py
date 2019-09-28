card_list = []


def show_menu():
    """
    系统菜单
    """
    print("*" * 50)
    print("欢迎使用此系统 v1.0")
    # print("")
    print("1-新增名片")
    print("2-显示全部")
    print("3-搜索名片")
    print("")
    print("0-退出系统")
    print("*" * 50)


def add_card():
    """
    新增名片
    :return:
    """
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    email_str = input("请输入emaill:")

    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    card_list.append(card_dict)

    print(card_list)

    print("新增 %s 用户成功" % name_str)


def show_cards():
    """
    显示全部
    """
    print("-" * 50)
    print("显示全部")

    if len(card_list) == 0:
        print("没有名片信息!")
        return

    for name in ["姓名","qq","phone","email"]:
        print(name,end="\t\t")
    print("")
    print("="*50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """
    搜索名片
    :return:
    """
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要查找的名片:")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了%s" % find_name)
            print(card_dict)
            # TODO 找到后需要执行的操作
            break

    else:
        print("没有找到%s" % find_name)