dic={"first":1,"second":2,"third":1,"four":5,"five":5,"six":9,"seven":7}

i=[]
for val in dic.values():
    if val in i:
        continue
    else:
        i.append(val)
print(i)


#['2', '7', '9', '5', '1'] 

