class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i + 1] > nums[i]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i]: break
                nums[i], nums[j] = nums[j], nums[i]
                self.reverse(nums, i + 1, n - 1)
                return
        self.reverse(nums, 0, n-1)
        
    def nextPermutation2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] >= nums[i+1]: i -= 1
        if i >=0:
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1, len(nums)-1)
                
