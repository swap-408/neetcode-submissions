class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        substr = ""
        def maxpodd(s,i):
            nonlocal res
            count = 1
            j = 1
            while i-j >=0 and i+j<len(s) and s[i-j]==s[i+j]:
                count += 2
                j += 1
            res += j
        def maxpeven(s,i):
            nonlocal res,substr
            count = 0
            j = 0
            while i-j >=0 and i+j+1<len(s) and s[i-j]==s[i+j+1]:
                count += 2
                j += 1
            res += j
        
        for i in range(0,len(s)):
            maxpodd(s,i)
            maxpeven(s,i)
        return res