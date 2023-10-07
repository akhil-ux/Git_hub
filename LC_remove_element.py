from collections import Counter
nums = [3,2,2,3]
val = 3
k=0
x=nums.count(val)
print(x)
for i in range(x):
    nums.append("_")
    nums.remove(val)
for i in range(len(nums)):
    if(nums[i]!="_"):
        k+=1

