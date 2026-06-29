class Solution:
    def twoSum(self , nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
            if remaining in dic:
                return (dic[remaining],i)
            dic[nums[i]] = i