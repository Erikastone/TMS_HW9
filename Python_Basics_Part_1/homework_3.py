#1
variable_1 = 5
variable_2 = 7
variable_3 = 9

amount = variable_1 + variable_2 + variable_3
difference = variable_1 - variable_2 - variable_3
composition = variable_1 * variable_2 * variable_3
calculate_1 = variable_1 - variable_2 + variable_3
calculate_2 = (variable_1 * variable_2) / variable_3
calculate_3 = (variable_1 + variable_2) % variable_3

print ("There are three integer variables to calculate:",
    "\namount: ", amount, "\ndifference: ", difference, "\ncomposition: ", composition, "\ncalculate_1:",
    calculate_1, "\ncalculate_2:", calculate_2, "\ncalculate_3:", calculate_3)

#2
from math import sqrt
cat_a = float(input("cat a: "))
cat_b = float(input("cat b: "))
square = (cat_a * cat_b) / 2
hypotenuse = sqrt(cat_a ** 2 + cat_b ** 2)

print("A right triangle with cat_a andcat_b legs is given. Find the area of the triangle and its hypotenuse.",
    "\nsquare: ", square,"\nhypotenuse:", hypotenuse)

#3
str_world = "Hello world, a b c, test, test1 test2 test3 test4 test5"
world_count = len(str_world.split())
print("Determine how many words are in a line: ", world_count)

#4
text = "hhhabchghhh"
text = text.replace('h', 'H', text.count('h') -1).replace('H', 'h', 1)
print("Replacing all occurrences of the letter h with the letter H in this line, except for the first and last occurrences: ",text)

#5
str_text = "Hello"
print("the third character of this line: ", str_text[2])
print("the penultimate character of the string: ", str_text[-2])
print("the first five characters of the string: ", str_text[:5])
print("the entire line up to the last two characters: ", str_text[:-2])
print("all characters with even indexes",
"assuming that indexing starts at 0, so characters"
"are output starting from the first one: ", str_text[::2])
print("all characters with odd indexes,"
"that is, starting from the second character of the string: ", str_text[1::2])
print("all characters are in reverse order: ", str_text[::-1])
print("all characters of the string are separated by one in"
"reverse order, starting from the last one: ", str_text[::-2])
print("print the length of this string: ", len(str_text))

#6
num = input("number: ")
print("the last digit: ", num[-1])

#7
numbers = int(input("numbers: "))
print("the number of tens in the number: ", numbers // 10 % 10)

#8
numbers_3 = 567
sum_1 = numbers_3 % 10
numbers_3 = numbers_3 // 10
sum_2 = numbers_3 % 10
numbers_3 = numbers_3 // 10
print("the sum of the digits of a three-digit number: ", numbers_3 + sum_1 + sum_2)
