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
mail_host="smtp.gmail.com" 
mail_user="yuwancumian666@gmail.com" 
mail_pass="jpfgqpfxecrqvzca"
  
sender = 'yuwancumian666@gmail.com'  
receivers = ['2506930314@qq.com'] 

def add_img(src, img_name):
	img = MIMEImage(open(src, 'rb').read(), _subtype='jpg')
	img.add_header('Content-Disposition', 'attachment', filename = img_name)
	return img
	
mail = MIMEMultipart('测试邮件')  
mail['From'] = "yuwancumian666@gmail.com"  
mail['To'] = "鱼丸粗面" 
mail['Subject'] = '福利'

message = MIMEText(make_html_bs.get_html().encode('utf-8'), 'html')
mail.attach(message)
#mail.attach(add_img(r'img\girl.jpg', 'Girl'))

try:  

	smtp = smtplib.SMTP(mail_host, 587)   
	smtp.ehlo()
	smtp.starttls()
	smtp.login(mail_user,mail_pass)    
	smtp.sendmail(sender, receivers, mail.as_string())
	smtp.close()
	print u"邮件发送成功"  
except smtplib.SMTPException,e:  
	print e 