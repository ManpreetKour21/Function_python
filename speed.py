speed=int(input("enter the number....."))
def driver(speed):
    speed1=speed-70
    point=speed1//5
    if speed<=70:
        print("ok")
    elif point>12:
        print("License suspended")
    elif speed>70:
        print(point)
driver(speed)   





