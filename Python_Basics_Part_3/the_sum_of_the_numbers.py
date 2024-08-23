total = 0
numbers = [2,6,8,4,6,7]

for i in range(0,len(numbers)):
    total = total + numbers[i]
    max_elem =max(numbers)
    min_elem = min(numbers)
    print(f"Total: {total} and max {max_elem} min {min_elem}")