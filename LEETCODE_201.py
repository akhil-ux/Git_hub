import decimal
left = 5
right = 7
result = left
j = left
for i in range(left+1, right+1):
    x = bin(j)[2:]
    y = bin(i)[2:]
    result = int(x) and int(y)
    j += 1
print(decimal.Decimal(str(result)))
