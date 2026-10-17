class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minhp = nums
        self.k = k
        heapq.heapify(self.minhp)

        while len(self.minhp) > k:
            heapq.heappop(self.minhp)

    def add(self, val: int) -> int:
        heapq.heappush(self.minhp,val)
        while len(self.minhp) > self.k:
            heapq.heappop(self.minhp)
        return self.minhp[0]
