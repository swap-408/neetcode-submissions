class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [[p[0]**2 + p[1]**2,p] for p in points]
        hp.sort()
        res = [hp[i][1] for i in range(k)]
        return res