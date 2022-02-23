def lenth():
    list1=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
    i=0
    lis=[]
    while i<len(list1):
        count=0
        j=0
        while j<len(list1[i]):
            count=count+1
            j=j+1
        lis.append(count)
        i=i+1
    print(lis)
lenth ()


