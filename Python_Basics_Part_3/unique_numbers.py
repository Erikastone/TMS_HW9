nums = [6,9,0,3,4,6,7,1,2,1,3,4,3,3,3]

for i in range(len(nums)):
    count =nums.count(i)
    if count > 1:
        print(f"The number {i} appears {count} times.")