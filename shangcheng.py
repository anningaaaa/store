import random
shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13],
    ["可乐",10],
    ["薯片",5.5],
    ["炸鸡",18],
    ["熟食",16]
]
you = [
    ["机械革命", 13500],
    ["HUAWEI watch", 1080],
    ["MAC PC", 11700],
    ["Iphone 54 plus", 40500],
    ["辣条", 2.5],
    ["老干妈", 11],
    ["可乐", 9],
    ["薯片", 5],
    ["炸鸡", 16],
    ["熟食", 11]
]
while True:
    b = input("请输入业务编号(1:恭喜中奖  2：对不起，您没中奖）:")
    if b == "1":
        index = random.randint(0,len(you) - 1 )
        print("恭喜您抽中了",you[index][0],"优惠券")
    elif b == "2":
        print("对不起，您没中奖")
    elif b == "q" or b == "Q":
        print("欢迎下次抽奖！")
        break
    else:
        print("输入非法，请重新输入！")
# 2.初始化您的余额
money = input("请输入您的钱包余额:")
money = int(money)



# 3.准备一个空的购物车
mycart = []

# 买东西
quan = int(input("请选择您的优惠券："))
while True:
    # 展示商品
    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        print(index,"\t\t",value)
    # 请输入您要的商品
    chose = input("请输入您要的商品：")
    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if you[quan][0] == shop[chose][0]:
            shop[chose][1] == you[quan][1]
            print(shop[chose][1] == you[quan][1])
        else:
            shop[chose][1] == shop[chose][1]
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            # 看钱是否足够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                # 钱减去
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车，您的余额还剩：￥",money)
            else:
                print("对不起，您的余额不足，请到商城去购买！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")

# 打印小票
print("下面是您的购物小条，请拿好：")
for index,value in enumerate(mycart):
    print(index,"\t\t",value)
print("您的钱包还剩：￥",money)