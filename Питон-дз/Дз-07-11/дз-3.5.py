print('Введите координаты первой клетки')
a = int(input())
b = int(input())
print('Введите координаты второй клетки')
c = int(input())
d = int(input())
p1 = 'none'
p2 = 'none'
if (a%2 == 0 and b%2 ==0) or (a%2 == 1 and a%2 ==1):
    p1 = 'black'
elif (a%2 == 1 and b%2 ==0) or (a%2 == 0 and a%2 ==1):
    p1 = 'white'



if (c%2 == 0 and d%2 ==0) or (c%2 == 1 and d%2 == 1):
    p2 = 'black'
elif (c%2 == 1 and d%2 ==0) or (c%2 == 0 and d%2 ==1):
    p2 = 'white'



if p1 == p2:
    print('YES')
else:
    print('NO')
