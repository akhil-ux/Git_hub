n=5
bit=[0]*(n+1)
count_of_bits=[]
for i in range(n+1):
    x=bin(i)[2:]
    bit[i]=x.count('1')
print(bit)