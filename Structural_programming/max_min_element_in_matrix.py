#Реализовать функцию, которая находит минимальный и
#максимальный элементы в матрице (матрица M x N). Вывести в
#консоль индексы найденных элементов
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]
    return matrix

def min_max_elem(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    min_index = None
    max_index = None
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_index = (i,j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_index = (i,j)
    
    print(f"Минимальный элемент: {min_val} индеск: {min_index}") 
    print(f"Максимальный элемент: {max_val} индеск: {max_index}")                 

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = matrix_random(m, n)
for row in matrix:
    print(row)

min_max_elem(matrix)