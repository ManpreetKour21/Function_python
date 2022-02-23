# def sec_max():
#     list=[-50,-3,1,-2,-4,-6]
#     i=0
#     max=0
#     sec=list[i]
#     while i<len(list):
#         if list[i]>max:
#             max=list[i].
#         i+=1
#         j=0
#         while j<len(list):
#             if max>list[j] and list[j]>sec:
#                 sec=list[j]
#             j+=1
#     print("first max number :-",max)
    # print("sec max number :-",sec)
# sec_max()



def sec_max(list):
    # list=[-50,-3,1,-2,-4,-6]
    i=0
    max=0
    sec=list[i]
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i+=1
        j=0
        while j<len(list):
            if max>list[j] and list[j]>sec:
                sec=list[j]
            j+=1
    print("first max number :-",max)
    print("sec max number :-",sec)
sec_max([-50,-3,1,-2,-4,-6])



# def aad(a,b):
#     c=a+b
#     print(c)
#     add()

# add ()

