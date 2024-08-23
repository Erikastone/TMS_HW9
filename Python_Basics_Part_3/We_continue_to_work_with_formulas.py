import math

def cos_maclaurin(x, n_terms=10):
    result = 1.0  # Начальное значение ряда (первый член)
    sign = 1  # Знак для чередующихся членов

    for n in range(1, n_terms):
        term = (x ** (2 * n)) / math.factorial(2 * n)
        result += sign * term
        sign *= -1  # Чередуем знак

    return result

# Пример использования:
x_value = 1.5  
n_terms_to_calculate = 10  # Количество членов ряда для вычисления

cos_value = cos_maclaurin(x_value, n_terms_to_calculate)
print(f"cos({x_value}) ≈ {cos_value:.6f}")