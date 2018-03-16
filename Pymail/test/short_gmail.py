#coding:utf-8
import smtplib
GMAIL_USERNAME = "yuwancumian666@gmail.com"
GMAIL_PASSWORD = "jpfgqpfxecrqvzca"#yuwancumian666
recipient = "2506930314@qq.com"
email_subject = "Python"
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
headers = "\r\n".join(["from: " + GMAIL_USERNAME,
			"subject: " + email_subject,
			"to: " + recipient,
			"mime-version: 1.0",
			"content-type: text/html"])
 
body_of_email = "gmail!!"
content = headers + "\r\n\r\n" + body_of_email
session.sendmail(GMAIL_USERNAME, recipient, content)