import functools

class Solution:
    def cmp(self, a, b):
        return 1 if str(b) +str(a) > str(a) + str(b) else -1
    
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=functools.cmp_to_key(self.cmp))
        res = ''
        for num in nums:
            res += str(num)
        return '0' if res[0] == '0' else res
