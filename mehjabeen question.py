#  
# a=[1,2,3,4,5]
# i=0
# j=0
# while i<len(a)-1:
#     print(a[i]+a[j])
#     j=j+1
# i=i+  



# def catAndMouse(x,y,z):
#     if(x-z)==(y-z):
#         return "Mouse C"
#     elif (x-z)>(y-z):
#         return "Cat B"
#     else:
#         return  "Cat A"
# x=int(input("enter distance"))
# y=int(input("enter distance"))
# z=int(input("enter distance"))
# print(catAndMouse(x,y,z))

# DistanceA=int(input("enter a distance"))
# DistanceB=int(input("enter a distance"))
# if DistanceA>DistanceB:
#     print("cat B")
# elif DistanceA== DistanceB:
#     print("Mouse C")
# else:
#     print("cat  A")


def prime(num):
    i=1
    while i<=num:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count=count+1
            j+=1
        if count==2:
            print(i,"prime no")
        i+=1
num=int(input("enter a num"))
(prime(num))












