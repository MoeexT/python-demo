# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.sina.com"  #设置服务器
mail_user="yuwancumiana@sina.cn"    #用户名
mail_pass="mq2020."   #口令 
sender = 'yuwancumiana@sina.cn' 
receivers = ['yuwancumian666@gmail.com'] 


message = MIMEText('从windows发来的一封测试信', 'plain', 'utf-8') # 这里指定邮件内容
message['From'] = "yuwancumiana@sina.cn" 
message['To'] =  "鱼丸粗面"  #receiver's name could be customized
subject = '测试' #title
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException as e:
    print "Error: cannot send my email"
    print e