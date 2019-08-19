# 两个变量left和right分别表示剩余左右括号的个数
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, "", res)
        return res
    
    def dfs(self, left, right, out, res):
        if left > right: return
        if left == 0 and right == 0: res.append(out)
        else:
            if left > 0: self.dfs(left - 1, right, out + '(', res)
            if right > 0: self.dfs(left, right - 1, out + ')', res)
