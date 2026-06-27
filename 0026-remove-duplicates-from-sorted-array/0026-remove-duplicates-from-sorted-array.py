class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        for i in range(0,len(nums)):
            dic[nums[i]] = 0

        j = 0
        for k in dic:
            nums[j] = k
            j += 1

        return j