chars = ["a", "a", "b", "b", "c", "c", "c"]
freq = {}
for i in chars:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
final_array = []
keys = []
values = []
for  i in freq.values():
    values.append(i)
for i in freq.keys():
    keys.append(i)
print(values,keys)
