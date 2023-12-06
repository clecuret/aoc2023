f=open('inputday5.txt')
lines=f.readlines()
f.close()
seeds = [*map(int, lines[0].split(": ")[1].split())]
maps={}
mapnb=0
for i in "\n".join(lines[2:]).split("\n\n"):
    if ':' in i:
        mapnb += 1
    elif len(i)>2:
        if mapnb not in maps:
            maps[mapnb]=[]
        maps[mapnb].append(i.split())

res = []
for token in seeds:
    for mymap in maps:
        for dest, source, nb in maps[mymap]:
            if int(source) <= token and token < int(source) + int(nb):
                token = int(dest) + token - int(source)
                break
    res.append(token)
print('Solution for Part 1 : '+ str(min(res)))

seeds = [*map(int, lines[0].split(": ")[1].split())]
startintervals = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
maps = [[[*map(int, n.split())] for n in i.split("\n")[1:]] for i in "".join(lines[2:]).split("\n\n")]

sol=[]
for interv in startintervals:
    remaining = [interv]
    result = []
    for intermap in maps:
        while remaining:
            inter = remaining.pop()  
            for dest, src, nb in intermap:
                deb=inter[0]
                fin=inter[1]
                if fin < src or deb >= src + nb:  # simple case, we continue
                    continue
                elif deb < src  and src <= fin  and fin < src + nb:  # partial case 1
                    result.append((dest, dest + fin - src))
                    remaining.append((deb, src - 1))
                    break
                elif src <= deb  and  fin < src + nb:  # all is inside
                    result.append((dest - src + deb, dest - src + fin))
                    break
                elif src <= deb and deb < src + nb  and src + nb <= fin:  # partial case 2
                    result.append((dest -src + deb, dest + nb - 1))
                    remaining.append((src + nb, fin))
                    break
                elif deb < src and src + nb <= fin:  #  a part of each side is outside
                    result.append((dest, dest + nb - 1))
                    remaining.append((deb, src - 1))
                    remaining.append((src + nb, fin))
                    break
            else:  
                result.append(inter)
        remaining = result
        result = []
    sol.extend(remaining)
print('Solution for Part 2 : '+ str(min(loc[0] for loc in sol)))
