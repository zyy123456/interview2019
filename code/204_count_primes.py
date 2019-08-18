class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        prime = [True] * n
        for i in range(2, n):
            if not prime[i]:
                continue
            res += 1
            j = 2
            while i * j < n:
                prime[i*j] = False
                j += 1
        return res
