#! python3
# -*- coding:utf-8 -*- 

import time
import urllib.request as ulb
from bs4 import BeautifulSoup as bs

def download(url, proxy=None, num_retries=2):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	print ("Downloading: "+url+"...")
	request = ulb.Request(url=url, headers=headers)
	time.sleep(1)
	try:
		html = ulb.urlopen(request).read()
	except ulb.URLError as e:
		print ("Download Error: " + str(e.reason))
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)
	return html
	
def getList():
	url = 'http://s.weibo.com/top/summary?cate=realtimehot'
	html = download(url)
	soup = bs(html, 'lxml')
	plist = soup.find_all('p',class_='star_name')
	list = []
	for tag in plist:
		list.append(tag.contents[1].string)
		
	return list
	
if __name__ == '__main__':
	list = []
	for i in range(10):
		list = list + getList()
		list.append('\n')
	
	with open('hotWords.txt', 'w') as f:
		for word in list:
			f.write(word+'\n')

			



