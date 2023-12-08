from math import lcm
f=open('inputday8.txt')
lines=f.readlines()
f.close()
dirs = lines[0][:-1].replace('L','0').replace('R','1')
maps={}
starts=[]
for l in lines[2:]:
    start,couple=l.split(' = ')
    if start[2]=='A':
        starts.append(start)
    maps[start]=couple[1:-2].split(', ')

start='AAA'
step=1
notfound=True
while notfound :
    for go in dirs:
        start=maps[start][int(go)]
        if start == 'ZZZ':
            notfound = False
            break
        step += 1

print('Solution for Part 1 : %s' % step)

step=1
found=False
indexes={}
while not found :
    for go in dirs:
        newstarts=[]
        for idx,start in enumerate(starts):
            newstart=maps[start][int(go)]
            if newstart[2]=='Z':
                if idx not in indexes:
                    indexes[idx]=step
            newstarts.append(newstart)
        starts=newstarts
        if len(indexes.values())==len(starts) :
            found=True
            break
        step += 1
print('Solution for Part 2 : %s' % lcm(*indexes.values()))
