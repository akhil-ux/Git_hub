from itertools import combinations
nums = [-1,0,1,2,-1,-4]
k=[]
for i in combinations(nums,3):
    print(i)
    if((i[0]+i[1]+i[2])==0 ):
        k.append(i)
print(k)
