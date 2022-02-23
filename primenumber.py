# a=[1,2,3,4,5,6,7,8]
# i=1
# b=[]
# while i<len(a):
#     if a[i]%2!=0 or a[i]==2:
#         b.append(a[i])
#     i=i+1
# print(b)

# def show ():
#     a=[1,2,3,4,5,6,7,8]
#     i=1
#     b=[]
#     while i<len(a):
#         if a[i]%2!=0 or a[i]==2:
#             b.append(a[i])
#         i=i+1
#     print(b)
# show ()


def add():
    i=2
    while i<=100:
        j=2
        count=0
        while j<i:
            if i%j==0:
                count=count+1
            j=j+1

        if count==0:
            # 
            print(i,"prime")
        i+=1
   
add ()



# def primeornot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (nreturn (i,"prime")num % i) == 0:
#                 print(num,"is not a prime number")
#                     print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeornot(406)





# i=2
# while i<=100:
#     j=2
#     count=0
#     while j<i:
#         if i%j==0:
#             count=count+1
#         j=j+1

#     if count==0:
#         print(i,"prime")
#     i+=1


