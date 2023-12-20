import random
def findmina():
    for i in range(m):
        minki1.append((min(matrix1[i])))
    chich1 = min(minki1)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if matrix1[i][j] == chich1 and chich1 == min(matrix1[i]):
                print(f'Его координаты: строка {i + 1} столбец {j + 1}')
def findminb():
    for i in range(m):
        minki2.append((min(matrix2[i])))
    chich2 = min(minki2)
    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            if matrix2[i][j] == chich2 and chich2 == min(matrix2[i]):
                print(f'Его координаты: строка {i + 1} столбец {j + 1}')
minki1 = []
minki2 = []
try:
    m = abs(int(input('Введите количество строк первой матрицы: ')))
    n = abs(int(input('Введите количество столбцов первой матрицы: ')))
    matrix1 = [[random.randint(10, 99) for i in range(n)] for j in range(m)]
    for r in range(m):
        print(matrix1[r])
    findmina()
    k = abs(int(input('Введите количество строк второй матрицы: ')))
    l = abs(int(input('Введите количество столбцов второй матрицы: ')))
    matrix2 = [[random.randint(10, 99) for i in range(l)] for j in range(k)]
    for r in range(m):
        print(matrix2[r])
    findminb()
except:
    print('Вы ввели неверные размеры')