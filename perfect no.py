# i = 1
# sum=0
# n = int(input("Enter a number: "))
# while(i <= n//2 ):
#     if (n % i == 0) :
#         sum += i
#     i += 1
# if sum == n :
#     print(n,"is a perfect number")

# else :
#     print(n,"is not a perfect number")


def show():
    i = 1
    sum=0
    n = int(input("Enter a number: "))
    while(i <= n//2 ):
        if (n % i == 0) :
            sum += i
        i += 1
    if sum == n :
        print(n,"is a perfect number")

    else :
        print(n,"is not a perfect number")
show ()