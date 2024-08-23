arr_len = [1,3,5,7,9,11,13]
low = 0
hight = len(arr_len) - 1
data = 11

while low <= hight:
    midll = (low + hight) // 2
    if arr_len[midll] == data:
        print(f"Element 11 is at index {midll}")   
        break    
    elif arr_len[midll] < data:
        low = midll + 1
    else:
        hight = midll - 1
    