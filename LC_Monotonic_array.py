# nums=[1,3,2]
nums=[2,2,2,2]
monotonic_ascending=0
monotonic_descending=0
monotonic_same=0

for i in range(len(nums)-1):
    if(nums[i]<nums[i+1]):
        monotonic_ascending+=1
        
    elif(nums[i]>nums[i+1]):
        monotonic_descending+=1
    else:
        monotonic_same+=1
if(monotonic_descending==0 or monotonic_ascending==0):
    print(True)
else:
    print(False)
