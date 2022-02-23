def sub():
    a=[34,27,6,4,7,3] 
    i=0
    j=1
    d=[]
    while i<len(a):
        b=[]
        sub=a[i]-a[j]
        d.append(sub)
        i=i+2
        j=j+2
    print(d)
sub ()