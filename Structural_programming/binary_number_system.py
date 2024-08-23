#O(logn)
#Программа получает на вход число в десятичной системе
#счисления. Реализовать функцию, которая переводит входное
#число в двоичную систему счисления. Допускается реализация
#функции как в рекурсивном варианте, так и с итеративным
#подходом
def binary_number(number):
    if number == 0:
        return '0'
    
    binary =""
    
    while number > 0:
        binary =str(number % 2) + binary
        number //= 2
    return binary
    
binary_numbers =int(input("Number of binary numbers:" ))
binary_num = binary_number(binary_numbers)
print(binary_num)    