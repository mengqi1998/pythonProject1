# #更新yum源
# cat > /etc/yum.repos.d/gitlab-ce.repo <<EOF
# [gitlab-ce]
# name=Gitlab CE Repository
# baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el\$releasever/
# gpgcheck=0
# enabled=1
# EOF
#
# #安裝
# yum clean all && yum makecache
# sudo yum install gitlab-ce        #自動安裝最新版
# sudo yum install gitlab-ce-x.x.x    #安裝指定版本
#
# #配置啟動
# # 1.修改gitlab配置檔案指定為安裝gitlab伺服器ip和自定義埠： vim /etc/gitlab/gitlab.r
# # 2.重置並啟動GitLab
# # 執行：
# gitlab-ctl reconfigure
# gitlab-ctl restart
# # 初始賬戶: root 密碼: 5iveL!fe
#
# # 自定義密碼：
# gitlab-rails console production     #開始初始化密碼
# u=User.where(id:1).first        來查詢與切換賬號（User.all 可以檢視所有使用者）
#
# u.password=12345678  設定密碼
# u.password_confirmation=12345678
# u.save!
# exit
#
#





##############################################################################
##############################################################################
##############################################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://gas.goodlife.tw/")  # 更改網址以前往不同網頁
now_gas = driver.find_element(by=By.ID, value='cpc')
predict = driver.find_element(by=By.CLASS_NAME, value='up')

print(predict.text)
print(now_gas.text)
driver.quit()
#add column

import requests as req
from urllib import parse

evt = 'test'   # 事件名稱
key = 'b-Lz1dFuvX_oHp4iURBg1r'
val1 = predict.text  # value1參數值
val2 = now_gas.text  # value2參數值
url = (f'https://maker.ifttt.com/trigger/{evt}' +
       f'/with/key/{key}?value1={val1}&value2={val2}')

r = req.get(url)  # 執行IFTTT平台的webhooks
r.text   # 取得IFTTT的回應
