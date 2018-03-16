# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.gmail.com"  #设置服务器
mail_user="yuwancumian666@gmail.com"    #用户名
mail_pass="jpfgqpfxecrqvzca"   #口令 
sender = 'yuwancumian666@gmail.com' 
receivers = ['2506930314@qq.com'] 


message = MIMEText('从windows发来的一封测试信', 'plain', 'utf-8')
message['From'] = "yuwancumian666@gmail.com" 
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