class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        res = ""
        for j in range(len(strs[0])):
            c = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != c:
                    return res
            res += c
        return res
                    
