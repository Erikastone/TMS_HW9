from math import pow
# i = annual interest rate
i = float(input("Enter the annual interest rate: "))
# s = loan amount
s = float(input("Enter the loan amount: "))
# n = the number of months for which to take out a loan
n = float(input("Enter the number of months for which the loan is taken out: "))
# p = monthly interest rate
p = i / n
# m = monthly payment
m = (s * p * pow((1 + p), n)) / (pow((1 + p), n) - 1)

print(f"The amount of the monthly payment: {m} , The amount you will pay to the bank: {m * n}, Overpayment: {(m * n) - s}")