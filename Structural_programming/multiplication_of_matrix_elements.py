#Реализовать функцию, которая перемножает элементы
#каждого столбца матрицы с соответствующими элементами K-го
#столбца (матрица M x N)
import numpy as np
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]
    return matrix

def multiplay(matrix, K):
    # Выбираем K-й столбец (индексация с 0)
    k_colum =matrix[:, K]
    result_matrix = matrix * k_colum[:, np.newaxis]
    return result_matrix

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
k = int(input("Введи нужый индекс столбца: "))
matrix = np.array(matrix_random(m, n))
result = multiplay(matrix, k)
for row in matrix_random(m,n):
    print(row)

print(f"Результат умножения: {result}")