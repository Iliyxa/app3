import random
try:
    a = float(input('Введите число, из которого будет извлекаться корень: '))
    if a >= 0:
        def root(n):
            if n == 1:
                return (1 + a) / 2
            if n > 1:
                return (root(n - 1) + a / (root(n - 1))) / 2
        print(f'Корень из {a} примерно равен {str(root(5))[:7]}')
    else:
        print('Вы ввели отрицательное число или не число вовсе')
except:
    print('Вы ввели отрицательное число или не число вовсе')

