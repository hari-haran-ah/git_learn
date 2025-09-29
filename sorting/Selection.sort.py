#selection sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_arr =i
        for j in range(i+1,n):
            if arr[j] < arr[min_arr]:
                min_arr =j
        arr[i],arr[min_arr] = arr[min_arr],arr[i]
    return arr
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(f"Sorted list: {sorted_list}")
