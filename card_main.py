import card_tools

while True:
    # TODO 显示提示菜单
    card_tools.show_menu()
    action_str = input("请输入要执行的操作:")
    print("执行的操作是:%s" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            card_tools.add_card()
        elif action_str == "2":
            card_tools.show_cards()
        else:
            card_tools.search_card()
        pass
    elif action_str == "0":
        print("欢迎再次使用!")
        break
        # pass
    else:
        print("输入错误,请重新输入!")
