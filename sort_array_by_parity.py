nums = [3,1,2,4]
odd=[]
even=[]
for i in nums:
    if(i%2!=0):
        odd.append(i)
    else:
        even.append(i)
print(odd+even)