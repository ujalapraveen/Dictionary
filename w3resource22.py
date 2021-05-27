

my_dict = {
    'a':500, 
    'b':5874, 
    'c':560,
    'd':400, 
    'e':5874, 
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
           b=key
        elif max1>my_dict[value]and max2<my_dict[value]:
           max2= my_dict[key]
           e=key
        elif max2>my_dict[value]and max3<my_dict[value]:
           max3=my_dict[key]
           c=key
list.append(b)
list.append(e)
list.append(c)
print(list)
    






