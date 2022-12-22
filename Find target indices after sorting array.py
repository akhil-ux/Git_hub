class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                l1.append(i)
        return l1
