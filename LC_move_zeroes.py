nums = [ 1, 0, 3, 12,0,98,78,0,]
i = 0
j = len(nums)-1
while (i != j):
    if (nums[j] == 0):
        j -= 1

    if (nums[i] == 0 and nums[j] != 0):
        nums[i], nums[j] = nums[j], nums[i]
    if(nums[i]!=0):
        i+=1
    print(i,j)
    
print(nums)
