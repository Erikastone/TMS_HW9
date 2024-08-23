cash_phone = float(input("Enter the cost of the phone : "))
sum_cost = float(input("Enter the amount you can set aside : "))

days = 0
money = 0

while money < cash_phone:
    days += 1
    if days % 7 != 0:
        money += sum_cost
print(f"In {days} days you can save up") 