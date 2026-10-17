class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return max(nums[0],nums[1])

        mprofit0 = nums[0]
        mprofit1 = max(nums[0],nums[1])
        mprofit = 0
        for i in range(2,n):
            mprofit = max(nums[i]+mprofit0, mprofit1)
            mprofit0 = mprofit1
            mprofit1 = mprofit
        return mprofit