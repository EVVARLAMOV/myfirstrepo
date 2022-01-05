a = [int(i) for i in input().split()]
for k in range(1,len(a)-1):
    if a[k]>a[k+1] and a[k]> a[k-1]:
        print(a[k])
