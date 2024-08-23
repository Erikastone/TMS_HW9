#Программа получает на вход число. Реализовать функцию,
#которая определяет, является ли это число простым (делится
#только на единицу и на само себя)
def simpel_num(number: int) -> int:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input('Number: '))
if simpel_num(number):
    print(f'{number} число простое')
else:
    print(f'{number} число не простое')