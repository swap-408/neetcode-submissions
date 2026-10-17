class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1: return stones[0]
        hp = [-s for s in stones]
        heapq.heapify(hp)
        while len(hp)>=2:
            A = -heapq.heappop(hp)
            B = -heapq.heappop(hp)
            if A==B: continue
            heapq.heappush(hp, - abs(A-B))
        
        if len(hp)==0: return 0
        return -heapq.heappop(hp)
        
        i