d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d1=[]
for values in sorted(d):
	a=values,":",d[values]
	d1.append(a)
print(d1)
