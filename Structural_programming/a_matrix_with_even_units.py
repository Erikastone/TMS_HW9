#Дана матрица M x N. Исходная матрица состоит из нулей и
#единиц. Реализовать функцию, которая добавит к матрице ещё
#один столбец, элементы которого делает количество единиц в
#соответствующей строке чётным
import numpy as np
import random

def matrix_random(m,n):
    matrix = [[random.randint(0,1) for _ in range(n)] for _ in range(m)]
    return matrix
#В этой функции мы создаем новую матрицу с дополнительным столбцом, 
# копируем элементы из исходной матрицы, подсчитываем количество единиц 
# в каждой строке и делаем его чётным, если необходимо
def make_row_ones_even(matrix):
    """
    Добавляет к матрице ещё один столбец, элементы которого делают количество единиц в соответствующей строке чётным.
    Args:
        matrix (List[List[int]]): Исходная матрица M x N (состоящая из нулей и единиц).
    Returns:
        List[List[int]]: Новая матрица с добавленным столбцом.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # Создаем новую матрицу с дополнительным столбцом
    new_matrix = np.zeros((num_rows, num_cols + 1), dtype = int)

    for i in range(num_rows):
        # Копируем элементы из исходной матрицы
        new_matrix[i, :num_cols] = matrix[i]
        
        # Подсчитываем количество единиц в строке
        num_ones = sum(matrix[i])
        
        # Делаем количество единиц чётным
        if num_ones % 2 == 1:
            new_matrix[i, -1] = 1
    return new_matrix
        
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = matrix_random(m,n)
result_matrix = make_row_ones_even(matrix)

for row in result_matrix:
    print(row)