
def sum_of_list(nums):
    total = 0
    for i in nums:
        total += i
    return total


def missing_number(num,n):
        expected = n * (n+1) // 2
        actual = sum_of_list(num)
        return expected - actual  
          
num = list(map(int,input("Enter the number").split()))
max_list = num[0]
for i in num:
    if i > max_list:
        max_list = i
n = max_list
    
print(missing_number(num,n))


def find_missing_number_sort(nums, n):
    nums.sort()
    for i in range(1,n +1):
        if i not in nums:
            return i
    return None
num = list(map(int,input("Enter the number").split()))
max_list = num[0]
for i in num:
    if i > max_list:
        max_list = i
n = max_list
print(find_missing_number_sort(num,n))
