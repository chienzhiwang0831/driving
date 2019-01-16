country = input('請問你哪裡人: ')
age = int(input('請輸入你的年紀: '))
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
else:
	print('沒這國家"你這笨蛋!')