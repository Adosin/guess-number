# 產生一個隨機整數 1 ~ 100
# 讓使用者"重複(迴圈的意思)"數字去猜
# 猜對的話, 印出"終於猜對啦!"
# 猜錯的話, 要告訴使用者答案大小

import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這次你猜得第', count, '次') 
		break
	elif num > r:
		print('數字大於答案')
	elif num < r: 
		print('數字小於答案')
	print('這次你猜得第', count, '次') 
