def is_very_even_number(n):
    if n%2==0:
        num=n//10
        num=n%10
        if num%2==0:
            return True
        else:
            return False
    else:
        return False
is_very_even_number()





