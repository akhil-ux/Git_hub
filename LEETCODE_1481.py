arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
l = list(freq.values())
l.sort()
for i in range(len(l)):
    if l[i]<=k:
        k-=l[i]
        l[i]=-1
    else:
        break
co =0
for i in l:
    if i!=-1:
        co+=1
print(co)
print(l)