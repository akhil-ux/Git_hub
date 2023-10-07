candies = [4,2,1,1,2]
extraCandies = 1
m1=max(candies)
for i in range(len(candies)):
    candies[i]+=extraCandies
    if(candies[i]>=m1):
        candies[i]=True
    else:
        candies[i]=False
print(candies)