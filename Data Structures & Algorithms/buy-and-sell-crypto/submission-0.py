class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minarr = [prices[0]]
        prev = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] <= prev:
                minarr.append(prices[i])
                prev = prices[i]
            else:
                minarr.append(prev)
        res = 0
        for i in range(0,len(minarr)):
            res = max(prices[i]-minarr[i], res)

        return res