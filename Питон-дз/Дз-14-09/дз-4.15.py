a = [int(i) for i in input(print('Введите первый список')).split()]
b = [int(i) for i in input(print('Введите второй список')).split()]
c = []
if len(a) != len(b):
    print('Ошибка')
else:
    for i in range(len(a)):
            c.append(a[i] + b[i])
print(c)
