class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(0,len(nums)):
            sum += nums[i]

        return (len(nums)*(len(nums)+1))//2 - sum