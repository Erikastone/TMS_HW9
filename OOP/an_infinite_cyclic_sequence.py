from itertools import cycle

def cyclic_sequence():
    numbers = [1, 2, 3] 
    for num in cycle(numbers):
        yield num

try:
    user_limit = int(input("Введите количество чисел для вывода: "))
    sequence = cyclic_sequence()
    for _ in range(user_limit):
        print(next(sequence))
except ValueError:
    print("Пожалуйста, введите целое число.")