#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import chardet
import os
from PIL import Image
from io import BytesIO
import time

def login():
    #发送登录请求的目标地址
    url = 'https://passport.bilibili.com/login/dologin'
    #发送登录请求所需参数
    act = 'login'
    gourl = 'https://passport.bilibili.com/login/dologin'
    keeptime = '2592000'
    userid = '15919959898'
    pwd = ''
    #获取验证码

    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    t = str(int(time.time() * 1000))
    captcha_url = 'https://passport.bilibili.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url)


    i = Image.open(BytesIO(r.content))
    i.show()
    vdcode = input('请手动输入验证码:\n>')
    #获取与验证码同步的cookies
    cookies = dict(r.cookies)
    #封装所需参数
    data = {'act':act,'gourl':gourl,'keeptime':keeptime,'userid':userid,'pwd':pwd,'vdcode':vdcode}
    #伪装成浏览器
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Referer':'https://passport.bilibili.com/login'
}
    #发送请求
    r = requests.post(url,data=data,headers=headers,cookies=cookies)
    #通过返回的html代码判断是否登陆成功
    content = r.content.decode()
    print(content)

if __name__ == '__main__':
    login()
