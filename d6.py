from math import floor,ceil

f=open('inputday6.txt')
lines=f.readlines()
f.close()

def delta(d,record):
	return (d**2-4*record)

def result(d,record):
	# first think with math so we look for size of interval between the 2 roots of equation x^2-dx+record
	return floor((d+delta(d,record)**0.5)/2)-ceil((d-delta(d,record)**0.5)/2)+1

durations=[*map(int, lines[0].split(':')[1].split())]
records=[*map(int, lines[1].split(':')[1].split())]
total=1
for i in range(len(durations)):
	total *= result(durations[i],records[i])
print('Solution for Part 1 : '+ str(total))

duration=int(lines[0].split(':')[1].replace(" ",""))
record=int(lines[1].split(':')[1].replace(" ",""))
total = result(duration,record)
print('Solution for Part 2 : '+ str(total))