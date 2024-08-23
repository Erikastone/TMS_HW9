#Реализовать функцию, которая создаёт матрицу размером
#M строк на N столбцов и заполняет её рандомными числами
import random

def matrix_random(M,N):
    matrix = [[random.randint(1,100) for _ in range(N)] for _ in range(M)]
    return matrix

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

for row in matrix_random(m,n):
    print(row)