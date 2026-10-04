class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for k in range(0,len(nums)-2):
            if k!=0 and nums[k]==nums[k-1]: continue
            l,r = k+1, len(nums)-1
            while l<r:
                sum = nums[l]+nums[r]+nums[k]
                if sum == 0:
                    res.append([nums[k],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l +=1
                    r -= 1
                elif sum<0:
                    l += 1
                else:
                    r -= 1
            k += 1
                
        return res