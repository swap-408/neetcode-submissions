class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lm,rm = [0]*n, [0]*n
        lm[0] = height[0]
        rm[n-1] = height[n-1]
        for idx in range(1,n):
            lm[idx] = max(height[idx],lm[idx-1])
        for idx in range(n-2,-1,-1):
            rm[idx] = max(height[idx],rm[idx+1])
        
        res =0
        for i in range(0,n):
            area = min(lm[i],rm[i]) - height[i]
            if area>0: res += area
            
        return res 