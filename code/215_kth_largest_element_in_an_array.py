class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pos = self.partition(nums, left, right)
            if pos == k -1:
                return nums[pos]
            elif pos > k - 1:
                right = pos - 1
            else:
                left = pos  + 1
    def partition(self, nums, left, right):
        pivot, l, r = nums[left], left + 1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r

# quicksort
class Solution:
    def quicksort(self, nums, left, right) :
        if left > right:
            return
        pos = self.partition(nums, left, right)
        self.quicksort(nums, left, pos-1)
        self.quicksort(nums, pos+1, right)

    def partition(self, nums, left, right):
        pivot, l, r = nums[left], left + 1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
