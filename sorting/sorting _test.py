def selection_sort_get_second_largest_element(arr):
    arr = list(set(arr))
    n = len(arr)
    for i in range(n):
        min_val = i
        for j in range(i+1,n):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i],arr[min_val] = arr[min_val],arr[i]
    
    return arr[-2] ,arr

my_list = list(map(int,input("Enter the number with space:").split()))
second_largest,array_ele = selection_sort_get_second_largest_element(my_list)
print(f"Second largest element is: {second_largest}")
print(f"Sorted array is: {array_ele}")

