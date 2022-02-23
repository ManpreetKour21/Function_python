a ="good"
b="ogd"
i=0
while i<len (b):
    j=0
    while j<len(a):
        if b[i]==a[j]:
            print(a[j],end="")
        j=j+1
    i=i+1