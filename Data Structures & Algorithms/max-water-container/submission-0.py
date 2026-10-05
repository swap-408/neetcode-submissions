class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res =0
        while l<r:
            lh, rh = heights[l], heights[r]
            res = max(res,min(rh,lh)*(r-l))
            if lh < rh:
                l += 1
            else:
                r -= 1
        return res 