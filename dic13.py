# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 

# s=[]
# s1=[]
# for i in my_dict.values():
#     s.append(i)
# for j in my_dict.keys():
#     s1.append(j)
# var1=0
# var2=0
# n=0
# s2=[]
# l=len(s)
# while n >l:
#     n1=0
#     while n1<l:
#         if s[n1]>s[n]:
#             if s1[n1]not in s2:
#                 s2.append(s1[n1])
#         n1+=1
#     break
#     n+=1
# print(s2)


my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list=[]
i=0
max1=0
max2=0
max3=0
for key in my_dict:
    for value in my_dict:
        if my_dict[key]>max1:
           max1=my_dict[key]
           c=key
        elif max1>my_dict[value]and max2<my_dict[value]:
           max2= my_dict[key]
           d=key
        elif max2>my_dict[value]and max3<my_dict[value]:
           max3=my_dict[key]
           e=key
list.append(c)
list.append(d)
list.append(e)
print(list)
    


