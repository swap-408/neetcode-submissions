class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(0,len(nums)):
            d = (target-nums[i])
            if d in dic and dic[d] != i:
                return [dic[d],i]
            else:
                dic[nums[i]] = i

        return [0,0]