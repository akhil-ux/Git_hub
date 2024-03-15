nums = [4, 2, 5, 7]
even = []
odd = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
j=0
k=0
for i in range(len(nums)):
    if(i%2==0):
        nums[i]=even[j]
        j+=1
    else:
        nums[i]=odd[k]
        k+=1
print(nums)
