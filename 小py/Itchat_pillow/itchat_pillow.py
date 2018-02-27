from numpy import *
import itchat
import urllib
import requests
import os
from PIL import Image
from os import listdir
import math

# 微信扫描登录
itchat.auto_login(hotReload=True)

# 获取微信好友列表
friends = itchat.get_friends(update=True)[0:]

user = 'images'
if os.path.exists(user) == False:
    os.mkdir(user)

# 爬取微信好友头像图片，下载保存到本地
num = 1
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(user + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

pics = listdir(user)

# 微信好友个数
numPic = len(pics)
print(numPic)

# 微信好友头像缩小后，每个头像的大小
eachsize = int(math.sqrt(float(640 * 640) / numPic))

print(eachsize)

# 每行头像的个数
numline = int(640 / eachsize)

toImage = Image.new('RGB', (640, 640))

print(numline)

x = 0
y = 0

for i in pics:
    # 打开图片
    try:img = Image.open(user + "/" + i)

    except IOError:
        print("Error: 没有找到文件或读取文件失败"+i)
    else:
        #缩小图片
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        #拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1

    # 保存图片
    toImage.save(user + ".jpg")
    # 并发送到手机
    itchat.send_image(user + ".jpg", 'filehelper')