#prime number
def is_prime(num):
    if num <=1:
        return False
    for i in range(2,int(num**0.5 +1)):
        if num % i ==0:
            return False
    return True
num = eval(input("Enter the number:"))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
    
#Q2. Palindrome String

def palindrome(str1):
    cleaned = str1.replace(" ","").lower()
    str_str = ""
    for i in cleaned:
        if i in " ":
            continue
        else:
         str_str= i+str_str
    return str_str == cleaned
str1=eval(input("Enetr the string:"))
if palindrome(str1):
    print(f"{str1} is palindrome")
else:
    print(f"{str1} is not palindrome")
    
#Q3. Fibonacci Series

def fabinacci(num):
    if num <= 1:
        return num
    return fabinacci(num-1) +fabinacci(num-2)
num=eval(input("Enetr the Number:"))
print("Fabinacci series Are:")
for i in range(num+1):
    print(f"{fabinacci(i)}",end=" ")

#Q4. Anagram Test

def anagaram(str1:str,str2:str)-> dict:
    freq1={}
    freq2={}
    
    for ch in str1:
        if ch in " ":
            continue
        if ch in freq1:
            freq1[ch] +=1
        else:
            freq1[ch] =1
    for ch in str2:
        if ch in " ":
            continue
        if ch in freq2:
            freq2[ch] +=1
        else:
            freq2[ch] =1
    return freq1 == freq2

str1 = eval(input("Enter the string1:"))
str2 = eval(input("Enter the String2:"))

if anagaram(str1,str2):
    print(f"{str1} and {str2} is anagram")
else:
    print(f"{str1} and {str2} is not anagram")

#Q6. Leap Year Range

def leap_tear(year):
    if (year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
year = eval(input("enter the Year:"))
if leap_tear(year):
    print(f"{year} this year leap year")
else:
    print(f"{year}this year not a leap year")
    
#Q7. Word Frequency in File

def Word_Frequency(filename):
    with open(filename,"r") as f:
        freq ={}
        words= f.read().split()
        for i in words:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] =1
        return freq
file_location = eval(input("Enter the file location:"))
print(Word_Frequency(file_location))


#Q8. Vowels & Consonants
def vowles_con(str1):
    vowles = 0
    consonents =0
    for ch in str1:
        if ch in ['a','e','i','o','u']:
            vowles +=1
        elif ch.isalpha():
            consonents +=1
    return vowles,consonents

str1=eval(input("Enter the String:"))
v,c =vowles_con(str1)

print(f"Vowels ->{v}\n Consonants -> {c}")

#Q9. Number Pattern

def num_series(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(i,end= " ")
        print()
num = eval(input("Enter the NUmber:"))
(num_series(num))

#Q10. Even & Odd in List

def list_even_odd(list_item):
    even_list = []
    odd_list = []
    for _ in list_item:
        if _ % 2 == 0:
            even_list.append(_)
        else:
            odd_list.append(_)
    return even_list,odd_list
num = list(map(int,input("Enter the number:").split()))
even,odd = list_even_odd(num)
print(f"This the total list ->{num} \n Even list are -> {even} \n Odd list are -> {odd}")


