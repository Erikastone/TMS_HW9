#Реализовать функцию, которая находит сумму элементов
#матрицы (матрица M x N). Определить, какую долю в общей сумме
#(процент) составляет сумма элементов каждого столбца
import numpy as np
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]       
    return matrix

def precent_matrix(matrix):
    # Находим сумму всех элементов матрицы
    total_sum = np.sum(matrix)
    # Находим сумму элементов каждого столбца
    colum_sum = np.sum(matrix,axis=0)
    # Вычисляем процент для каждого столбца
    precents = (colum_sum /total_sum) * 100
    return precents

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = matrix_random(m,n)
for row in matrix_random(m,n):
    print(row)

precent = precent_matrix(matrix)
print(f"Процент элементов каждого столбца: {precent}")    