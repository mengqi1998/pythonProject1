import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests as req

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://gas.goodlife.tw/")  # 更改網址以前往不同網頁
now_gas = driver.find_element(by=By.ID, value='cpc')
predict = driver.find_element(by=By.CLASS_NAME, value='up')

print(predict.text)
print(now_gas.text)
driver.quit()

# from urllib import parse
evt = 'test'   # 事件名稱
key = 'b-Lz1dFuvX_oHp4iURBg1r'
val1 = predict.text  # value1參數值
val2 = now_gas.text  # value2參數值
url = (f'https://maker.ifttt.com/trigger/{evt}' +
       f'/with/key/{key}?value1={val1}&value2={val2}')

r = req.get(url)  # 執行IFTTT平台的webhooks
r.text   # 取得IFTTT的回應


