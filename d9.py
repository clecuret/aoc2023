f=open('inputday9.txt')
lines=f.readlines()
f.close()
total=0
total2=0
for l in lines:
	alls=[]
	data=[*map(int,l.split())]
	curr=data
	while not all(el==0 for el in curr):
		differences = [b - a for a, b in zip(curr, curr[1:])]
		alls.append([curr[-1], curr[0]])
		curr=differences
	total += sum(d[0] for d in alls)
	total2 += sum(d[1]* (-1)**(idx+2) for idx,d in enumerate(alls))

print('Solution for Part 1 : %s' % total)
print('Solution for Part 2 : %s' % total2)
