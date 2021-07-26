from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class Action():
    def __init__(self):
    # 初始化配置
        self.desired_caps = {
            "deviceName": "ANP4C20410008147",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        # 设置滑动初始坐标和滑动距离
        self.start_x = 500
        self.start_y = 1500
        self.distance = 1300
    def comments(self):
        sleep(3)
        # app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(272, 970)], 200)  # appium中模拟手指点击方法，叫tap，有两个参数，元素位置和点击持续时间ms
    def scroll(self):
        # 无限滑动
        while True:
            # 模拟滑动
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance,300)
            # TouchAction(self.driver).press(x=390, y=1399).move_to(x=438, y=441).release().perform()
            # 设置延时等待
            sleep(10)
    def main(self):
        self.comments()
        self.scroll()
if __name__ == '__main__':
    action = Action()
    action.main()