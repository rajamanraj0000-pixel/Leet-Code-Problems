class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = float("-inf")
        total = 0
        for i in range(0,len(nums)):
            total += nums[i]
            Max = max(Max,total)
            if total < 0:
                total = 0
        return Max