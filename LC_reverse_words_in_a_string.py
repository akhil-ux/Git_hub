s = "  hello world  "
temp_string=""
reverse_string=""
s=s[::-1]
for i in s:
    if(i!=" "):
        temp_string+=i
    if(i==" "):
        reverse_string+=temp_string[::-1]
        reverse_string+=" "
        temp_string=""
reverse_string+=temp_string[::-1]
print(reverse_string)