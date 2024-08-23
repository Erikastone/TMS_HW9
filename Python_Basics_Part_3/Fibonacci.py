fib1 = fib2 = 1

nubber_el = int(input("nubber : ")) #- 2

#while nubber_el > 0:
    # fib_sum = fib1 + fib2
    #fib1 = fib2
    #fib2 = fib_sum
    #nubber_el -= 1
    
#print(f"Fibonacci : {fib2}")
print(f"Fibonacci : {fib1} and {fib2}")
for i in range(2, nubber_el):
    fib1,fib2 = fib2, fib1 + fib2
    print(f"Fibonacci2 : {fib2}")
    