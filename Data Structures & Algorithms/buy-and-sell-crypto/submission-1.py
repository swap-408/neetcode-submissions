class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = prices[0] 
        res = 0
        for i in range(1,len(prices)):
            res = max(prices[i]-cmin, res)
            cmin = min(cmin,prices[i])

        return res