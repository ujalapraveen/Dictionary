dic1=[]
dic2=[]
dic={}
i=1
while i<=10:
    r=input("enter the name of student:=")
    u=int(input("enter the marks;="))
    dic1.append(r)
    dic2.append(u)
    i=i+1
j=0
while j<len(dic1):
    dic[dic1[j]]=dic2[j]
    j+=1
print(dic)
