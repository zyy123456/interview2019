class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        mp = {}
        left, cnt, minlen = 0, 0, float('inf')  
        for char in t:
            mp[char] = mp.get(char, 0) + 1
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = 0
            mp[s[i]] -= 1
            if mp[s[i]] >= 0: cnt += 1
            while cnt == len(t):
                if minlen > i - left + 1:
                    minlen = i - left + 1
                    res = s[left: left + minlen]
                mp[s[left]] += 1
                if mp[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res
