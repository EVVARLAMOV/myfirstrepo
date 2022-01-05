n = int(input())
a = (1440 - n)//60
if a < 0:
    a = -a
    if a > 24:
        while a > 24:
            a -= 24
elif a%24 == 0:
        a = '00'
print(a,':')
