chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
temp_set=set(chars)
freq_array=[0]*(len(set(chars)))
for i in chars:
    freq_array[abs(97-ord(i))]+=1
k=""
for i in range(len(freq_array)):
    if(freq_array[i]==1):
        pass
    k+=str(freq_array[i])
print(len(k)+len(temp_set))
