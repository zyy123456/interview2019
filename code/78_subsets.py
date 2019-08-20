class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,out = [], []
        nums.sort()
        self.dfs(nums, 0, out, res)
        return res
    
    def dfs(self, nums, pos, out, res):
        res.append(out[:])
        for i in range(pos, len(nums)):
            out.append(nums[i])
            self.dfs(nums, i + 1, out, res)
            out.pop()
