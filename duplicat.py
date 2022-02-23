# a=[1,2,3,3,3,3,4,5]
# i=0
# b=[]
# while  i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)


n=int(input("enter the number.."))
def mul():
  i=1
  mul=1
  while i<=n:
    num=int(input("enter the number.."))
    mul=mul*num
    i=i+1
  print(mul)
mul()