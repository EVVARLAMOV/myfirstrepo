a = [int(i) for i in input().split()]
def srar(a):
    b = 0
    for i in range(len(a)):
        b += a[i]
    b = b/len(a)
    return(b)
