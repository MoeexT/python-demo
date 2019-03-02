#!/usr/bin/python
#coding:utf-8 
import sys 
import smtplib 
import traceback
import make_html_bs
from email.header import Header
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
receivers = ['yuwancumian666@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 ,'2535257276@qq.com','635936876@qq.com' 

def add_img(src, img_name):
	img = MIMEImage(open(src, 'rb').read(), _subtype='jpg')
	img.add_header('Content-Disposition', 'attachment', filename = img_name)
	return img
	
mail = MIMEMultipart("mixed")  
mail['From'] = "yuwancumiana@sina.cn"  
mail['To'] = "鱼丸粗面" 
mail['Subject'] = Header('福利','utf-8')
message = MIMEText("今日福利(windows)", 'plain', 'utf-8')
mail.attach(message)
try:
	html = make_html_bs.get_html().encode('utf-8')
except Exception as e:
	print traceback.print_exc()
	sys.exit(u"loading pages failed...")
HTML = MIMEText(html, _subtype='html', _charset='utf-8')
mail.attach(HTML)
#mail.attach(add_img(r'cat.jpg', 'cat'))

try:  

	smtp = smtplib.SMTP()
	smtp.connect(mail_host)
	smtp.login(mail_user, mail_pass)    
	smtp.sendmail(sender, receivers, mail.as_string())
	smtp.close()
	print u"send mail success"  
except smtplib.SMTPException,e:
	print e 
