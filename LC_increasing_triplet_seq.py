
nums = [3,2,1]
if(len(nums)<3):
    print(-1)
i = 0
j=1
k=2
for k in range(2,len(nums)):
    if(nums[i]<nums[j] and nums[j]<nums[k]):
        print(True)
    i+=1
    j+=1
    k+=1