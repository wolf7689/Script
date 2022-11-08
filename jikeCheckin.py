#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
环境变量说明：
export JIKE_COOKIE="网站cookie，分号;隔开" 
cron: 0 0 8 * * *
new Env('极客云签到');
"""

import requests
import os

cookies = {}
ctext = os.getenv("JIKE_COOKIE")
ctext_a = ctext.split(";")

for c in ctext_a:
    kv = c.split("=")
    if len(kv) > 1:
        cookies[kv[0].strip()] = kv[1].strip()

url = 'https://jike191.com/user/checkin'

r = requests.post(url, cookies=cookies)
try:
    response = r.json()
    if(response.get('ret')):
        print("签到成功")
        print(response.get('msg'))
    else:
        print("签到失败")
        print(response.get('msg'))
except:
    print("出错啦！！")
    print(r.text)
