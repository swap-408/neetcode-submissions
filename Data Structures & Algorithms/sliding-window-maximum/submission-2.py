class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1: return nums
        heap = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        res = [-heap[0][0]]
        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            while ((i-k)<heap[0][1]<=i) == False:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res