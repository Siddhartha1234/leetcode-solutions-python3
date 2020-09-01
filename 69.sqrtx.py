class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x

        while lo < hi:
            mid = (lo + hi + 1) >> 1

            if mid * mid <= x:
                lo = mid
            else:
                hi = mid - 1

        return lo
