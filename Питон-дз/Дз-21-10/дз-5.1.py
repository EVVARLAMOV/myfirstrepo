a = [int(i) for i in input(print('Введите список')).split()]
k = int(input(print('Введите число')))
for i in range(len(a)):
    if a[i] == k:
        a[i] = 0
while(a.count(0)!= 0):
    a.pop(a.index(0))
    
print(a)
