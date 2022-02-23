a=["manpreett","chungali"]
i=0
b=[]
while i<len(a):
    c=[]
    j=0
    while j<len(a[i]):
        c.append(a[i][j])
        j+=1
    b.append(c)
    i+=1
print(b)
