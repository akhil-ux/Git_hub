nums = [3,1,-2,-5,2,-4]
negative = []
non_negative = []
for i in nums:
    if i >= 0:
        non_negative.append(i)
    else:
        negative.append(i)
j =0
k=0
for i in range(len(nums)):
    if i%2==0:
        nums[i]= non_negative[j]
        j+=1
    else:
        nums[i]=negative[k]
        k+=1
print(nums)