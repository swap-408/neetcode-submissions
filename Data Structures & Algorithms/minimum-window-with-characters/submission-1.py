class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq , window = {}, {}
        charSet = set(t)
        for c in t:
            freq[c] = freq.get(c,0)+1
        l = 0
        matches = 0
        res = s + "U"
        for r in range(0, len(s)):
            if s[r] in charSet:
                window[s[r]] = 1+ window.get(s[r],0)
                if window[s[r]]==freq[s[r]]: matches += 1


            while matches == len(charSet):
                res = s[l:r+1] if len(res)>(r-l+1) else res
                if s[l] in charSet:
                    if window[s[l]]==1:
                        window.pop(s[l])
                    else:
                        window[s[l]] -= 1
                    
                    if window.get(s[l],-1) < freq[s[l]]:
                        matches -= 1
                l += 1
        if res == s+"U": return ""
        return res
                    

