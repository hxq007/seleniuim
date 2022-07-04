from selenium import webdriver;


# 基础层 放 selenium原生方法
class BasePage:
    # 初始化方式
    def __init__(self):
        self.d = webdriver.Chrome();
        d = self.d
        self.d.get("https://smpf-dev.gbookchina.com/")
        self.d.maximize_window()

    # 定位元素关键字
    def locator_element(self, loc):
        # print(loc)
        return self.d.find_element(*loc)

    # 设置值的关键字
    def set_keys(self, loc, ia):
        return self.d.find_element(*loc).send_keys(ia)

    # 点击的关键字
    def click_set(self, loc):
        self.d.find_element(*loc).click()

    def get_value(self, loc):
        return self.locator_element(loc).text
