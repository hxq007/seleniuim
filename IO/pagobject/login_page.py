import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


# 页面对象层  放置页面的元素和页面的动作

class LoginPage(BasePage):
    # 页面的元素

    # 登录账号
    username = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
    # 登录密码
    password = (By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/input')
    # 点击登录按钮
    submit = (By.XPATH, '//*[@id="app"]/div/div[2]/form/button/span')

    quit_test =(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/a/li/span')
    # 页面的动作

    def login_ecshop(self,username,password):
        # 继承 基础层 的element函数，传入对应的xpath
        self.set_keys(LoginPage.username,username)
        time.sleep(2)
        self.set_keys(LoginPage.password,password)
        time.sleep(2)
        self.click_set(LoginPage.submit)
        time.sleep(5)

    def assert_test(self):
        self.click_set(LoginPage.quit_test)
        time.sleep(4)
        print("傻逼")

