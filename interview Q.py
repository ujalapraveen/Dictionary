# item_list=[{'item':'item1','amount':400},
# {'item':'item2','amount':300},
# {'item':'item1','amount':750}]
# res =dict()
# for dict in item_list:
#     for list in dict:
#         if list in res:
#             res[list]+=(dict[list])
#         else:
#             res[list]=dict[list]
# print(str(res))



my_list=[{'item':'item1','amount':400},
{'item':'item2','amount':300},
{'item':'item1','amount':750}]
new_list=[]
for d in my_list:
    new_list.append(list(d.values()))
combined_dict={}
for t in new_list:
    if t[0] in combined_dict:
        combined_dict[t[0]]+=t[1]
    else:
        combined_dict[t[0]]=t[1]
print(combined_dict)





# numbers=[10,20,[300,400,[500,600],500],30,40]
# numbers[2][2][1]=800
# print(numbers)


# numbers=(1,2,3,4,5,6,7,8,9,10)
# print(numbers)

#for i in range(1,11):print(i,end=" ")
    #print(i,end=" ")
# for i in range(1,11)