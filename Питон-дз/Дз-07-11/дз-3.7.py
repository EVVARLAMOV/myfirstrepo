print('Введите координаты первой клетки')
a = int(input())
b = int(input())
print('Введите координаты второй клетки')
c = int(input())
d = int(input())
if (c == a + 2 or c == a - 2) and (d == b + 1 or d == b - 1):
    print('YES')
elif (c == a + 1 or c == a - 1) and (d == b + 2 or d == b - 2):
    print('YES')
else:
    print('NO')
