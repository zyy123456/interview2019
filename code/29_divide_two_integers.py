class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0 or (dividend == -pow(2, 31) and divisor==-1): return pow(2, 31) - 1
        sign = (dividend < 0) ^ (divisor < 0)
        res = 0
        m, n = abs(dividend), abs(divisor)
        if n == 1:
            return m if sign == 0 else -m
        while  m >= n:
            t, p = n, 1
            while m >= (t << 1):
                t <<= 1
                p <<= 1
            res += p
            m -= t
        return res if sign == 0 else -res
