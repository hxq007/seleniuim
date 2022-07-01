import time
import unittest
from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver;
from selenium.webdriver.common.by import By


class Testcase(unittest.TestCase):

    def test_01_login(self):
        d = webdriver.Chrome();

        d.get("https://smpf-dev.gbookchina.com/")

        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys("admin123")
        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("wmzsgg123")
        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button/span').click()
        time.sleep(4)
        d.quit()
    def test_02_select_list(self):
        '''查询iccid'''

        d = webdriver.Chrome();

        d.get("https://smpf-dev.gbookchina.com/")

        d.maximize_window()


        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys("admin123")
        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("wmzsgg123")
        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button/span').click()
        time.sleep(1)
        #点击SIM卡列表
        d.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/a/li').click()
        time.sleep(3)
        # 点击检索项目
        '''d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div/input').click()
        time.sleep(1)
        d.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        time.sleep(1)
        d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input')
        set = select(d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div/input').click())
        select(set).select_by_visible_text('ICCID')'''


    def test_04_delete_prod(self):
        d = webdriver.Chrome();

        d.get("https://smpf-dev.gbookchina.com/")

        time.sleep(1)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys("admin123")
        time.sleep(0)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("wmzsgg123")
        time.sleep(0)
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button/span').click()

        #进入SIM卡申请页面
        d.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/a/li/span').click()






if __name__ == '__main__':
    print("这是main方法")
    unittest.main()