
import requests

# LINE Notify 權杖
token = 'kkpN8FrEG1wfMoDVc2NbuETr30MlfSs1rLnRh0vX3jR'
# 要發送的訊息
message = '這是test'
# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message ,
         'stickerPackageId': '11539',  # 貼圖編號
         'stickerId': '52114118',  # 貼圖序號
         }
# 以 requests 發送 POST 請求
requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data)

# # 要傳送的圖片檔案
image = open('https://yabeline.tw/Stickers_Data.php?Number=1448326', 'rb')
files = { 'imageFile': image }

