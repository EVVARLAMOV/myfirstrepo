a = float(input(print('Введите первое число')))
b = float(input(print('Введите второе число'))) 
operation = str(input('Введите оператор'))
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
else:
    print('Недопустимый оператор')
