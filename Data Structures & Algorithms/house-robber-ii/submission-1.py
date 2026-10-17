class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        rob1, rob2 = 0,0
        for i in range(len(nums)-1):
            temp1 = max(rob1+nums[i], rob2)
            rob1 = rob2
            rob2 = temp1
        rob1, rob2 = 0,0
        for i in range(1,len(nums)):
            temp2 = max(rob1+nums[i], rob2)
            rob1 = rob2
            rob2 = temp2

        return max(temp1,temp2)
