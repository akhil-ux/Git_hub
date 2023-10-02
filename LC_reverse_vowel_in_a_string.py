s ="aA"
s=list(s)
k=['a','i','e','u','o','A','E','I','O','U']
x=""
i=0
j = len(s)-1
while(i<j):
    if(s[i] in k and s[j] in k):
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    elif(s[i] in k):
        j-=1
    else:
        i+=1
for i in s:
    x+=i
print(x)
