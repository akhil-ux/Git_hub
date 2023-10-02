import math

s = "haveaniceday"
def encryption(s):
    s = s.replace(" ", "")
    Length = len(s)
    root = math.sqrt(Length)
    row = int(root)
    column = math.ceil(root)  # Use math.ceil() instead of __ceil__()
    while row * column < Length:
        if row * column < Length and row < column:
            row += 1
        elif row * column < Length and column < row:
            column += 1
    
    x = row
    y = column
    print(row, column)
    arr = [[""] * column for _ in range(row)]  # Use list comprehension
    k = 0
    for i in range(x):
        for j in range(y):
            if k < Length:
                arr[i][j] = s[k]
                k += 1
    new_string=""
    for j in range(column):
        if(j !=0):
            new_string+=" "
        for  i in range(row):
            new_string+=arr[i][j]
    print(new_string)