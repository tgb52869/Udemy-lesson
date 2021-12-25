i = 3 #三次機會
while True:
    password = input('請輸入密碼: ')
    if password == 'a123456':
    	print("登入成功")
    	break
    elif password != "a123456":
    	i = i - 1
    	print("密碼錯誤! 還有", i, "次機會")
    elif i == 0:
    	print("帳號鎖定")
    	break





