#!/usr/bin/python
# -*- coding:utf-8 -*- 
import re
import sys
import time
import urlparse
import urllib2 as ulb
from bs4 import BeautifulSoup as bs

reload(sys)
sys.setdefaultencoding('utf-8')

def download(url, proxy=None, num_retries=2):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	print ("Downloading: "+url+"...")
	request = ulb.Request(url=url, headers=headers)
	time.sleep(1)
	#opener = ulb.build_opener()
	try:
		#html = opener.open(request).read()
		html = ulb.urlopen(request).read()
	except ulb.URLError as e:
		print ("Download Error: " + str(e.reason))
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)
	# html = ulb.urlopen(request).read()
	return html

def get_list(article_list, tag_name = None, attr = None):
	list = []
	for tag in article_list:
		if tag.find('img') == None:
			continue
		if attr == None:
			list.append(tag.find(tag_name).string)
		else:
			list.append(tag.find(tag_name)[attr])
	return list

def get_bd_link(link_list):
	href_list = []
	pass_list = []
	for link in link_list:
		html = download(link)
		soup = bs(html, 'lxml')
		print("parsing pan.baidu...")
		str = soup.find('meta',content=re.compile('pan.baidu'))['content']
		print (str)
		try:
			href = re.search(r'http://pan.baidu.com/s/(\S+)',str).group()
		except:
			href = re.search(r'https://pan.baidu.com/s/(\S+)',str).group()
		password = re.search(r'[a-zA-Z0-9]{4}\r',str).group()[:4]
		href_list.append(href)
		pass_list.append(password)
		
	return href_list, pass_list

def write_html(list):
	fout = open('output.html', 'w') 
	fout.write("<html>")
	fout.write("<body>")
	for i in range(10):
		fout.write(u'''
		<article>
			<header>
				<h2 >'''+list[0][i].encode('utf-8')+'''</h2>
				<div> 
				<p>'''+list[1][i]+'''</p>
				</div>
			</header>
			<p style="text-align:center">
				<img src="'''+list[2][i].encode('utf-8')+'''"/>
			</p>
			<footer> 
				<p style="text-align: right"><a href="'''+list[3][i]+'''">'''+list[4][i]+'''</a></p>
			</footer>
		</article>
		''')
	
	fout.write("</body>")
	fout.write("</html>")
	fout.close()

def make_html(list):
	html = "<html>\n"
	html +="<body>\n"
	for i in range(10):
		html += (u'''
		<article>
			<header>
				<h2 >'''+list[0][i].encode('utf-8')+'''</h2>
				<div> 
				<p>'''+list[1][i]+'''</p>
				</div>
			</header>
			<p style="text-align:center">
				<img src="'''+list[2][i].encode('utf-8')+'''"/>
			</p>
			<footer> 
				<p style="text-align: right"><a href="'''+list[3][i]+'''">'''+list[4][i]+'''</a></p>
			</footer>
		</article>
		''')
	
	html +="</body>\n"
	html += "</html>\n"
	return html
	
def get_html():
	url = "https://asina.us/"
	html = download(url)
	if html == None:
		print (u"页面不存在...")
		return None
	soup = bs(html, 'lxml')
	article_list = soup.find_all('article')
	del article_list[0]
	img_list = get_list(article_list, tag_name = 'img', attr = 'src')
	link_list = get_list(article_list, tag_name = 'a', attr = 'href')
	time_list = get_list(article_list, tag_name = 'time')
	title_list = get_list(article_list, tag_name = 'a')
	href_list, pass_list = get_bd_link(link_list)
	list = [title_list, time_list, img_list, href_list, pass_list]
	return make_html(list)
	
def main():
	# 更改默认字符编码
	#reload(sys)
	#sys.setdefaultencoding('utf-8')
	
	# 页面入口
	url = "https://asina.us/"
	
	# 下载, 解析页面
	html = download(url)
	if html == None:
		print (u"页面不存在...")
		return None
	soup = bs(html, 'lxml')
	article_list = soup.find_all('article')
	del article_list[0]
	img_list = get_list(article_list, tag_name = 'img', attr = 'src')
	link_list = get_list(article_list, tag_name = 'a', attr = 'href')
	time_list = get_list(article_list, tag_name = 'time')
	title_list = get_list(article_list, tag_name = 'a')
	href_list, pass_list = get_bd_link(link_list)
	list = [title_list, time_list, img_list, href_list, pass_list]
	write_html(list)

if __name__ == '__main__':
	main()
	
	