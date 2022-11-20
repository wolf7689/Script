#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
环境变量说明：
export JIKE_COOKIE="网站cookie，分号;隔开" 
cron: 0 0 8 * * *
new Env('极客云签到');
"""

from notify import *
import headers
import requests
import os

ctext = os.getenv("JIKE_COOKIE")
cookies = dict(x.strip().split("=") for x in ctext.split(";") if x)

url = 'https://jike191.com/user/checkin'
# headers = {
#     'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
#     'referer': 'https://jike191.com/user'
#     }

r = requests.post(url, cookies=cookies, headers=headers.headers1)
title = "🐺极客云签到"
context = ""
try:
    response = r.json()
    if(response.get('ret')):
        context = "签到成功 " + response.get('msg')
        print(context)
    else:
        context = "签到失败 " + response.get('msg')
        print(context)
except:
    context = r.text
    print("出错啦！！")
    print(context)
    
send(title, context)
