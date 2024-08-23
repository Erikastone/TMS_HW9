#Дан список чисел, отсортированных по возрастанию. На
#вход принимается значение, равное одному из элементов списка.
#Реализовать функцию, выполняющую рекурсивный алгоритм
#бинарного поиска, на выходе программа должна вывести позицию
#искомого элемента в исходном списке
def b_search(arr, left, right, data):
    if right < left:
        return -1
    else:
        mid = (left + right) //2
        if arr[mid] > data:
            return b_search(arr, left, mid -1, data)
        elif arr[mid] < data:
            return b_search(arr, mid + 1, right, data)
        else:
            return mid
        
list = [3,5,8,11,34,56,79]
print(b_search(list,0,6,34))