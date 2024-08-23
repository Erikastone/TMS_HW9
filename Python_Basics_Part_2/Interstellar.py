from math import pi
# l = the length of the year on the planet
# r = the radius of the planet's orbit (millionkm.)
r = float(input("radius: "))
# v = orbital speed (km/h)
v = float(input("orbital speed: "))
r2 = float(input("radius 2: "))
v2 = float(input("orbital speed 2: "))
l = 2 * r * pi / v
l2 = 2 * r2 * pi / v2
print(f"""The length of the year on the first and second planets : {l} and {l2} 
    Is it true that a year is longer on the first planet than on the second : {l == l2}""")