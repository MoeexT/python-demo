#!/usr/bin/python
#coding:utf-8 
import sys 
import smtplib 
import make_html_bs
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText    
 
reload(sys)
sys.setdefaultencoding('utf-8')
# 第三方 SMTP 服务  
mail_host="smtp.sina.com"  #设置服务器  
mail_user="yuwancumiana@sina.cn"    #用户名  
mail_pass="mq2020."   #htdjucacsmbeebhi
  
sender = 'yuwancumiana@sina.cn'  
receivers = ['yuwancumian666@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  

def add_img(src, img_name):
	img = MIMEImage(open(src, 'rb').read(), _subtype='jpg')
	img.add_header('Content-Disposition', 'attachment', filename = img_name)
	return img
	
mail = MIMEMultipart('测试邮件')  
mail['From'] = "yuwancumiana@sina.cn"  
mail['To'] = "鱼丸粗面" 
mail['Subject'] = '福利'
try:
	html = make_html_bs.get_html().encode('utf-8')
except:
	sys.exit(u"加载页面失败...")
message = MIMEText(html, 'html')
mail.attach(message)
#mail.attach(add_img(r'img\girl.jpg', 'Girl'))

try:  

	smtp = smtplib.SMTP_SSL(mail_host, 465)   
	smtp.ehlo() 
	smtp.login(mail_user,mail_pass)    
	smtp.sendmail(sender, receivers, mail.as_string())
	smtp.close()
	print u"邮件发送成功"  
except smtplib.SMTPException,e:  
	print e 