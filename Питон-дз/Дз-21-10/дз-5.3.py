a = [int(i) for i in input(print('Введите список')).split()]
b = 0
for i in range(len(a)):
    if b < a[i]:
        b = a[i]
while(a.count(b)!= 0):
    a.pop(a.index(b))
b = 0
for i in range(len(a)):
    if b < a[i]:
        b = a[i]
print(b)
