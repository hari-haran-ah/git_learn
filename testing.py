#anagram

def ana_gram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2)

str1 = input("enter the string:")
str2 = input("ented the anagram_string:")
print(ana_gram(str1,str2))



#palindrome
def palindrome(n):
    str_str = ""
    cleaned = n.lower().replace(" ", "")
    for i in cleaned:
        str_str = i + str_str
        
    return str_str == cleaned

input_value = input("enter the value :")
if(palindrome(input_value)):
    print("Yes")
else:
    print("No")



#prime Number
def prime_num(n):
    if n <=1:
        return False
    for i in range(2,int(n**0.5 +1)):
        if n % i == 0:
            return False
    return True
def show_prime(num):
    primes = []
    for i in range(2,num + 1):
        if prime_num(i):
            primes.append(i)
    return primes

input_value =int(input("enter the Number:"))

print(show_prime(input_value))


# reverse the string
def reverse_string(s):
    str_str = ""
    for i in s:
        str_str = i + str_str
    return str_str
input_value=input("Enter the string:")
print(reverse_string(input_value))



# reverse using the slice operator
def reverse_slice(s):
    s = s.lower().replace(" ","")
    return s[::-1]
input_value = input("Enter the String:")
print(reverse_slice(input_value))

#fabinacci series
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
input_value =int(input("Enter the number:"))
for i in range(input_value):
    print(f"{fib_recursive(i)}",end=" ")



# factorial iteration
def factorial_iter(n):
    result= 1
    for i in range(1,n+1):
        result *= i
    return result
input_value =int(input("enter the number:"))
print(factorial_iter(input_value))


# factorial recursion
def factorial_iters(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_iters(n-1)
input_value =int(input("Enter the NUmber:"))
print(factorial_iters(input_value))


# frequency in the string
def char_frequency(s:str)-> dict:
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] =1
    return freq
input_value=input("Enter the String:")
print(char_frequency(input_value))


#second largest number

def second_largest(n):
    return (sorted(set(n))[-2])

input_value=list(map(int,input("Enter numbers separated by space:").split()))
print(second_largest(input_value))

#remove duplication without using the set
def remove_duplicate(n):
    result=[]
    for i in n:
        if i in result:
            continue
        else:
            result.append(i)
    return result
input_value = list(map(int,input("Enter NUmbers separated by space:").split()))
print(remove_duplicate(input_value))

#remove duplication with using the set
def remove_duplication(n):
    return list(set(n))

input_value=list(map(int,input("Enter NUmbers separated by space:").split()))
print(remove_duplication(input_value))

#swap two numbers without using temp
def swap_num(num1,num2):
    print("Before swapping: a =", num1, "b =", num2)
    num1,num2 = num2,num1
    return num1 ,num2
input_value1=int(input("enter the number1:"))
input_value2=int(input("enter the NUmber2:"))
print(swap_num(input_value1,input_value2))

#swap two numbers with using temp
def swap_num(num1,num2):
    print("Before swapping: num1 =", num1, "num2 =", num2)
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2
input_value1=int(input("Enter the Value1:"))
input_value2=int(input("Enter the value2:"))

print(swap_num(input_value1,input_value2))

#sum of digit
def num_of_digit(num):
    num1=0
    for i in str(num):
        num1 += int(i)
    return num1
n = int(input("Enter the number:"))
print(num_of_digit(n))


#sum of digit
def num_of_digit(num):
    total=0
    while num > 0:
        total += num % 10
        num//=10
    return total
n = int(input("Enter the Value:"))
print(num_of_digit(n))

#reverse the integer
def reverse_int(num):
    str_str = ""
    for i in str(num):
        str_str = i + str_str
    return int(str_str)
n = (input("enter the Number:"))
print(reverse_int(n))


#reverse the integer
def reverse_int(num):
    return int(str(num)[::-1])

n = int(input("Enter the Number: "))
print(reverse_int(n))


#Common Elements in Two Lists
def two_list(num1,num2):
   return sorted(list(set(num1) | set(num2)))
   num1.extend(num2)
   return num1

list1 = list(map(int,input("Enter the list:").split()))
list2 = list(map(int,input("Enter the list:").split()))
print(two_list(list1,list2))


#square root of the value
def square_num(n):
    result = []
    for i in range(1,n+1):
        result.append(i**2)
    return result
N=int(input("Enter the number:"))
print(square_num(N))


#file read count the words
def read_file(filename):
    freq={}
    with open(filename,"r") as f:
        words = f.read().split()
        for word in words:
            if word in freq:
                freq[word] +=1
            else:
                freq[word] =1
    return freq
n=input("Enter Your Filename:")
print(read_file(n))

#Right-Angled Triangle
def triangle_right(n):
    for i in range(1,n+1):
        print('*' * i)
n=int(input("Enter the nUmber:"))
triangle_right(n)

def triangle_right(n):
    for i in range(n,0,-1):
        print('*' * i)
n=int(input("Enter the nUmber:"))
triangle_right(n)

def triangle_right(n):
    for i in range(n):
        print('*' * n)
n=int(input("Enter the nUmber:"))
triangle_right(n)

def diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))

n=int(input("Enter the nUmber:"))
diamond(n)

def number_loop(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
n=int(input("Enter the nUmber:"))
number_loop(n)

def number_loop(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
n=int(input("Enter the nUmber:"))
number_loop(n)

def number_loop(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
n=int(input("Enter the nUmber:"))
number_loop(n)

def number_loop(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(i,end=" ")
        print()
n=int(input("Enter the nUmber:"))
number_loop(n)

# use with statement (it auto-closes file).
with open("hello.txt","w") as f:
    f.write("hello COntent was Reset added the new text\n")
print("Content reset sucessfully")
    
with open("hello.txt" ,"a") as f:
    f.write("Added the new content After writhing")
print("content writing sucessfully")

with open("hello.txt" ,"r") as f:
    read= f.read()
    print("file content")
    print(read)
    
with open("hello.txt" ,"r") as f:
    for line in f:
        print("line are",line.strip())

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

def count_words_each_line(filename):
    with open(filename,"r") as f:
        read_no = 1
        for line in f:
            words=line.split()
            print(f"Line {read_no}: {len(words)} words -> {words}")
            read_no +=1

count_words_each_line("sample.txt")

# anagram
def anagram_test(str1, str2):
    
    freq1= {}
    freq2= {}
    
    for ch in str1:
        if ch in " ":
            continue
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in str2:
        if ch in " ":
            continue
        if ch in freq2:
            freq2[ch] +=1
        else:
            freq2[ch] =1
    
    return freq1 == freq2

str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")
print(anagram_test(str1, str2))

def vowels_consonants(str1):
    vowels = 0
    consonants = 0
    cleaned=str1.replace(" ","").lower()
    for i in cleaned:
        if i == 'a' or i== "e" or i == "o" or i == 'i' or i == 'u':
            vowels += 1
        else:
            consonants +=1
    return vowels,consonants
n=input("Enter the String:")
v,c = vowels_consonants(n)
print(f"Vowels = {v}, Consonants = {c}")

# even or odd
def even_odd(n):
  if n % 2 == 0:
      return True
  else:
      return False
      
n = int(input("ENter the nUmber:"))
if(even_odd(n)):
    print(f" {n} is Even")
else:
    print(f"{n} is odd")

# even or odd
'''
It is divisible by 4.
But if it is divisible by 100, then it is NOT a leap year.
Unless it is divisible by 400 → then it is a leap year.
'''
def leap_year(n):
  if (n % 4 == 0 and n % 100 != 0) or  n % 400 == 0:
      return "leap year"
  else:
      return "Not Leap Year"
  
n = int(input("ENter the nUmber:"))
print(leap_year(n))

def fibonacci_iterative(n):
    a ,b = 0,1
    for _ in range(n):
        print(a,end=" ")
        a,b = b,a+b
num = int(input("Enter the number of terms: "))
fibonacci_iterative(num)


#armstrong numberx 
def is_armstrong(num: int) -> bool:
    digit = str(num)
    power = len(digit)
    total =0
    
    for d in digit:
        total += int(d) ** power
    return total == num


num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
    
    
# strong NUmber

def factoral(n):
    fact =1
    for i in range(1,n+1):
        fact *=i
    return fact
def is_strong(num):
    original = num
    total =0
    while num > 0:
        digit = num % 10
        total +=factoral(digit)
        num//=10
    return total == original

n = int(input("Enter a number: "))
if is_strong(n):
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is NOT a Strong Number")

# Perfect Number Check

def perfect_num(num):
    if num <= 0:
        return False
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i
    return num == total

n = int(input("Enter a number: "))
if perfect_num(n):
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")

#decorators

def decor_tor(func):
    def wrapper(num,num1):
        print("befor sum the number")
        func(num,num1)
        print("After the sum the number")
    return wrapper
@decor_tor
def sum(num,num1):
    print(num + num1)

@decor_tor
def minous(num,num1):
    print(num - num1)


sum(10,20)
minous(10,10)

# method overloading

class hai:
    def add(self,n1:int,n2:int):
        print("First")
        return n1 + n2
    
    def add(self,n1:int,n2: int=0):
        print("Second")
        return n1 - n2

obj = hai()
print(obj.add(10))
print(obj.add(20,10))

# method overloading

class hai:
    def add(self, n1:int, n2:int=None):
        if n2 is None:
            print("first")
            return n1
        else:
            print("second")
            return n1 +n2

obj = hai()
print(obj.add(10))
print(obj.add(20,10))

# method overloading
class hai:
    def add(self,*args):
        if len(args) == 1:
            print("first")
            return args[0]
        elif len(args) ==2:
            print("second")
            return args[0] + args[1]

obj = hai()
print(obj.add(10))
print(obj.add(20,10))


#methos overriding
class Mathoperation:
    def add(self,n:int,n2 :int):
        return n + n2
    
class Mathfunction(Mathoperation):
    def add(self,n:int,n2 :int):
        return n - n2
    
obj = Mathfunction()
print(obj.add(10,20))
    
    
class prime_check:
    
    def __init__(self,number):
        self.number = number
        
    def check_primme(self):
        n = self.number
        if n <= 1:
            return False
        for i in range(2,int(n ** 0.5 +1)):
            if n % i == 0:
                return False
        return True
    
    def display(self):
        prime = self.check_primme()
        if prime:
            print(f"{self.number} this number is prime")
        else:
            print(f"{self.number} this number is not prime")


num = int(input("Enter the Value:"))
prime = prime_check(num)
prime.display()



def Genarator():
    yield "hello gen"
    print("After yield")
    yield "hello after"

second = Genarator()
print(next(second))
print(next(second))
     


# encapulation
class RepeatTest:
    def __init__(self,name,password):
        self.name = name
        self.__password = password
    
    #getter
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.__password
    
    #setter
    
    def set_name(self,name):
        self.name = name
    
    def set_password(self,password):
        self.__password = password
    
    
obj = RepeatTest("Hari","****")
print(obj.get_name())
print(obj.get_password())
obj.set_name("Hariharan A")
obj.set_password("*******")
print(obj.get_name())
print(obj.get_password())


#abstract

from abc import ABC , abstractmethod

class car(ABC):
    
    @abstractmethod
    def car_name(self):
        print("default")
        pass
    
    @abstractmethod
    def car_model(self):
        pass

class susuzi(car):
    def __init__(self,carname,carmodel):
        self.carname = carname
        self.carmodel = carmodel
    def car_name(self):
        return self.carname
    def car_model(self):
        return self.carmodel

obj = susuzi("susuzi","y21")
print(obj.car_name())
print(obj.car_model())


# polymorphism

# compile time polymorphism

def add(*args):
    result = 0
    for i in (args):
        result += i
    return result


print(add(2,34,45,56,6,67,78,8))

def add(a,b=0):
    return a+b
try:
    print(add(10))
    print(add(10,20))
    print(add(10,20,30))
except: StopIteration
print("To more inputs")

#run time polymorphism
class plus:
    def add(self,a,b):
        return a+b
    def minuss(self,a,b):
        return a-b
class minus(plus):
    def add(self,a,b):
        return a+b

obj = minus()
print(obj.add(10,5))
print(obj.add(10,5))
print(obj.minuss(10,5))


#inheritance
# single level inheritance
class Parent:
    def parent_method(self):
        return "This is parent method"
class Child(Parent):
    def child_method(self):
        return "This is child method"
obj = Child()
print(obj.parent_method())
print(obj.child_method())


#multi level inheritance
class GrandParent:
    def grandparent_method(self):
        return "This is grandparent method"
class Parent(GrandParent):
    def parent_method(self):
        return "This is parent method"
class Child(Parent):
    def child_method(self):
        return "This is child method"
obj = Child()
print(obj.parent_method())
print(obj.child_method())
print(obj.grandparent_method())


#heriacical
class Parent:
    def parent_method(self):
        return "This is parent method"
class Child1(Parent):
    def child1_method(self):
        return "This is child1 method"
class Child2(Parent):
    def child2_method(self):
        return "This is child2 method"
obj1 = Child1()
obj2 = Child2()
print(obj1.parent_method())
print(obj2.parent_method())
print(obj2.child2_method())


# multiple inheritance
class Father:
    def father_method(self):
        return "This is father method"
class Mother:
    def mother_method(self):
        return "This is mother method"
class Child(Father,Mother):
    def child_method(self):
        return "This is child method"
obj = Child()
print(obj.father_method())
print(obj.mother_method())
print(obj.child_method())
def number(num):
    
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

num = int(input("Enter the number:"))
number(num)


# First Non-Repeating Character
def word_count(str1):
    freq ={}
    words = str1.lower()
    for word in words:
        if word in freq:
            freq[word] +=1
        else:
            freq[word] = 1
    for word in words:
        if freq[word] == 1:
            return word
        
    return None
string = input("Enter the string:")
print(word_count(string))


import datetime

# 1. Get current date & time
now = datetime.datetime.now()
print("Current Date & Time:", now)

# 2. Get only date
today = datetime.date.today()
print("Today:", today)

# 3. Formatting date
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)

# 4. Create custom date
custom_date = datetime.date(2025, 9, 6)
print("Custom Date:", custom_date)

# 5. Difference between dates
future = datetime.date(2025, 12, 31)
delta = future - today
print("Days until 2025 ends:", delta.days)

now = datetime.date(2025 ,12 ,6)
delta = now - today
print(delta.days)

def common_divisor(num1 , num2):
    if num1 and num2 == 0:
        return "GCD not possible"
    while num2 !=0:
        num1,num2 = num2,num1 % num2
    return num1
n1 = int(input("Enter the First Number:"))
n2 = int(input("Enter the Second Number:"))
print(f"The GCD of {n1} and {n2} is {common_divisor(n1,n2)}")


# list comprehension
even_odd = ["Even" if i % 2 == 0  else "odd" for i in range(6)]
print(even_odd)

# Nested list comprehension
matrix = [(i,j) for i in range(3) for j in range(3)]
print(matrix)

even_odd = lambda x:"Even" if x %2 == 0 else "Odd"
print(list(map(even_odd, range(6))))

# Using filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(even_numbers)

nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


f = lambda x: x + 1
print(f.__name__)

#map
result = list(map(lambda x: x * 2, range(0,6+1,2)))
print(result)

#filter
result = list(filter(lambda x:x % 2==0,range(9+1+2) ))
print(result)

import turtle

t = turtle.Turtle()

# A circle is just many tiny forward + turn movements
for i in range(10):       # 360 small steps
    t.forward(100)           # move a little forward
    t.right(1000) # turn a little

turtle.done()


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


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element = matrix[1-1][2] # Row 1, Column 2 -> 6
print(f"Element at [0][2] is: {element}")

# Iterating through the matrix
for row in matrix:
    print(row)
    
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())
#even in the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


num_rows = len(matrix)
num_cols = len(matrix[0])
print(f"Matrix has {num_rows} rows and {num_cols} columns.\n")

even_count = 0
even_numbers_found = []
for i in range(num_rows):
    for j in range(num_cols):
        element = matrix[i][j]
        if element % 2 == 0:
            even_count += 1
            even_numbers_found.append(element)
            print(f"Even number found: {element} at position ({i}, {j})")
            
print(f"\nTotal even numbers found: {even_count}")
print(f"The even numbers are: {even_numbers_found}")

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        n= len(nums1)
        if n % 2 == 1:
            return float(nums1[n // 2])
        else:
            mid1 = nums1[n // 2 - 1]
            mid2 = nums1[n // 2]
            return (mid1 + mid2) / 2.0


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0
        while left < right:
            width = right - left
            h = min(height[left],height[right])
            max_area= max(max_area, width * h)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1
