N = int(input())
M = int(input())
x = int(input())
y = int(input())
a = 0
b = 0
if N-x < x:
    a = N-x
else:
    a = x


if M-y < y:
    b = M-y
else:
    b = y

if a<=b:
    print(a)
else:
    print(b)
