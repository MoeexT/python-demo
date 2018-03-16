#coding:utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
# 第三方 SMTP 服务  
mail_host="smtp.sina.com"  #设置服务器  
mail_user="yuwancumiana@sina.cn"    #用户名  
mail_pass="mq2020."   #htdjucacsmbeebhi
  
  
sender = 'yuwancumiana@sina.cn'  
receivers = ['yuwancumian666@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  
  
mail = MIMEText('这是一封TLS加密了的测试邮件', 'plain', 'utf-8')  
mail['From'] = "yuwancumiana@sina.cn"  
mail['To'] =  Header("鱼丸粗面", 'utf-8')  
  
subject = '邮件测试'  
mail['Subject'] = Header(subject, 'utf-8')
  
try:  
	'''
	  smtpObj = smtplib.SMTP_SSL(mail_host, 465)   
	  smtpObj.login(mail_user,mail_pass)    
	  smtpObj.sendmail(sender, receivers, mail.as_string())  
	  smtpObj.quit()  
	'''
	smtp = smtplib.SMTP(mail_host, 25)
	smtp.set_debuglevel(True)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(mail_user, mail_pass)
	smtp.sendmail(sender, receivers, mail.as_string())
	smtp.close()
	print u"邮件发送成功"  
except smtplib.SMTPException,e:  
	print e 