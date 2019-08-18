class Solution:
    def dfs(self, digits, hashmap, level, out, res):
        if level == len(digits):
            res.append(out)
            return 
        str = hashmap[int(digits[level])]
        for i in range(len(str)):
            self.dfs(digits, hashmap, level + 1, out + str[i], res)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        hashmap =["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.dfs(digits, hashmap, 0, "", res)
        return res
