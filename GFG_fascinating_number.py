n=190
l=[]
flag=1
s=str(n)
s+=str(n*2)
s+=str(n*3)
for i in s:
    l.append(int(i))
freq_array=[0]*10
for i in l:
    freq_array[i]+=1
print(freq_array,l)
for i in range(1,len(freq_array)):
    if(freq_array==0 or freq_array[i]>1):
        flag=1
if(flag==1):
    print(False)
else:
    print(True)

