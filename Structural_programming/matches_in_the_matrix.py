#Программа получает на вход число H. Реализовать
#функцию, которая определяет, какие столбцы имеют хотя бы одно
#такое же число, а какие не имеют (матрица M x N)
import numpy as np
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]
    return matrix
def find_elemet_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # Инициализируем список для хранения информации о столбцах
    column_has_same_number = [False] * num_cols
    
    for j in range(num_cols):
        # Создаем множество для хранения уникальных чисел в столбце
        unique_numbers = set()
        for i in range(num_rows):
            unique_numbers.add(matrix[i][j])
        # Если множество содержит более одного числа, столбец имеет хотя бы одно такое же число
        column_has_same_number[j] = len(unique_numbers) > 1
    return column_has_same_number

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = matrix_random(m, n)
result = find_elemet_matrix(matrix)
for row in matrix_random(m,n):
    print(row)
print(f"Имеет ли столбец уникальное число :{result}")            