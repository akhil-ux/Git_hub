arr = [1, 2, 1, 3, 2, 5]
hash = {}
for i in arr:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
value = {i for i in hash if hash[i]==1}
print(list(value))