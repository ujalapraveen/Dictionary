d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for key in d1:
    if key in d2:
        d2[key]=d2[key]+d1[key]
for key in d1:
    if key not in d2:
        d2[key]=d1[key]
print(d2)




