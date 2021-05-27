dic={}
i=1
while i<=5:
    dic[i]=i*i
    i+=1
print(dic)

#o/p={1:1,2:4,3:9,4:16,5:25}



list=[1,2,3,3,3,3,4,5]
c=[]
i=0
while i<len(list):
    if list[i] not in c:
        c.append(list[i])
    i+=1
print(c)

#O/p=[1,2,3,4,5]

list=[1,2,3,4,5,6,7,8,9]
a=[]
i=0
while i<len(list):
    if list[i]%2==0:
        a.append(list[i])
    i+=1
print(a)

#O/P=[2,4,6,8]

list=[1,2,3,4,5]
i=0
new=0
list2=[]
while i<len(list):
    new=new+list[i]
    list2.append(new)
    i+=1
print(list2)

#O/P=[1,3,6,10,15]

    

