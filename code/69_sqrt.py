class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left, right = 0, x
        while left < right:
            mid = left + (right - left) //2
            if x // mid >=mid:
                left = mid + 1
            else:
                right = mid
        return right - 1
