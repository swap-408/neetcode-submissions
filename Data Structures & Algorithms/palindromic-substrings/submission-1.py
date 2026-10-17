class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def maxpodd(s,i):
            j = 1
            while i-j >=0 and i+j<len(s) and s[i-j]==s[i+j]:
                j += 1
            return j
        def maxpeven(s,i):
            
            j = 0
            while i-j >=0 and i+j+1<len(s) and s[i-j]==s[i+j+1]:j += 1
            return j
        
        for i in range(0,len(s)):
            res += maxpodd(s,i)
            res += maxpeven(s,i)
        return res