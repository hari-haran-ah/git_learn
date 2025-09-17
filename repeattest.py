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
    
