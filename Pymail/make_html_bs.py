#! python2
# -*- coding:utf-8 -*- 
import re
import sys
import time
import datetime
# import urlparse
import urllib2 as ulb
from datetime import date
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
		try:
			print (str)
		except:
			print ("can't parse the BaiduDisk Link")
		try:
			href = re.search(r'http://pan.baidu.com/s/(\S+)',str).group()
		except:
			href = re.search(r'https://pan.baidu.com/s/(\S+)',str).group()
		password = re.search(r'[a-zA-Z0-9]{4}\r',str).group()[:4]
		href_list.append(href)
		pass_list.append(password)
		
	return href_list, pass_list

	
def make_html(list):
	#html = "<html>\n"
	#html +="<body>\n"
	#print ("total return "+str(len(list[0]))+" links")
	html = ''
	for i in range(len(list[0])):
		try:
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
		except:
			continue
	
	#html += "</body>\n"
	#html += "</html>\n"
	return html
	
def get_html():
	length = 0
	HTML = ''
	for  index in range(1,3):
		url = "http://adb123.com/page/"+str(index)# asina.us
		html = download(url)
		if html == None:
			print (u"page not exist...")
			return None
		soup = bs(html, 'lxml')
		article_list = soup.find_all('article')
		del article_list[0]
		
		for i,j in enumerate(article_list):
			string = j.find('time').string
			date_ = time.strptime(string, '%Y-%m-%d')
			article_date = date(date_[0], date_[1], date_[2])
			target_date = date.today() - datetime.timedelta(2)
			if article_date == target_date:
				article_list = article_list[:i]
		length += len(article_list)
		img_list = get_list(article_list, tag_name = 'img', attr = 'src')
		link_list = get_list(article_list, tag_name = 'a', attr = 'href')
		time_list = get_list(article_list, tag_name = 'time')
		title_list = get_list(article_list, tag_name = 'a')
		href_list, pass_list = get_bd_link(link_list)
		list = [title_list, time_list, img_list, href_list, pass_list]
		HTML += make_html(list)
	print ('Finally got '+str(length)+' links')
	return HTML

if __name__ == '__main__':
	html = get_html()
	fout = open('output.html', 'w') 
	fout.write(html)
	fout.close()
	
	
