class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = [0]*2001
        m = -2000
        for n in nums:
            count[1000+n] += 1
            m = max(m,1000+n)
        
        for i in range(m,-1,-1):
            if count[i]<k:
                k -= count[i]
                continue
            else:
                return i-1000
        return 0