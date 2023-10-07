nums = [0,1,2,2,4,4,1]

n=len(nums)
k=[0]*(max(nums)+1)
j=[]
for i in nums:
    if i%2==0:
        k[i]+=1
maxx=max(k)
for i in range(len(k)):
    if(k[i]==maxx):
        j.append(i)
j.sort()
print(j[0])
