x = 2
while True:
	if x >= 0:
		password = input('請輸入密碼:')
		if password == 'IAisadorable':
			print('成功登入!歡迎進入本系統!')
			break
		else:
			print('密碼錯誤! 還有', x, '次機會')
			x = x-1
	else:
		print('您已超過3次錯誤,禁止進入!')
		break
	