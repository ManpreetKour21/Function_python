def name(a,b,c,d):
    if len(a)>len(b) and len(a)>len(c) and len(a)>len(d):
        print(a)
    if len(b)>len(a) and len(b)>len(c) and len(b)>len(d):
        print(b)
    if len(c)>len(a) and len(c)>len(b) and len(c)>len(d):
        print(c)
    if len(d)>len(a) and len(d)>len(b) and len(d)>len(c):
        print(d)
    if len(a)==len(b):
        print(a)
        print(b)
    if len(c)==len(d):
        print(c)
        print(d)
name ("hello","welcome","sonu","monu")