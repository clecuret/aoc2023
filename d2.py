import re
f=open('inputday2.txt')
lines=f.readlines()
f.close()
total=total2=0
idgame=0
for l in lines:
	idgame=idgame+1
	maxred=maxblue=maxgreen=0
	games=l.split(':')[1].split(';')
	ok=True
	for g in games:
		li = list(re.findall(r'(green|red|blue|\d+)', g))
		for idx, item in enumerate(li):
			if idx % 2 == 1:
				maxred = int(li[idx-1]) if (item=='red' and int(li[idx-1])>maxred) else maxred
				maxblue = int(li[idx-1]) if (item=='blue' and int(li[idx-1])>maxblue) else maxblue
				maxgreen = int(li[idx-1]) if (item=='green' and int(li[idx-1])>maxgreen) else maxgreen
				if (item=='red' and int(li[idx-1])>12) or (item=='green' and int(li[idx-1])>13) or (item=='blue' and int(li[idx-1])>14):
					#print(l)
					ok=False
	if ok:
		total=total+idgame
	puissance=maxred*maxblue*maxgreen
	total2=total2+puissance
print('Solution for Part 1 : '+ str(total))
print('Solution for Part 2 : '+ str(total2))

