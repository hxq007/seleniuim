
# 测试用例层 存放测试用例或者测试数据
import unittest

from pagobject.login_page import LoginPage


class TestCasset(unittest.TestCase):
    # 调用对象  pagobject.login_page import LoginPage
    def test_01_login(self):
        la = LoginPage()
        la.login_ecshop("admin123","wmzsgg123")
        print("w hsi quan die ")
