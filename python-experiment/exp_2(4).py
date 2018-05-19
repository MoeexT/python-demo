# ! py -3
# -*- coding: utf8 -*-


import random


def guess_secret(max_times):
	guess = 0
	secret = random.randint(0, 100)
	times = 1
	print("-----------------欢迎参加猜数字游戏，请开始-------------------")
	for i in range(max_times - 1, -1, -1):
		try:
			guess = int(input("@数字区间0-9，请输入你猜的数字："))
		except:
			print("输入格式有误！！！")
			exit()
		print("你猜的数字是：", guess)
		if guess == secret:
			print("你猜了{}次，猜对了，好腻害".format(times))
			break
		elif guess < secret:
			print("你猜的数字小于正确答案, 还剩{}次机会".format(i))
			if i == 0:
				print("你始终没有猜对，游戏失败\n正确答案是：", secret)
		else:
			print("你猜的数字大于正确答案, 还剩{}次机会".format(i))
			if i == 0:
				print("你始终没有猜对，游戏失败\n正确答案是：", secret)

		times += 1

	print("游戏结束")


if __name__ == "__main__":
	try:
		maxts = eval(input("@请输入猜数字的最大次数："))
	except:
		print("输入格式有误！！！")
	guess_secret(maxts)
