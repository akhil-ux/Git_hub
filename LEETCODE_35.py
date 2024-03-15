nums = [1, 3, 5, 6]
target = 5
low = 0
high = len(nums)-1
while (low != high):
    mid = (low+high)//2
    if (nums[mid] > target):
        high = mid-1
    if (nums[mid] < target):
        low = mid+1
    if (nums[mid] == target):
        print(mid)
