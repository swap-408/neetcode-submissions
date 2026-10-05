class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start, end = 0,0
        dic = {}
        while end < len(s):
            while end < len(s) and s[end] not in dic:
                dic[s[end]] = end
                end += 1 
            res = max(res, end-start)
            while start <= end and end<len(s) and s[end] in dic:
                dic.pop(s[start])
                start += 1
        
        res = max(res, end-start)
        return res