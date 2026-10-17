class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d0 = 0
        d1 = 0
        res = 0
        for i in range(2,len(cost)+1):
            res = min(d1+cost[i-1],d0+cost[i-2])
            d0=d1
            d1=res
        return res