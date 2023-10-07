from collections import Counter
s="hhello"
x=0
for i in s:
    x=i.count(s)
    if(x==1):
        print(i)
        break