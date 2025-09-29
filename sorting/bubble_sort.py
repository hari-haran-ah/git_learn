def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

my_list = [5, 2, 4, 6, 1, 3]
sorted_list = bubble_sort(my_list)
print(f"Sorted list: {sorted_list}")


