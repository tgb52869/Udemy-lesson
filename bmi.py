height = input("身高(公尺) ")
weight = input("體重(公斤) ")
height = float(height)
weight = float(weight)
bmi = weight / height ** 2
bmi = float(bmi)

if bmi >= 35 : 
	print("重度肥胖") 
elif bmi >= 30 and bmi < 35 : 
	print("中度肥胖") 
elif bmi >= 27 and bmi < 30 : 
	print("輕度肥胖") 
elif bmi >= 24 and bmi < 27 : 
	print("過重") 
elif bmi >= 18.5 and bmi < 24 : 
	print("正常") 
elif bmi < 18.5 : 
	print("過輕")
