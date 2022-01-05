a = [int(i) for i in input().split()]
for k in range(len(a)-1):
    if a[k]*a[k+1] > 0:
        print(a[k],' , ', a[k+1])
