def hello(s):
    str_str = ""
    for i in s:
        str_str= i + str_str
    return str_str
        
x = input("Enter the value:")
print(hello(x))
