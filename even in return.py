def dis():
    i=1
    b=[]
    while i<=10:
        b.append(i)
        i=i+1
    return b
def show():
    a=dis()
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],"even")
        else:
            print(a[i],"odd")
        i=i+1
show()