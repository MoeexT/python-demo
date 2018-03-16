#coding:utf-8

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.sina.com'
SMTP_PORT = 25
sender = 'yuwancumiana@sina.cn' 
recipient = 'yuwancumian666@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'Python 附件'
msg['To'] = recipient
msg['From'] = sender
subject = 'Python annex'

img = MIMEImage(open(r'img/girl.jpg', 'rb').read(), _subtype='jpg')
img.add_header('Content-Disposition', 'attachment', filename = 'Girl.jpg')
msg.attach(img)

part = MIMEText(open('test.txt','rb').read(), 'plain')
# part["Content-Type"] = 'application/octet-stream'
part["Content-Disposition"] = 'attachment; filename="test.txt"'
part.set_payload("text annex")
msg.attach(part)
try:
	session = smtplib.SMTP()
	session.connect(SMTP_SERVER, 25)
	'''
	session.ehlo()
	session.starttls()
	session.ehlo()
	'''
	session.login(sender, 'mq2020.')
	session.sendmail(sender, recipient, msg.as_string())
	print u'发送成功'
	session.quit()
except smtplib.SMTPException,e:  
	print e 
