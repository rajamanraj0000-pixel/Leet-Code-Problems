class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        pos_ind = 0
        neg_ind = 1
        for i in range(0,len(nums)):
            if nums[i] >= 0:
                result[pos_ind] = nums[i]
                pos_ind += 2
            else:
                result[neg_ind] = nums[i]
                neg_ind += 2
        return result
            