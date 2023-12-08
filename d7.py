f=open('inputday7.txt')
lines=f.readlines()
f.close()


def num_rank(rank):
    if rank[0] == "A":
        return 14
    if rank[0] == "J":
        return 11
    if rank[0] == "Q":
        return 12
    if rank[0] == "K":
        return 13
    if rank[0] == "T":
        return 10
    if rank[0] == "*":
        return 1
    return int(rank)

def score(mamain):
    counters={}
    for c in mamain:
        counters[c]= mamain.count(c)
    if 5 in counters.values():
        score=6*15**5
    elif 4 in counters.values():
        score=5*15**5
    elif 3 in counters.values() and 2 in counters.values():
        score=4*15**5
    elif 3 in counters.values():
        score=3*15**5
    elif 2 in counters.values() and list(counters.values()).count(2)==2:
        score=2*15**5
    elif 2 in counters.values():
        score=1*15**5
    else:
        score=0
    return score+num_rank(mamain[0])*15**4+num_rank(mamain[1])*15**3+num_rank(mamain[2])*15**2+num_rank(mamain[3])*15+num_rank(mamain[4])

data=[]
for l in lines:
    c=l.split()
    data.append((c[0],int(c[1]),score(c[0])))
total=0
datasorted=sorted(data, key=lambda el:el[2])
for myid, el in enumerate(datasorted):
    total+= el[1]*(myid+1)
print('Solution for Part 1 : %s' % total)

def score2(mamain):
    # bricolage et compagnie... je deteste compter les cartes
    counters={}
    counterwithj={}
    nbj = mamain.count("J")
    mamain=mamain.replace("J","*")
    rest=mamain.replace("*","")
    for c in rest:
        counters[c]= rest.count(c)        
    for c in mamain:
        if c != '*':
            counterwithj[c]=mamain.count(c)+nbj
        else:
            counterwithj[c]=mamain.count(c)
    if 5 in counterwithj.values() or nbj==5:
        score=6*15**6
    elif 4 in counterwithj.values(): 
        score=5*15**6
    elif len(counters)==2 :
        score=4*15**6
    elif 3 in counterwithj.values():
        score=3*15**6
    elif list(counters.values()).count(2)==2 :
        score=2*15**6
    elif list(counters.values()).count(2)==1 or nbj==1:
        score=1*15**6
    else:
        score=0
    return score+num_rank(mamain[0])*15**4+num_rank(mamain[1])*15**3+num_rank(mamain[2])*15**2+num_rank(mamain[3])*15+num_rank(mamain[4])

data=[]
for l in lines:
    c=l.split()
    data.append((c[0],int(c[1]),score2(c[0])))
total=0
datasorted=sorted(data, key=lambda el:el[2])
for myid, el in enumerate(datasorted):
    total+= el[1]*(myid+1)
print('Solution for Part 2 : %s' % total)
