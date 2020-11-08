class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [[-1, -1] for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                dp[i][0] = nums[i]
                dp[i][1] = 0
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
                dp[i][1] = max(dp[i - 1])

        return max(dp[len(nums) - 1])
