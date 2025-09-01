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