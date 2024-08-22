def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

try:
    user_limit = int(input("Введите число: "))
    for num in fibonacci_generator(user_limit):
        print(num)
except ValueError:
    print("Пожалуйста, введите целое число.")