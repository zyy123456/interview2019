class Solution:        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        left, maxlen = 0, 1
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = (s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]))
                if dp[j][i] and maxlen < i - j + 1: 
                    maxlen = i - j + 1
                    left = j
        return s[left: left+maxlen]
