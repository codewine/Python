
'''
解读Python发送邮件

解读Python发送邮件

Python发送邮件需要smtplib和email两个模块。也正是由于我们在实际工作中可以导入这些模块，才使得处理工作中的任务变得更加的简单。今天，就来好好学习一下使用Python发送邮件吧。

SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

1.邮件正文是文本的格式

复制代码
 1 # -*- coding: UTF-8 -*-
 2
 3 from email.mime.multipart import MIMEMultipart
 4 from email.mime.text import MIMEText
 5 import smtplib
 6 import sys
 7 import csv
 8 import xlrd
 9 from pyExcelerator import *
10 import os
11 import xlwt
12 from xlutils.copy import copy
13 import pyExcelerator
14 import datetime
15 import time
16
17 reload(sys)
18 sys.setdefaultencoding("utf-8")
19
20 mailto_list = [""]  # 邮件接收方的邮件地址
21 mail_host = "smtp.exmail.qq.com"    # 邮件传送协议服务器
22 mail_user = ""  # 邮件发送方的邮箱账号
23 mail_pass = ""  # 邮件发送方的邮箱密码
24
25 def send_mail(to_list, sub, content):
26     me = "天才白痴梦"+"<"+mail_user+">"
27     msg = MIMEText(content, _subtype='plain', _charset='utf-8')
28     msg['Subject'] = sub    # 邮件主题
29     msg['From'] = me
30     msg['To'] = ";".join(to_list)
31     try:
32         server = smtplib.SMTP()
33         server.connect(mail_host)
34         server.login(mail_user, mail_pass)
35         server.sendmail(me, to_list, msg.as_string())
36         server.close()
37         return True
38     except Exception, e:
39         print str(e)
40         return False
41
42 if __name__ == '__main__':
43     sub = "天才白痴梦"
44     content = '...'
45     if send_mail(mailto_list, sub, content):
46         print "发送成功"
47     else:
48         print "发送失败"
复制代码
2.邮件正文是表格的格式：由于是表格，所以我们选择HTML来实现表格的功能，邮件上面显示的就是HTML实现的内容了。

复制代码
 1 # -*- coding: UTF-8 -*-
 2
 3 from email.mime.multipart import MIMEMultipart
 4 from email.mime.text import MIMEText
 5 import smtplib
 6 import sys
 7 import csv
 8 import xlrd
 9 from pyExcelerator import *
10 import os
11 import xlwt
12 from xlutils.copy import copy
13 import pyExcelerator
14 import datetime
15 import time
16
17 reload(sys)
18 sys.setdefaultencoding("utf-8")
19
20 mailto_list = [""]  # 邮件接收方的邮件地址
21 mail_host = "smtp.exmail.qq.com"    # 邮件传送协议服务器
22 mail_user = ""  # 邮件发送方的邮箱账号
23 mail_pass = ""  # 邮件发送方的邮箱密码
24
25 def send_mail(to_list, sub, content):
26     me = "天才白痴梦"+"<"+mail_user+">"
27     # 和上面的代码不同的就是，这里我们选择的是html 的格式
28     msg = MIMEText(content, _subtype='html', _charset='utf-8')
29     msg['Subject'] = sub    # 邮件主题
30     msg['From'] = me
31     msg['To'] = ";".join(to_list)
32     try:
33         server = smtplib.SMTP()
34         server.connect(mail_host)
35         server.login(mail_user, mail_pass)
36         server.sendmail(me, to_list, msg.as_string())
37         server.close()
38         return True
39     except Exception, e:
40         print str(e)
41         return False
42
43 if __name__ == '__main__':
44     sub = "天才白痴梦"
45     html = '<html></html>'
46     if send_mail(mailto_list, sub, html):
47         print "发送成功"
48     else:
49         print "发送失败"
复制代码
3.邮件正文是图片的格式：要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

复制代码
 1 def send_mail(to_list, sub, content):
 2     me = "天才白痴梦"+"<"+mail_user+">"
 3
 4     msg = MIMEMultipart()
 5     msg['Subject'] = sub    # 邮件主题
 6     msg['From'] = me
 7     msg['To'] = ";".join(to_list)
 8
 9     txt = MIMEText("天才白痴梦", _subtype='plain', _charset='utf8')
10     msg.attach(txt)
11
12     # <b>：黑体  <i>：斜体
13     msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<img alt="" src="cid:image1" />good!', 'html', 'utf-8')
14     msg.attach(msgText)
15
16     file1 = "F:\\1.jpg"
17     image = MIMEImage(open(file1, 'rb').read())
18     image.add_header('Content-ID', '<image1>')
19     msg.attach(image)
20
21     try:
22         server = smtplib.SMTP()
23         server.connect(mail_host)
24         server.login(mail_user, mail_pass)
25         server.sendmail(me, to_list, msg.as_string())
26         server.close()
27         return True
28     except Exception, e:
29         print str(e)
30         return False
31
32 if __name__ == '__main__':
33     sub = "天才白痴梦"
34     html = '<html></html>'
35     if send_mail(mailto_list, sub, html):
36         print "发送成功"
37     else:
38         print "发送失败"
复制代码
4.发送邮件附件：邮件附件是图片

复制代码
 1 def send_mail(to_list, sub, content):
 2     me = "天才白痴梦"+"<"+mail_user+">"
 3
 4     msg = MIMEMultipart()
 5     msg['Subject'] = sub    # 邮件主题
 6     msg['From'] = me
 7     msg['To'] = ";".join(to_list)
 8
 9     txt = MIMEText("天才白痴梦", _subtype='plain', _charset='utf8')
10     msg.attach(txt)
11
12     # # <b>：黑体  <i>：斜体
13     # msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<img alt="" src="cid:image1" />good!', 'html', 'utf-8')
14     # msg.attach(msgText)
15     #
16     # file1 = "F:\\1.jpg"
17     # image = MIMEImage(open(file1, 'rb').read())
18     # image.add_header('Content-ID', '<image1>')
19     # msg.attach(image)
20
21     att = MIMEText(open('F:\\1.jpg', 'rb').read(), 'base64', 'utf-8')
22     att["Content-Type"] = 'application/octet-stream'
23     att["Content-Disposition"] = 'attachment; filename="1.jpg"'
24     msg.attach(att)
25
26     try:
27         server = smtplib.SMTP()
28         server.connect(mail_host)
29         server.login(mail_user, mail_pass)
30         server.sendmail(me, to_list, msg.as_string())
31         server.close()
32         return True
33     except Exception, e:
34         print str(e)
35         return False
复制代码
5.发送群邮件：同时发送给多人

1 mailto_list = [""]  # 邮件接收方的邮件地址
上面这一行代码是邮件接收方的邮件地址，如果我们需要给多人发送邮件的话，就只需要把对方的邮件帐号绑在这一个列表里就ok了。

加密SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

方法：只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。

1 smtp_server = 'smtp.qq.com'
2 smtp_port = 25    # 默认端口号为25
3 server = smtplib.SMTP(smtp_server, smtp_port)
4 server.starttls()
5 # 剩下的代码和前面的一模一样:
6 server.set_debuglevel(1)     # 打印出和SMTP服务器交互的所有信息


'''