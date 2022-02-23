# Complete the function that takes a non-negative integer n as input,
# and returns a list of all the powers of 2 with the exponent ranging 
# from 0 to n (inclusive).


def squares(n):
    a=0
    b=[]
    i=0
    while i<n+1:
        b.append(2**i)
        i+=1
    return b
user=int(input("Enter the number:"))
print(squares(user))