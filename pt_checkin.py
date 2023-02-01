#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
环境变量说明：
export PT_TIME_COOKIE="网站cookie，分号;隔开" 
export HDC_COOKIE="网站cookie" 
export CHD_COOKIE="网站cookie" 
export HDA_COOKIE="网站cookie" 
export HD_TIME_COOKIE="网站cookie" 
export TTG_COOKIE="网站cookie" 
cron: 0 20 8 * * *
new Env('PT签到');
"""

import os
import demjson3
import requests
import requests_html
import headers
from notify import send

def generate_cookies(cookies):
    return dict(x.strip().split("=") for x in cookies.split(";") if x)


def pt_time():
    url = 'https://www.pttime.org/attendance.php'
    session = requests_html.HTMLSession()
    ctext = os.getenv("PT_TIME_COOKIE")
    cookies = generate_cookies(ctext)
    try:
        r = session.get(url, cookies=cookies, headers=headers.headers1)
    except ConnectionResetError:
        return_msg = 'pttime❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        # print(r.text)
        title = r.html.find('title')
        if title:
            if '登录' in title[0].text:
                return_msg = 'pttime❌登录失效'
                print(return_msg)
            else:
                return_msg = 'pttime✔签到成功'
                print(return_msg)
        else:
            print(r.text)
            return_msg = 'pttime签到失败，请查看日志'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'pttime签到失败'
        print(return_msg)
    return return_msg


def hd_china():
    main_url = 'https://hdchina.org/'
    url = 'https://hdchina.org/plugin_sign-in.php?cmd=signin'
    session = requests_html.HTMLSession()
    ctext = os.getenv("HDC_COOKIE")
    cookies = generate_cookies(ctext)
    try:
        r = session.get(main_url, cookies=cookies, headers=headers.headers2)
    except ConnectionResetError:
        return_msg = 'hdchina❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        title = r.html.find('title')
        if title:
            if 'Login' in title[0].text:
                return_msg = 'hdchina❌登录失效'
                print(return_msg)
            else:
                csrf = r.html.find('meta[name="x-csrf"]')[0].attrs['content']
                # print(csrf)
                payload = {'csrf': csrf}
                r = session.post(url, cookies=cookies, headers=headers.headers2, data=payload)

                if r.status_code == requests.codes.ok:
                    print(r.json())
                    return_msg = 'hdchina✔签到成功'
                    print(return_msg)
                else:
                    return_msg = 'hdchina签到失败'
                    print(return_msg)
        else:
            print(r.text)
            return_msg = 'hdchina签到失败，请查看日志'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'hdchina签到失败'
        print(return_msg)
    return return_msg


def chd():
    url = 'https://chdbits.co/bakatest.php'
    session = requests_html.HTMLSession()
    ctext = os.getenv("CHD_COOKIE")
    cookies = generate_cookies(ctext)
    try:
        r = session.get(url, cookies=cookies, headers=headers.headers1)
    except ConnectionResetError:
        return_msg = 'chd❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        # print(r.text)
        title = r.html.find('title')
        if title:
            if '登录' in title[0].text:
                return_msg = 'chd❌登录失效'
                print(return_msg)
            else:
                question_id = r.html.find('input[name="questionid"]')[0].attrs['value']
                payload = {
                    'questionid': question_id,
                    'choice[]': 1,
                    'usercomment': '此刻心情:无',
                    'wantskip': '不会'
                }
                r = session.post(url, cookies=cookies, headers=headers.headers1, data=payload)
                if r.status_code == requests.codes.ok:
                    # print(r.text)
                    return_msg = 'chd✔签到成功'
                    print(return_msg)
                else:
                    print(r.status_code)
                    return_msg = 'chd签到失败'
                    print(return_msg)
        else:
            print(r.text)
            return_msg = 'chd签到失败，请查看日志'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'chd签到失败'
        print(return_msg)
    return return_msg


def hd_area():
    url = 'https://www.hdarea.co/sign_in.php'
    session = requests_html.HTMLSession()
    ctext = os.getenv("HDA_COOKIE")
    cookies = generate_cookies(ctext)
    payload = {'action': 'sign_in'}
    try:
        r = session.post(url, cookies=cookies, headers=headers.headers1, data=payload)
    except ConnectionResetError:
        return_msg = 'hdarea❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        print(r.text)  # 纯文本
        if len(r.html.find('title')) > 0:
            return_msg = 'hdarea❌登录失效'
            print(return_msg)
        else:
            return_msg = 'hdarea✔签到成功'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'hdarea签到失败'
        print(return_msg)
    return return_msg


def hd_time():
    url = 'https://hdtime.org/attendance.php'
    session = requests_html.HTMLSession()
    ctext = os.getenv("HD_TIME_COOKIE")
    cookies = generate_cookies(ctext)
    try:
        r = session.get(url, cookies=cookies, headers=headers.headers1)
    except ConnectionResetError:
        return_msg = 'hdtime❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        # print(r.text)
        title = r.html.find('title')
        if title:
            if '登录' in title[0].text:
                return_msg = 'hdtime❌登录失效'
                print(return_msg)
            else:
                return_msg = 'hdtime✔签到成功'
                print(return_msg)
        else:
            print(r.text)
            return_msg = 'hdtime签到失败，请查看日志'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'hdtime签到失败'
        print(return_msg)
    return return_msg


def ttg():
    main_url = 'https://totheglory.im/'
    url = 'https://totheglory.im/signed.php'
    session = requests_html.HTMLSession()
    ctext = os.getenv("TTG_COOKIE")
    cookies = generate_cookies(ctext)
    try:
        r = session.get(main_url, cookies=cookies, headers=headers.headers1)
    except ConnectionResetError:
        return_msg = 'ttg❌网络不通'
        print(return_msg)
        return return_msg

    if r.status_code == requests.codes.ok:
        r.encoding = 'utf-8'
        # print(r.text)
        title = r.html.find('title')
        if title:
            if '登录' in title[0].text:
                return_msg = 'ttg❌登录失效'
                print(return_msg)
            else:
                json_text = r.text.split('$.post("signed.php", {')[1].split('},', 1)[0]
                print(json_text)
                payload = demjson3.decode('{' + json_text + '}')
                r = session.post(url, cookies=cookies, headers=headers.headers1, data=payload)

                if r.status_code == requests.codes.ok:
                    r.encoding = 'utf-8'
                    print(r.text)  # 纯文本
                    return_msg = 'ttg✔签到成功'
                    print(return_msg)
                else:
                    print(r.status_code)
                    return_msg = 'ttg签到失败'
                    print(return_msg)
        else:
            print(r.text)
            return_msg = 'ttg签到失败，请查看日志'
            print(return_msg)
    else:
        print(r.status_code)
        return_msg = 'ttg签到失败'
        print(return_msg)
    return return_msg


if __name__ == '__main__':
    ln = '\n'
    title = '🐺pt签到'
    context = ln
    context = context + pt_time() + ln
    context = context + hd_china() + ln
    context = context + chd() + ln
    context = context + hd_area() + ln
    context = context + hd_time() + ln
    context = context + ttg() + ln
    send(title, context)
