import time
import os
import random
import webbrowser as web
count = 20
j = 0
while j < count:
    i = 0
    while i <= 8:
        web.open_new_tab('https://m.weibo.cn/1797131247/4301198158585325')  # 网址替换这里
        i = i + 1
        time.sleep(3)  # 这个时间根据自己电脑处理速度设置，单位是s
    else:
        time.sleep(10)
        os.system('taskkill /F /IM chrome.exe')  # google浏览器，其他的更换下就行
        # print 'time webbrower closed'

    j = j + 1

import requests

for i in range(1, 10):
    proxies = {
        "http": "http://61.164.252.106:139"
    }
    url = "https://mp.weixin.qq.com/s/rz7eRPiGktxEFY_g-oOWGw"
    print(url)
    req = requests.get(url)
    # 设置编码
    req.encoding = 'utf-8'
    # print(req.text)
