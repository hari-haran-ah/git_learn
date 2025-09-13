# product of three number
def sum_product(nums,target):
    n = len(nums)
    result =[]
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] * nums[j] * nums[k] == target:
                    result.append((nums[i],nums[j],nums[k]))
                    count +=1
    return result,count
nums = list(map(int,input("Enter the Value:").split()))
target =int( input("Enter the target Number: "))
result,count = sum_product(nums,target)
print(f" combination are :{result}")
print(f"the count of combination :{count}")

# count substring
def count_sub(string,target):
    total = []
    count = 0
    for i in range(len(string) - len(target) + 1):
        if string[i:i+len(target)] == target:
            total.append(string[i:i+len(target)])
            count += 1
    return total ,count
string = input("Enter the String:")
target = input("Enter the Substring:")
result,count = count_sub(string,target)
print(f"the string are :{result}")
print(f"count are :{count}")