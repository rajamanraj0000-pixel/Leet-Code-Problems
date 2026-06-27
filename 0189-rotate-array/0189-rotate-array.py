class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def rotate(nums,left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

        rotate(nums,len(nums)-k , len(nums)-1)
        rotate(nums,0,len(nums)-k-1)
        rotate(nums,0,len(nums)-1)