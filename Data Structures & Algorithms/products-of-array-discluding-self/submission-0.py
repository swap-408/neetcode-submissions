class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        totalProduct = 1
        for num in nums:
            if num == 0: zeroCount += 1
            else: totalProduct *= num
        
        if zeroCount > 1: return [0]*len(nums)
        
        res = []
        if zeroCount == 1:
            res = [0 if num!= 0 else totalProduct for num in nums]
            return res
        for num in nums:
            res.append(totalProduct//num)
        return res
