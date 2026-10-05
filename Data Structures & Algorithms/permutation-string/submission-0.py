class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freq1 = [0]*26
        for s in s1:
            freq1[ord(s)-ord('a')] += 1

        freq2 = [0]*26
        for i in range(0,len(s1)):
            freq2[ord(s2[i])-ord('a')] += 1
        
        if freq1 == freq2: return True

        n = len(s1)
        for i in range(n, len(s2)):
            freq2[ord(s2[i])-ord('a')] += 1
            freq2[ord(s2[i-n])-ord('a')] -= 1

            if freq1 == freq2: return True
        return False        