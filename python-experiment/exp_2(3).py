# ! py -3
# -*- coding: utf8 -*-


import random


guess = 0
secret = random.randint(0, 100)
times = 1
max_times = 10

print("-----------------欢迎参加猜数字游戏，请开始-------------------")
for i in range(9, -1, -1):
    guess = int(input("@数字区间0-100，请输入你猜的数字："))
    print("你猜的数字是：", guess)
    if guess == secret:
        print("你猜了{}次，猜对了，好腻害".format(times))
        break
    elif guess < secret:
        print("你猜的数字小于正确答案, 还剩{}次机会".format(i))
    else:
        print("你猜的数字大于正确答案, 还剩{}次机会".format(i))

    times += 1

print("游戏结束")
