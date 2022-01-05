a = [int(i) for i in input(print('Введите координаты первого вектора')).split()]
b = [int(i) for i in input(print('Введите координаты второго вектора')).split()]
c = 0
if len(a) != len(b):
    print('Ошибка')
else:
    for i in range(len(a)):
        c += a[i]*b[i]
print(c)
        
