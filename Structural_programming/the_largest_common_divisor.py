#Программа получает на вход два числа и находит их НОД
#(наибольший общий делитель). Пример: на вход подаются числа 12
#и 18, их НОД равен 6
def divisor_number(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return divisor_number(num2, num1 % num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
divisor = divisor_number(num1, num2)
print(divisor)