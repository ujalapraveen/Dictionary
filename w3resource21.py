# d= {'1':['a','b'], '2':['c','d']}
# list1=d.get("1")
# list2=d.get("2")
# for i in range(2):
#     for j in range(2):
#         print(list1[i]+list2[j])



d={'1':['a','b'],'2':['c','d']}
i=0
list1=d.get('1')
list2=d.get('2')
while i <len(d):
    j=0
    while j<len(d):
        new=(list1[i]+list2[j])
        print(new)
        j+=1
    i+=1
