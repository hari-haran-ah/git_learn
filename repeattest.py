
    
#file char check
def check_word(filename):
    with open(filename, "r") as f:
        words = f.read().split()
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        for word in words:
            if freq[word] == 1:
                return word
        return None
filename = input("Enter the file Name:")
result = check_word(filename)
print(result)


# word len each row
def word_len_each_row(filename):
    with open(filename , "r") as f:
        line_no = 0
        for line in f:
            words = line.split()
            print(f"{words}Line num{line_no} ->{len(words)}")
            line_no +=1

filename = input("Enter the file name:")
word_len_each_row(filename)
            