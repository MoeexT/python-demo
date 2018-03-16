#coding: utf-8
#py -2
import sys
import time
import urllib2 as ulb
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

url = "https://asina.us/"


class article:
	def __init__(title, time, img):
		self.title = title
		self.time = time
		self.img = img

def download(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	req = ulb.Request(url=url, headers=headers)
	html = ulb.urlopen(req).read()
	return html
# 解析页面
html = download(url)
dom = etree.HTML(html)#soup=bs(html,'lxml')
img_list=dom.xpath("//article[@id!='post-676']//p[1]//img[1]/@src")
time_list = dom.xpath("//article[@id!='post-676']//a[@rel='bookmark']//time/text()")
title_list = dom.xpath("//article[@id!='post-676']//h2[@itemprop='name headline']//a/text()")


def make_html(title_list, time_list, img_list):
	fout = open('output.html', 'w') 
	fout.write("<html>")
	fout.write("<body>")
	for i in range(10):
		fout.write(u'''
		<article>
			<header>
				<h2 >'''+title_list[i].encode('utf-8')+'''</h2>
				<div> 
				<p>'''+time_list[i]+'''</p>
				</div>
			</header>
			<p style="text-align:center">
				<img src="'''+img_list[i].encode('utf-8')+'''"/>
			</p>
			<footer> 
				<p style="text-align: right">百度云入口</p>
			</footer>
		</article>
		''')
		#fout.write("<td>%s</td>" % data['url'])
	
	fout.write("</body>")
	fout.write("</html>")

	fout.close()
	
name_list = ["完具", "我是你可爱的小猫", "萌兰酱", "小秋秋",\
 "软萌萝莉小仙", "少女映画", "原来是茜公主殿下", "隔壁小姐姐", "镜颜欢"]
if __name__=='__main__':
	make_html(title_list, time_list, img_list)