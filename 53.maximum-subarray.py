class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (all(x < 0 for x in nums)):
            return max(nums)

        csum = 0
        ans = 0
        for x in nums:
            csum += x
            if csum < 0:
                csum = 0

            ans = max([csum, ans])

        return ans
