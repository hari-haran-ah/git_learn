


#factorial

def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
num = int(input("Enter the number:"))
print(fact(num))

#factorial

def fact(num):
    if num == 0 or num == 1:
        return 1
    return  num * fact(num-1)
num = int(input("Enter the number:"))
print(fact(num))


#fibonacci
def fabi(num):
    a,b= 0,1
    for _ in range(num):
        print(a,end = " ")
        a,b = b,a+b
    print()
num = int(input("Enter the number:"))
fabi(num)

#fibonacci
def fabi(num):
    if num <= 1:
        return num
    return fabi(num-1) + fabi(num-2)
num = int(input("Enter the number:"))
for i in range(num):
    print(fabi(i),end=" ")


#Q6. Remove Duplicates from a Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0
    left = 0
    for right in range(len(nums)):
        if nums[left] != nums[right]:
            left +=1
            nums[left] = nums[right]
        
    return left+1
nums = list(map(int,input("Enter the value with Space:").split()))
print(remove_duplicates(nums))

def remove_duplication(nums):
    list_nondupliaction=[]
    for i in nums:
        if i not in list_nondupliaction:
            list_nondupliaction.append(i)
    return list_nondupliaction
nums = list(map(int,input("Enter the value with Space:").split()))
print(remove_duplication(nums))


#Q7. Container With Most Water (Two Pointers)

def max_area(height):
    left,right = 0,len(height)-1
    max_area = 0
    
    while left <right:
        width = left - right
        h = min(height[left],height[right])
        area = width * h
        max_area = max(max_area,area)
        if height[left] < height[right]:
            left +=1
        else:
            right -= 1
    return max_area
height = list(map(int,input("Enter the height with Space:").split()))
print(max_area(height))


#Q8. Median of Two Sorted Arrays

def find_median_sorted_arrays(nums1,nums2):
    nums1.extend(nums2)
    
    nums1.sort()
    
    n = len(nums1)
    
    if n % 2 == 1:
        return float(nums1[n//2])
    else:
        mid1 = nums1[n//2 -1]
        mid2 = nums1[n//2]
        return (mid1 + mid2) / 2.0
num1= list(map(int,input("enter the string").split()))
num2= list(map(int,input("enter the string").split()))
print(find_median_sorted_arrays(num1,num2))




#Q10. Object-Oriented Programming


class Stack:
    def __init__(self):
        self.stack =[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.empty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.empty():
            return "Steck is empty"
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

myStack = Stack()
myStack.push('A')
myStack.push('B')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.empty())
print("Size: ", myStack.size())


# abstarct

from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def car_name():
        pass
    def car_model():
        pass

class susuzi(car):
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def car_model(self):
        return self.model
    def car_name(self):
        return self.name

obj = susuzi("susuzi","y21")
print(obj.car_name())
print(obj.car_model())

def reverse_str(str1):
    str_str = ""
    for i in str1:
        str_str = i +str_str
    return str_str
n = input("Enter the string :")
print(reverse_str(n))

def Even_odd(num):
    even = []
    odd = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd
num = list(map(int,input("Enter the Number separated by space:").split()))
even_list ,odd_list = Even_odd(num)

print(f"words -> {num} \n even list -> {even_list} \n odd list -> {odd_list}")

def Even_odd(num):
    even = []
    odd = []
    for i in range(num+1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd
num = int(input("Enetr the number"))
even_list ,odd_list = Even_odd(num)

print(f"words -> {num} \n even list -> {even_list} \n odd list -> {odd_list}")


def Even_odd(str1):
    vowels = []
    consonants = []
    for i in str1:
        if i in " ":
            continue
        if i in ['a','e','i','o','u']:
            vowels.append(i)
        else:
            consonants.append(i)
    return vowels , consonants
str1 = input("Enetr the string:")
vowels_list ,consonat_list = Even_odd(str1)

print(f"words -> {str1} \n vowels list -> {vowels_list} \n consonants list -> {consonat_list}")



def palindome_check(str1):
    str_str = ""
    str1 = str1.replace(" ","").lower()
    for i in str1:
        str_str = i +str_str
    return str_str == str1
n = input("Enter the string :")
if palindome_check(n):
     print(f"{n} is plaindrome")
else:
    print(f"{n} not in palindrome")
    


def factorial_num(num):
    if num  == 0 or num ==1:
        return 1
    return num * factorial_num(num-1)
n = int(input("Enter the Number :"))
print(factorial_num(n))

def factorial_num(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
n = int(input("Enter the Number:"))
print(factorial_num(n))


# Fact Series

def fabi(num):
    if num <= 1:
        return num
    return fabi(num-1) + fabi(num-2)

n = int(input("Enter the Number:"))
for i in range(n):
    print(f"{fabi(i)}",end = ' ')


def fabi(num):
    a ,b = 0,1
    for i in range(num+1):
        print(a,end= " ")
        a,b = b,a+b
n = int(input("Enter the value:"))
fabi(n)


# Armstrong Number

def armstrong(num):
    digit = str(num)
    power = len(digit)
    total = 0
    
    for i in digit:
        total += int(i) ** power
    return total == num
n = int(input("Enter the Number:"))
if armstrong(n):
    print(f"{n} this number is armstrong")
else:
    print(f'{n} this number not armstrong')

class Student:
    
    def __init__(self,name):
        self.name = name
        self.marks = []
        
    def add_mark(self,mark):
        self.marks.append(mark)
    
    def avg_mark(self):
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)
    
    def display(self):
        avg = self.avg_mark()
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {avg:.2f}")
        if avg >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
name = input("Enter the Name:")            
s1 = Student(name)
s1.add_mark(50)
s1.add_mark(200)
s1.display()



def Genarator():
        yield "hello gen"
        print("After yield")
        yield "hello after"

second = Genarator()
try:
    print(next(second))
    print(next(second))
    print(next(second))
except:StopIteration
print("No more value")

import sys
normal_list = [i for i in range(1,100000000)] # normal list
gen_list = (i for i in range(1,1000000000)) # genlist list

#print(next(gen_list))
#print(next(gen_list))

#print(list(gen_list))
print("gen_list",sys.getsizeof(gen_list))
print("Noraml_list",sys.getsizeof(normal_list))