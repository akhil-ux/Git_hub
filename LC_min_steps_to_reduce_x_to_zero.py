nums = [3,2,20,1,1,3]
x = 10
i,count=0,0

j=len(nums)-1
if(nums[j]>nums[i]):
    while(i!=j and x>0 and nums[j]<=x):
        x-=nums[j]
        count+=1
        j-=1
else:
     while(i!=j and x>0 and nums[i]<=x):
        x-=nums[i]
        count+=1
        i+=1
print(count)
