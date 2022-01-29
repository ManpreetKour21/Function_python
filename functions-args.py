def show():
    a=[1,2,3,4,5,6,7,10,-2]
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    print(max)
show ()