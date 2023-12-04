import re
f=open('inputday1.txt')
trans={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
reversedtrans={'eno':'1','owt':'2','eerht':'3','ruof':'4','evif':'5','xis':'6','neves':'7','thgie':'8','enin':'9'}
lines=f.readlines()
f.close()
total=0
for l in lines:
	li = list(re.findall(r'\d+', l))
	nb = int(li[0][0]+li[-1][-1])
	total = total + nb
print('Calibration for Part 1 : '+ str(total))
total=0
for l in lines:
	li = list(re.findall(r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)', l))
	li2 = list(re.findall(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9)', l[::-1]))
	nb2 = int(trans.get(li[0],li[0])+reversedtrans.get(li2[0],li2[0]))
	total = total + nb2
print('Calibration for Part 2 : '+ str(total))
