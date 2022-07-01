##  unittest 

1. unittest ：命令行运行    main方法运行
2. 使用方式
   - 新建一个类继承 unittest TestCase   Testcase(unittest.TestCase) 
   - 导入unittest   import unittest 
   - 以test开头的方法名   def test_01_login(self)
3. 命令行运行：python - m unittest 模块名.py.类名.方法名
4. main方法运行：配置环境   写在另外一个文件内，写在文件内，需要配置环境。

### unittest 的原理

### selenium 定位 下拉列表

~~~python
        from select import select
	    from selenium.webdriver.support.select import Select
        #通过Xpath定位元素
        d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div/input').click()
        time.sleep(1)
        d.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        time.sleep(1)
        d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input')
        # 通过文本选择下拉内容
        set = select(d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div/input').click())
        select(set).select_by_visible_text('ICCID')
~~~

### selenium 文件上传 

~~~python
d.find_element(By.XPATH, '').send_keys(R"文件路径")#R代表真实路径
~~~

### selenium处理弹窗

~~~python
#处理弹出窗口 ：alert 只有确定   confirm 有确认和取消      prompt 有确定有有取消还可以输入值
ale = d.switch_to.alert
ale.dismiss   #取消
ale.accept  #确认 
ale.send_seys #输入值
ale.text  #获得文本
~~~

### 自动化设计模式  

#### pom模式和关键字驱动模式

#### pom 模式  page object model 页面对象模式 

**好处**

1. 解决线性脚本问题
2. 代码重复利用问题
3. 后期维护

pom分三层

1. 基础层  base主要放sselenium原生方法
2. 页面对象层 ：放置页面的元素和页面的动作 psgeobject 
3. 测试用例层：testcase 存放测试用例以及测试数据
4. 测试对象层调用基础层的方法，测试用例调用页面对象层的方法

基础层

 ~~~python
 from selenium import webdriver;
 
 
 # 基础层 放 selenium原生方法
 class BasePage:
     # 初始化方式
     def __init__(self):
         self.d = webdriver.Chrome();
         d = self.d
         self.d.get("https://smpf-dev.gbookchina.com/")
         self.d.maximize_window()
 
     def locator_element(self, loc):
         # print(loc)
         arr = self.d.find_element(*loc)
         return arr
 
 ~~~

基础层改良版

~~~python
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
        arr = self.d.find_element(*loc)
        return arr

    # 设置值的关键字
    def set_keys(self, loc, ia):
        arr = self.d.find_element(*loc).send_keys(ia)
        return arr
    # 点击的关键字
    def click_set(self,loc):
        self.d.find_element(*loc).click()
~~~



页面对象层  

~~~python
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
    # 页面的动作
    def login_ecshop(self):
        # 继承 基础层 的element函数，传入对应的xpath
        self.locator_element(LoginPage.username).send_keys("admin123")
        time.sleep(2)
        self.locator_element(LoginPage.password).send_keys("wmzsgg123")
        time.sleep(2)
        self.locator_element(LoginPage.submit).click()
        time.sleep(5)
~~~

页面对象层改良版

~~~python
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
    # 页面的动作
    def login_ecshop(self,username,password):
        # 继承 基础层 的element函数，传入对应的xpath
        self.set_keys(LoginPage.username,username)
        time.sleep(2)
        self.set_keys(LoginPage.password,password)
        time.sleep(2)
        self.click_set(LoginPage.submit)
        time.sleep(5)
~~~



测试用例层

~~~python

# 测试用例层 存放测试用例或者测试数据
import unittest

from pagobject.login_page import LoginPage


class TestCasset(unittest.TestCase):
    # 调用对象  pagobject.login_page import LoginPage
    def test_01_login(self):
        la = LoginPage()
        la.login_ecshop("admin123","wmzsgg123")

~~~

