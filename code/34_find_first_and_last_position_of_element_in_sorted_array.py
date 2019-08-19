class Solution:
    def helper(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = self.helper(nums, target)
        if pos == -1:
            return [-1, -1]
        
        l, r = pos, pos
        while l > 0 and nums[l] == nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and nums[r] == nums[r+ 1]:
            r += 1
        return [l, r]
