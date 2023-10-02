nums =  [0,0,0,0,0]
product_list=[0]*len(nums)
product=1
count=0
for i in range(len(nums)-1,-1,-1):
    if(nums[i]==0):
        count+=1
        continue
    product=product*(nums[i])
if(count>1):
    return product_list
for i in range(len(nums)):
    if(count==0):
        product_list[i]=product//nums[i]
        print(product,nums[i])
    if(count==1 and nums[i]!=0):
        product_list[i]=0
    if(nums[i]==0):
        product_list[i]=product
if(nums==product_list):
    print(nums)
else:
    print(product_list)
