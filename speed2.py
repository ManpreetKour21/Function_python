# def function(speed):
#     if speed<70:
#         print("ok")
#     elif speed>70:
#         i=71
#         b=0
#         while i<=speed:
#             if i%5==0:
#                 b+=1
#             i+=1
#         print(b)
#         if b>12:
#             print("License suspended")
#         else:
#             pass
# speed=int(input("Enter the number:"))
# function(speed)
def function(speed):
    if speed<70:
        print("ok")
    else:
        i=71
        b=0
        while i<=speed:
            if i%5==0:
                b+=1
            i+=1
        print(b)
        if b>12:
            print("License suspended")
        else:
            pass
speed=int(input("Enter the number:"))
function(speed)



