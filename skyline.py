def myfunc(s):
    x=''
    for i in range(len(s)):
        if i % 2 == 0:
            x = x + s[i].upper()
        else:
            x = x + s[i].lower()
    return str(x)
