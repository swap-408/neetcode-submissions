class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        map = {}
        res = 0
        for num in nums:
            map[num] = 1 + map.get(num+1,0)
            res = map[num] if map[num] > res else res
        
        return res