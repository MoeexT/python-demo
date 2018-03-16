#py -3
#coding: utf-8
import os
from Tkinter import *
from tkMessageBox import *
	
command = 'taskkill /F /IM REDAgent.exe'
os.system(command)
#tkMessageBox.showinfo(title='Fuck RedSpider',message='成功：已终止进程 REDAgent')
root = Tk()
root.withdraw()
showinfo(title = 'Fuck RedSpider', message = '已成功关闭该进程')

	