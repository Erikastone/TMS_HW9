#O(len(n))
arr_list = [5,6,7,1,2,3,4]
left = 0
right = len(arr_list) - 1
data = 2
while left <= right:
    mid = (left + right) // 2
    if arr_list[mid] == data:
        print(f"Element {data} is at idex {mid}")
        break
    if arr_list[left] <= arr_list[mid]:
        if arr_list[left] <= data <= arr_list[mid]:
            right = mid - 1
        else:
            left = mid + 1          
    else:
        if arr_list[mid] <= data <= arr_list[right]:
            left = mid + 1
        else:
            right = mid - 1


