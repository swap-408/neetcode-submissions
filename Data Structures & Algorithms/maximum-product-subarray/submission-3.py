class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpos = nums[0]
        maxneg = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxpos, maxneg = maxneg, maxpos
            maxpos = max(nums[i],maxpos*nums[i])
            maxneg = min(nums[i],maxneg*nums[i])
            
            res = max(res, maxpos)
        return res