class Solution:
    def countAndSay(self, n: int) -> str:
        if n <=0 : return ""
        res = "1"
        n -= 1
        while n:
            cur = ""
            i = 0
            while i < len(res):
                cnt = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    cnt += 1
                    i += 1
                cur += str(cnt) + res[i]
                i += 1

            res = cur
            n -= 1
        return res
