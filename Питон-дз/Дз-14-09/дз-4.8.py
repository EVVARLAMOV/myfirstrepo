print('Введите список, оканчивающийся 0')
a = [int(i) for i in input().split()]
b = 0
for k in range(len(a)-1):
    if a[k]<a[k+1]:
        b +=1
print(b)
