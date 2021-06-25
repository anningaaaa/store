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
    ["机械革命",13500],
    ["熟食",11]
]
while True:
    chose = input("请输入业务编号(1:恭喜中奖  2：对不起，您没中奖）:")
    if chose == "1":
        index = random.randint(0,len(you) - 1 )
        print("恭喜您抽中了",you[index],"优惠券")
        c = you[index]
    elif chose == "2":
        print("对不起，您没中奖")
    elif chose == "q" or chose == "Q":
        print("欢迎下次抽奖！")
        break
    else:
        print("输入非法，请重新输入！")

money = input("请输入您的钱包余额:")
money = int(money)
mycart = []
while True:
    for index,value in enumerate(shop):
        print(index,"\t\t",value)
    chose = input("请输入您要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                if you[0][0] == shop[0][0]:
                    money = money - you[0][1]
                else:
                    money = money - shop[chose][1]
                print("恭喜，成功添加购物车，您的余额还剩：￥",money)
            else:
                print("对不起，您的余额不足！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，商品不存在！")

# 打印小票
print("下面是您的购物小条，请拿好：")
for  index,value in enumerate(mycart):
    print(index,"\t\t",value)
print("您的钱包还剩：￥",money)
