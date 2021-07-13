from threading import Thread
import time
bread = 0
money = 3000
class Cook(Thread):
    cook = ""
    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                bread = bread + 1
                print(self.cook,"造了一个面包，还剩",bread,"个面包。")
            else:
                time.sleep(3)
                if bread <= 500:
                    continue
                else:
                    break
class Customer(Thread):
    customer = ""
    def run(self) -> None:
        global money
        global bread
        while True:
            if bread == 0:
                time.sleep(3)
            else:
                money = money - 3
                bread = bread - 1
                print(self.customer, "买了一个面包，还剩", money, "元，",bread,"个面包")
                if money <= 3000:
                    break
                else:
                    continue


u1 = Cook()
u2 = Cook()
u3 = Cook()
u1.cook = "厨师1号"
u2.cook = "厨师2号"
u3.cook = "厨师3号"
u1.start()
u2.start()
u3.start()

c1 = Customer()
c2 = Customer()
c3 = Customer()
c4 = Customer()
c5 = Customer()
c1.customer = "安宁"
c2.customer = "安宁宁"
c3.customer = "安宁宁宁"
c4.customer = "安宁宁宁宁"
c5.customer = "安宁宁宁宁宁"
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()








