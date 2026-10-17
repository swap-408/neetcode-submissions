class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:  return 1
        if n==2: return 2

        d1 = 1
        d2 = 2
        res = 0
        for i in range(3,n+1):
            res = d1+d2
            d1 = d2
            d2 = res
        return res