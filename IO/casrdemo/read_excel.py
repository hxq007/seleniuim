from selenium import webdriver;
from selenium.webdriver.common.by import By

d = webdriver.Chrome();

d.get("https://smpf-dev.gbookchina.com/")

d.find_element(By.xpath,'//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys("admin123");

d.find_element(By.xpath,'//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("wmzsgg123");
 
d.find_element(By.xpath,'//*[@id="app"]/div/div[2]/form/button/span').click();