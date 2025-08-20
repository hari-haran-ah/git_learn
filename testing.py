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
    return list(set(num1) & set(num2))

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
        read_no =1
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


