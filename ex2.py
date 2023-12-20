def PowerA3():
    n = 5
    try:
        while n > 0:
            n  = n - 1
            a = float(input('Введите число А: '))
            b = a ** 3
            print(f'B = {b}')
    except:
        print('Введено неверное значение')
PowerA3()