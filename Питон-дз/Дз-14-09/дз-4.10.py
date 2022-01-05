a = [int(i) for i in input(print('Введите списком рост каждого ученика')).split()]
x = int(input(print('Введите рост Пети')))
a.append(x)
a.sort()
a.reverse()
print(a.index(x))
