class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l,r = 1, piles[-1]

        res = r
        while l<=r:
            m = l + (r-l)//2
            need = self.eat(piles,m)
            if need>h: l = m+1
            else:
                res = min(res, m)
                r = m-1
        return res
    def eat(self, piles, m):
        need = 0
        for i in piles:
            need += ((i//m+1) if i%m!=0 else i//m)
        return need