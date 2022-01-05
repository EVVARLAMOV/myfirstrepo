a = [int(i) for i in input().split()]
b = 0
for k in range(0,len(a)-1):
    if b < a[k]:
        b = a[k]
print(a.pop(a.index(b)))
print(a.index(b))
