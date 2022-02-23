def show():
    list1=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
    i=0
    max=0
    while i<len(list1):
        count=0
        j=0
        while j<len(list1[i]):
            count=count+1
            if count>max:
                max=count
                li=list1[i]
            j=j+1
        i=i+1
    # print(count)
    print("max length =",max,"it's list-",li) 
show ()

