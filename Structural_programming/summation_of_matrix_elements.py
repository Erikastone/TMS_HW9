#Реализовать функцию, которая суммирует элементы
#каждой строки матрицы с соответствующими элементами L-й строки
#(матрица M x N)
import numpy as np
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]
    return matrix

def sum_rows(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # Инициализируем список для хранения сумм элементов строк
    row_sum = [0] * num_rows   
    for i in range(num_rows):
        for j in range(num_cols):       
            # Суммируем элементы каждой строки с соответствующими элементами L-й строки
            row_sum[i] += matrix[i][j]
    return row_sum       

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = matrix_random(m, n)
result = sum_rows(matrix)
for row in matrix_random(m,n):
    print(row)
print(f"Сумма элементов каждой строки: {result}")    