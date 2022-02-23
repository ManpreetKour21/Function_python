a=int(input("enter the number.."))
b=int(input("enter the number.."))
def add():
    add=a+b
    return add

def sub():
    sub=a-b
    return sub

def mul():
    mul=a*b
    return mul

def div():
    div=a/b
    return div

def show():
    n=input("enter calculate..")
    if n=='add':
        print(add())
    if n=='sub':
        print(sub())
    if n=='mul':
        print(mul())
    if n=='div':
        print(div())
show()



