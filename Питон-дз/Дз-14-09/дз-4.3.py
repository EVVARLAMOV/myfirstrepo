print('Введите натураоьное число не меньшее 2')
N = int(input())
for i in range(2,N-1):
    if N%i == 0:
        print(i)
        break
    else:
        i += 1
