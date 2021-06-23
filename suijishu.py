import random

a = random.randint(0,200)
i = 0
c = 5000
while i <= 20:
    if c < 500:
        break
    b = input("请输入您要猜的数字：")
    b = int(b)
    if b > a:
        print("大了！")
        c = c - 500
    elif b < a:
        print("小了！")
        c = c - 500
    else:
        print("恭喜您，猜中数字，本次幸运数字为：",b,"您一共猜了：",i+1,"次。","您还有金币：",c+1000)
        break
    i = i + 1