a = [int(i) for i in input(print('Введите последовательность, заканчивающуюся на 0')).split()]
b = 0
c = 0
for k in range(0,len(a)-1):
    if b < a[k]:
        b = a[k]
for k in range(0,len(a)-1):
    if a[k] == b:
        c += 1

print(c)
