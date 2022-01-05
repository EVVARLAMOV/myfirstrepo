a = [int(i) for i in input(print('Введите последовательность чисел, оканчивающуюся на 0')).split()]
b = 0
c = []
d = 0
for k in range(0,len(a)-1):
    if a[k] == a[k+1]:
        b += 1
    else:
        c.append(b)
        b = 0

for k in range(len(c)-1):
     if c[k] < c[k+1]:
         d = c[k]

print(d)
    
