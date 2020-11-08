class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        mprices = prices + [prices[-1]]
        for i in reversed(range(len(prices))):
            mprices[i] = max(mprices[i + 1], prices[i])

        res = 0
        for i in range(len(prices) - 1):
            res = max(res, mprices[i + 1] - prices[i])
        return res
