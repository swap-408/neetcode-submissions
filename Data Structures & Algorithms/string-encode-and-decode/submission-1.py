class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for idx in range(0,len(strs)):
            l = str(len(strs[idx]))
            d = str(len(l))
            s = s + d + l + strs[idx]

        return s
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0

        while idx < len(s):
            d = int(s[idx])
            idx += 1
            l = int(s[idx:idx+d])
            idx += d
            res.append(s[idx:idx+l])
            idx = idx + l
        return res
