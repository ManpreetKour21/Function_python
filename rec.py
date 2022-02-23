# import sys
# print(sys.getrecursionlimit())


# def show ():
#     print("my love simar")
#     show ()
# show ()

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibo (n-1)+fibo (n-2))


n=int(input("enter the number..........."))
i=0
while i<=n:
    print(i)
    i+=1


fibo ()




