import re
f=open('inputday4.txt')
lines=f.readlines()
f.close()
scores = {}
counts = [1] * len(lines)
total=0
for lid,l in enumerate(lines):
	wins, card = map(set, map(str.split, l.split(":")[1].split("|")))
	res=wins & card
	scores[lid]=len(res)
	for i in range(1,scores[lid]+1):
		counts[lid+i] += counts[lid] 
	if scores[lid]>0:
		total=total+2**(scores[lid]-1)
print('Solution for Part 1 : '+ str(total))
print('Solution for Part 2 : '+ str(sum(counts)))
