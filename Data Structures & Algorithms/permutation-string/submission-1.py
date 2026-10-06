class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freq1 = [0]*26
        freq2 = [0]*26
        for i in range(0,len(s1)):
            freq1[ord(s1[i])-ord('a')] += 1
            freq2[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(0,26):
            if freq1[i]==freq2[i]: matches += 1

        
        n = len(s1)
        if matches == 26: return True
        for i in range(n, len(s2)):
            r = ord(s2[i])-ord('a')
            freq2[r] += 1
            if freq2[r]-freq1[r] == 1: matches -= 1
            elif freq2[r]==freq1[r]: matches += 1

            l = ord(s2[i-n])-ord('a')
            freq2[l] -= 1
            if freq2[l]-freq1[l] == -1: matches -= 1
            elif freq2[l]==freq1[l]: matches += 1
            
            if matches == 26: return True
        return False        