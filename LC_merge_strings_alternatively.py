word1 = "ab"
word2 = "pqrs"
merged_string=""
max_length = max(len(word1),len(word2))
min_length = min(len(word1),len(word2))
for i in range(min_length):
    merged_string+=word1[i]
    merged_string+=word2[i]
if(i==len(word1)-1):
    for j in range(i+1,len(word2)):
        merged_string+=word2[j]
if(i==len(word2)-1):
    for j in range(i+1,len(word1)):
        merged_string+=word1[j]

print(merged_string)