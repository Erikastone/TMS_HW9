#Реализовать функцию, которая находит сумму элементов
#на главной диагонали и сумму элементов на побочной диагонали
#(матрица M x N)
import random

def matrix_random(m,n):
    matrix =[[random.randint(1,100) for _ in range(n)] for _ in range(m)]
    return matrix
#Используя два вложенных цикла (O(N^2)): В этом методе мы используем два цикла: 
# один для прохода по строкам, а другой для прохода по столбцам. Для каждого элемента 
# матрицы мы проверяем, принадлежит ли он главной или побочной диагонали, и добавляем его к соответствующей сумме
def sum_diagonal(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    principal_sum = 0
    secondery_sum = 0
    
    for i in range(num_rows):
        for j in range(num_cols):
            if i == j:
                principal_sum += matrix[i][j]
            if i + j == num_rows - 1:
                secondery_sum += matrix[i][j]
    return principal_sum, secondery_sum

m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = matrix_random(m,n)
principal,secondery = sum_diagonal(matrix)

for row in matrix_random(m,n):
    print(row)

print(f"Сумма на главной диагонали: {principal}")
print(f"Сумма на побочной диагонали: {secondery}")    