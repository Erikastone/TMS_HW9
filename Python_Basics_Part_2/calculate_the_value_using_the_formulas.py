import math

a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
x = float(input("Enter x number: "))

y = (a ** 2) / 3 + (a ** 2 + 4) / b + math.sqrt(a ** 2 + 4) / 4 + math.sqrt((a ** 2 + 4) ** 3) / 4
y_cos = math.cos(x) + math.sin(x)
y_cos2 = math.sqrt(math.cos(x) **4 + math.sin(2 * x -1) ** 2)
y_2 = (5 * x + 3 * x **2) * math.sqrt(1 + math.sin(x) **2)

print(f"formula a: {y}, formula b: {y_cos}, formula c: {y_cos2}, formula d: {y_2}")