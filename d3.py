import re
f=open('inputday3.txt')
lines=f.readlines()
f.close()
symbols='*#-+@%&=$/'
symbolloc=[]
pieces=[]
for lid,line in enumerate(lines):
	symbolloc.append([(m.start(0)) for m in re.finditer('(\*|\#|\-|\+|\@|\%|\&|\=|\$|\/)', line)])

for lid,line in enumerate(lines):
	numbers = re.finditer('(\d+)', line)
	for res in numbers:
		startidx=max([res.start()-1,0])
		endidx=min([res.end()+1,140])
		part=res.group(0)
		if (lid>0):
			for pos in symbolloc[lid-1]:
				if pos in range(startidx,endidx):
					pieces.append(part)
		if ((startidx in symbolloc[lid])):
			pieces.append(part)
		if (((endidx-1) in symbolloc[lid])):
			pieces.append(part)
		if (lid<139):
			for pos2 in symbolloc[lid+1]:
				if pos2 in range(startidx,endidx):
					pieces.append(part)

print('Solution for Part 1 : '+ str(sum([int(p) for p in pieces])))

total2=0
symbolloc=[]
gears={}
for lid,line in enumerate(lines):
	symbolloc.append([(m.start(0)) for m in re.finditer('(\*)', line)])
for lid,line in enumerate(lines):
	numbers = re.finditer('(\d+)', line)
	for res in numbers:
		startidx=max([res.start()-1,0])
		endidx=min([res.end()+1,140])
		part=res.group(0)
		if (lid>0):
			for pos in symbolloc[lid-1]:
				if pos in range(startidx,endidx):
					k=pos+140*(lid-1)
					if k not in gears:
						gears[k]=[]
					gears[k].append(int(part))
		if (startidx in symbolloc[lid]):
			k=startidx+140*lid
			if k not in gears:
				gears[k]=[]
			gears[k].append(int(part))
		if (endidx-1) in symbolloc[lid]:
			k=endidx-1+140*lid
			if k not in gears:
				gears[k]=[]
			gears[k].append(int(part))
		if (lid<139):
			for pos2 in symbolloc[lid+1]:
				if pos2 in range(startidx,endidx):
					k=pos2+140*(lid+1)
					if k not in gears:
						gears[k]=[]
					gears[k].append(int(part))
for gear in gears:
	if len(gears[gear])==2:
		total2 = total2+gears[gear][0]*gears[gear][1]

print('Solution for Part 2 : '+ str(total2))
